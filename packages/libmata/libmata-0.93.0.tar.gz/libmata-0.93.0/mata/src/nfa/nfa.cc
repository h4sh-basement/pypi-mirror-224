/* nfa.cc -- operations for NFA
 *
 * Copyright (c) 2018 Ondrej Lengal <ondra.lengal@gmail.com>
 *
 * This file is a part of libmata.
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 */

#include <algorithm>
#include <list>
#include <unordered_set>
#include <iterator>

// MATA headers
#include "mata/utils/sparse-set.hh"
#include "mata/nfa/nfa.hh"
#include "mata/nfa/algorithms.hh"
#include <mata/simlib/explicit_lts.hh>

using namespace Mata::Util;
using namespace Mata::Nfa;
using Mata::Symbol;
using Mata::BoolVector;

using StateBoolArray = std::vector<bool>; ///< Bool array for states in the automaton.

const std::string Mata::Nfa::TYPE_NFA = "NFA";

const State Limits::min_state;
const State Limits::max_state;
const Symbol Limits::min_symbol;
const Symbol Limits::max_symbol;

namespace {
    /**
     * Compute reachability of states.
     *
     * @param[in] nfa NFA to compute reachability for.
     * @return Bool array for reachable states (from initial states): true for reachable, false for unreachable states.
     */
    StateBoolArray compute_reachability(const Nfa& nfa) {
        std::vector<State> worklist{ nfa.initial.begin(),nfa.initial.end() };

        StateBoolArray reachable(nfa.size(), false);
        for (const State state: nfa.initial)
        {
            reachable.at(state) = true;
        }

        State state{};
        while (!worklist.empty())
        {
            state = worklist.back();
            worklist.pop_back();

            for (const SymbolPost& move: nfa.delta[state])
            {
                for (const State target_state: move.targets)
                {
                    if (!reachable.at(target_state))
                    {
                        worklist.push_back(target_state);
                        reachable.at(target_state) = true;
                    }
                }
            }
        }

        return reachable;
    }

    /**
     * Compute reachability of states considering only specified states.
     *
     * @param[in] nfa NFA to compute reachability for.
     * @param[in] states_to_consider State to consider as potentially reachable.
     * @return Bool array for reachable states (from initial states): true for reachable, false for unreachable states.
     */
    StateBoolArray compute_reachability(const Nfa& nfa, const StateBoolArray& states_to_consider) {
        std::vector<State> worklist{};
        StateBoolArray reachable(nfa.size(), false);
        for (const State state: nfa.initial) {
            if (states_to_consider[state]) {
                worklist.push_back(state);
                reachable.at(state) = true;
            }
        }

        State state;
        while (!worklist.empty()) {
            state = worklist.back();
            worklist.pop_back();

            for (const SymbolPost& move: nfa.delta[state]) {
                for (const State target_state: move.targets) {
                    if (states_to_consider[target_state] && !reachable[target_state]) {
                        worklist.push_back(target_state);
                        reachable[target_state] = true;
                    }
                }
            }
        }

        return reachable;
    }

    /**
     * Add transitions to the trimmed automaton.
     * @param[in] nfa NFA to add transitions from.
     * @param[in] state_renaming Map of old states to new trimmed automaton states.
     * @param[out] trimmed_aut The new trimmed automaton.
     */
    void add_trimmed_transitions(const Nfa& nfa, const StateRenaming& state_renaming, Nfa& trimmed_aut) {
        // For each reachable original state 's' (which means it is mapped to the state of trimmed automaton)...
        for (const auto& original_state_mapping: state_renaming)
        {
            // ...add all transitions from 's' to some reachable state to the trimmed automaton.
            for (const auto& state_transitions_with_symbol: nfa.delta[original_state_mapping.first])
            {
                SymbolPost new_state_trans_with_symbol(state_transitions_with_symbol.symbol);
                for (State old_state_to: state_transitions_with_symbol.targets)
                {
                    auto iter_to_new_state_to = state_renaming.find(old_state_to);
                    if (iter_to_new_state_to != state_renaming.end())
                    {
                        // We can push here, because we assume that new states follow the ordering of original states.
                        new_state_trans_with_symbol.insert(iter_to_new_state_to->second);
                    }
                }
                if (!new_state_trans_with_symbol.empty()) {
                    trimmed_aut.delta.mutable_state_post(original_state_mapping.second).insert(new_state_trans_with_symbol);
                }
            }
        }
    }

    /**
     * Get a new trimmed automaton.
     * @param[in] nfa NFA to trim.
     * @param[in] original_to_new_state_renaming Map of old states to new trimmed automaton states (new states should follow the ordering of old states).
     * @return Newly created trimmed automaton.
     */
    Nfa create_trimmed_aut(const Nfa& nfa, const StateRenaming& state_renaming) {
        Nfa trimmed_aut{ state_renaming.size() };

        for (const State old_initial_state: nfa.initial)
        {
            if (state_renaming.find(old_initial_state) != state_renaming.end())
            {
                trimmed_aut.initial.insert(state_renaming.at(old_initial_state));
            }
        }
        for (const State old_final_state: nfa.final)
        {
            if (state_renaming.find(old_final_state) != state_renaming.end())
            {
                trimmed_aut.final.insert(state_renaming.at(old_final_state));
            }
        }

        add_trimmed_transitions(nfa, state_renaming, trimmed_aut);
        return trimmed_aut;
    }

    /**
     * Get directed transitions for digraph.
     * @param[in] nfa NFA to get directed transitions from.
     * @param[in] abstract_symbol Abstract symbol to use for transitions in digraph.
     * @param[out] digraph Digraph to add computed transitions to.
     */
    void collect_directed_transitions(const Nfa& nfa, const Symbol abstract_symbol, Nfa& digraph) {
        const State num_of_states{nfa.size() };
        for (State src_state{ 0 }; src_state < num_of_states; ++src_state) {
            for (const SymbolPost& move: nfa.delta[src_state]) {
                for (const State tgt_state: move.targets) {
                    // Directly try to add the transition. Finding out whether the transition is already in the digraph
                    //  only iterates through transition relation again.
                    digraph.delta.add(src_state, abstract_symbol, tgt_state);
                }
                // FIXME: Alternatively: But it is actually slower...
                //digraph.add(src_state, abstract_symbol, symbol_transitions.targets);
            }
        }
    }
}

void Nfa::remove_epsilon(const Symbol epsilon)
{
    *this = Mata::Nfa::remove_epsilon(*this, epsilon);
}

StateSet Nfa::get_reachable_states() const
{
    StateBoolArray reachable_bool_array{ compute_reachability(*this) };

    StateSet reachable_states{};
    const size_t num_of_states{size() };
    for (State original_state{ 0 }; original_state < num_of_states; ++original_state)
    {
        if (reachable_bool_array[original_state])
        {
            reachable_states.insert(original_state);
        }
    }

    return reachable_states;
}

StateSet Nfa::get_terminating_states() const
{
    return revert(*this).get_reachable_states();
}

//TODO: probably can be removed, trim_inplace is faster.
void Nfa::trim_reverting(StateRenaming* state_renaming)
{
    if (!state_renaming) {
        StateRenaming tmp_state_renaming{};
        *this = get_trimmed_automaton(&tmp_state_renaming);
    } else {
        state_renaming->clear();
        *this = get_trimmed_automaton(state_renaming);
    }
}

void Nfa::trim_inplace(StateRenaming* state_renaming) {
#ifdef _STATIC_STRUCTURES_
    BoolVector useful_states{ useful_states() };
    useful_states.clear();
    useful_states = useful_states();
#else
    BoolVector useful_states{ get_useful_states() };
#endif
    const size_t useful_states_size{ useful_states.size() };
    std::vector<State> renaming(useful_states_size);
    for(State new_state{ 0 }, orig_state{ 0 }; orig_state < useful_states_size; ++orig_state) {
        if (useful_states[orig_state]) {
            renaming[orig_state] = new_state;
            ++new_state;
        }
    }

    delta.defragment(useful_states, renaming);

    auto is_state_useful = [&](State q){return q < useful_states.size() && useful_states[q];};
    initial.filter(is_state_useful);
    final.filter(is_state_useful);
    auto rename_state = [&](State q){return renaming[q];};
    initial.rename(rename_state);
    final.rename(rename_state);
    initial.truncate();
    final.truncate();
    if (state_renaming != nullptr) {
        state_renaming->clear();
        state_renaming->reserve(useful_states_size);
        for (State q{ 0 }; q < useful_states_size; ++q) {
            if (useful_states[q]) {
                (*state_renaming)[q] = renaming[q];
            }
        }
    }
}

Nfa Nfa::get_trimmed_automaton(StateRenaming* state_renaming) const {
    if (initial.empty() || final.empty()) { return Nfa{}; }

    StateRenaming tmp_state_renaming{};
    if (!state_renaming) {
        state_renaming = &tmp_state_renaming;
    }
    state_renaming->clear();

    const StateSet original_useful_states{get_useful_states_old() };
    state_renaming->reserve(original_useful_states.size());

    size_t new_state_num{ 0 };
    for (const State original_state: original_useful_states) {
        (*state_renaming)[original_state] = new_state_num;
        ++new_state_num;
    }
    return create_trimmed_aut(*this, *state_renaming);
}

namespace {
    // A structure to store metadata related to each state/node during the computation
    // of useful states. It contains Tarjan's metadata and the state of the
    // iteration through the successors.
    struct TarjanNodeData {
        StatePost::const_iterator post_it{};
        StatePost::const_iterator post_end{};
        StateSet::const_iterator targets_it{};
        StateSet::const_iterator targets_end{};
        // index of a node (corresponds to the time of discovery)
        unsigned long index{ 0 };
        // index of a lower node in the same SCC
        unsigned long lowlink{ 0 };
        // was the node already initialized (=the initial phase of the Tarjan's recursive call was executed)
        bool initilized{ false };
        // is node on Tarjan's stack?
        bool on_stack{ false };

        TarjanNodeData() = default;

        TarjanNodeData(State q, const Delta & delta, unsigned long index)
            : post_it(delta[q].cbegin()), post_end(delta[q].cend()), index(index), lowlink(index), initilized(true), on_stack(true) {
            if (post_it != post_end) {
                targets_it = post_it->cbegin();
                targets_end = post_it->cend();
            }
        };

        // TODO: this sucks. In fact, if you want to check that you have the last sucessor, you need to
        // first align the iterators.
        // TODO: this is super-ugly. If we introduce Post::transitions iterator, this could be much easier.
        // Align iterators in a way that the current state is stored in *(this->targets_it).
        void align_succ() {
            while (this->post_it != this->post_end && this->targets_it == this->targets_end) {
                if (this->targets_it == this->targets_end) {
                    ++this->post_it;
                    if (this->post_it != this->post_end) {
                        this->targets_it = this->post_it->cbegin();
                        this->targets_end = this->post_it->cend();
                    }
                }
            }
        }

        State get_curr_succ() {
            align_succ();
            return *(this->targets_it);
        }

        void move_to_next_succ() {
            if(this->post_it == this->post_end) {
                return;
            }
            ++this->targets_it;
        }

        bool is_end_succ() {
            align_succ();
            return this->post_it == this->post_end;
        }
    };
};

/**
 * @brief This function employs non-recursive version of Tarjan's algorithm for finding SCCs
 * (see https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm, in particular strongconnect(v))
 * The method saturates a bool vector @p reached_and_reaching in a way that reached_and_reaching[i] = true iff
 * the state i is useful at the end. To break the recursiveness, we use @p program_stack simulating
 * the program stack during the recursive calls of strongconnect(v) (see the wiki).
 *
 * Node data
 *  - lowlink, index, on_stack (the same as from strongconnect(v))
 *  - initialized (flag denoting whether the node started to be processing in strongconnect)
 *  - bunch of iterators allowing to iterate over successors (and store the state of the iteration)
 *
 * Program stack @p program_stack
 *  - contains nodes
 *  - node on the top is being currently processed
 *  - node is removed after it has been completely processed (after the end of strongconnect)
 *
 * Simulation of strongconnect( @p act_state = v )
 *  - if @p act_state is not initialized yet (corresponds to the initial phase of strongconnect), initialize
 *  - if @p act_state has already been initialized (i.e., processing of @p act_state was resumed by a
 *    recursive call, which already finished and we continue in processing of @p act_state ), we set
 *    @p act_state lowlink to min of current lowlink and the current successor @p act_succ of @p act_state.
 *    @p act_succ corresponds to w in strongconnect(v). In particular, in strongconnect(v) we called
 *    strongconnect(w) and now we continue after the return.
 *  - Then, we continue iterating over successors @p next_state of @p act_state:
 *      * if @p next_state is not initialized (corresponds to the first if in strongconnect(v)), we simulate
 *        the recursive call of strongconnect( @p next_state ): we put @p next_state on @p program_stack and
 *        jump to the processing of a new node from @p program_stack (we do not remove @p act_state from program
 *        stack yet).
 *      * otherwise update the lowlink
 *  - The rest corresponds to the last part of strongconnect(v) with a difference that if a node in the closed
 *    SCC if useful, we declare all nodes in the SCC useful and moreover we propagate usefulness also the states
 *    in @p tarjan_stack as it contains states that can reach this closed SCC.
 *
 * @return BoolVector
 */
BoolVector Nfa::get_useful_states() const {
    BoolVector useful(this->size(),false);
    std::vector<TarjanNodeData> node_info(this->size());
    std::deque<State> program_stack;
    std::deque<State> tarjan_stack;
    unsigned long index_cnt = 0;

    for(const State& q0 : initial) {
        program_stack.push_back(q0);
    }

    while(!program_stack.empty()) {
        State act_state = program_stack.back();
        TarjanNodeData& act_state_data = node_info[act_state];

        // if a node is initialized and is not on stack --> skip it; this state was
        // already processed (=this state is initial and was reachable from another initial).
        if(act_state_data.initilized && !act_state_data.on_stack) {
            program_stack.pop_back();
            continue;
        }

        // node has not been initialized yet --> corresponds to the first call of strongconnect(act_state)
        if(!act_state_data.initilized) {
            // initialize node
            act_state_data = TarjanNodeData(act_state, this->delta, index_cnt++);
            tarjan_stack.push_back(act_state);
            if(this->final.contains(act_state)) {
                useful[act_state] = true;
            }
        } else { // return from the recursive call
            State act_succ = act_state_data.get_curr_succ();
            act_state_data.lowlink = std::min(act_state_data.lowlink, node_info[act_succ].lowlink);
            // act_succ is the state that cased the recursive call. Move to another successor.
            act_state_data.move_to_next_succ();
        }

        // iterate through outgoing edges
        State next_state;
        // rec_call simulates call of the strongconnect. Since c++ cannot do continue over
        // multiple loops, we use rec_call to jump to the main loop
        bool rec_call = false;
        while(!act_state_data.is_end_succ()) {
            next_state = act_state_data.get_curr_succ();
            // if successor is useful, act_state is useful as well
            if(useful[next_state]) {
                useful[act_state] = true;
            }
            if(!node_info[next_state].initilized) { // recursive call
                program_stack.push_back(next_state);
                rec_call = true;
                break;
            } else if(node_info[next_state].on_stack) {
                act_state_data.lowlink = std::min(act_state_data.lowlink, node_info[next_state].index);
            }
            act_state_data.move_to_next_succ();
        }
        if(rec_call) continue;

        // check if we have the root of a SCC
        if(act_state_data.lowlink == act_state_data.index) {
            State st;
            // contains the closed SCC a final state
            bool final_scc = false;
            std::vector<State> scc;
            do {
                st = tarjan_stack.back();
                tarjan_stack.pop_back();
                node_info[st].on_stack = false;

                // SCC contains a final state
                if(useful[st]) {
                    final_scc = true;
                }
                scc.push_back(st);
            } while(st != act_state);
            if(final_scc) {
                // propagate usefulness to the closed SCC
                for(const State& st : scc) useful[st] = true;
                // propagate usefulness to predecessors in @p tarjan_stack
                for(const State& st : tarjan_stack) useful[st] = true;
            }
        }
        // all successors have been processed, we can remove act_state from the program stack
        program_stack.pop_back();
    }

    return useful;
}

StateSet Nfa::get_useful_states_old() const
{
    if (initial.empty() || final.empty()) { return StateSet{}; }

    const Nfa digraph{get_one_letter_aut() }; // Compute reachability on directed graph.
    // Compute reachability from the initial states and use the reachable states to compute the reachability from the final states.
    const StateBoolArray useful_states_bool_array{ compute_reachability(revert(digraph), compute_reachability(digraph)) };

    const size_t num_of_states{size() };
    StateSet useful_states{};
    for (State original_state{ 0 }; original_state < num_of_states; ++original_state) {
        if (useful_states_bool_array[original_state]) {
            // We can use push_back here, because we are always increasing the value of original_state (so useful_states
            //  will always be ordered).
            useful_states.insert(original_state);
        }
    }
    return useful_states;
}

std::string Nfa::print_to_DOT() const {
    std::stringstream output;
    print_to_DOT(output);
    return output.str();
}

void Nfa::print_to_DOT(std::ostream &output) const {
    output << "digraph finiteAutomaton {" << std::endl
                 << "node [shape=circle];" << std::endl;

    for (State final_state: final) {
        output << final_state << " [shape=doublecircle];" << std::endl;
    }

    const size_t delta_size = delta.num_of_states();
    for (State source = 0; source != delta_size; ++source) {
        for (const SymbolPost &move: delta[source]) {
            output << source << " -> {";
            for (State target: move.targets) {
                output << target << " ";
            }
            output << "} [label=" << move.symbol << "];" << std::endl;
        }
    }

    output << "node [shape=none, label=\"\"];" << std::endl;
    for (State init_state: initial) {
        output << "i" << init_state << " -> " << init_state << ";" << std::endl;
    }

    output << "}" << std::endl;
}

std::string Nfa::print_to_mata() const {
    std::stringstream output;
    print_to_mata(output);
    return output.str();
}

void Nfa::print_to_mata(std::ostream &output) const {
    output << "@NFA-explicit" << std::endl
           << "%Alphabet-auto" << std::endl;
           // TODO should be this, but we cannot parse %Alphabet-numbers yet
           //<< "%Alphabet-numbers" << std::endl;

    if (!initial.empty()) {
        output << "%Initial";
        for (State init_state: initial) {
            output << " q" << init_state;
        }
        output << std::endl;
    }

    if (!final.empty()) {
        output << "%Final";
        for (State final_state: final) {
            output << " q" << final_state;
        }
        output << std::endl;
    }

    for (Transition trans : delta.transitions()) {
        output << "q" << trans.source << " " << trans.symbol << " q" << trans.target << std::endl;
    }
}

std::vector<Transition> Nfa::get_trans_as_sequence() const
{
    std::vector<Transition> trans_sequence{};

    for (State state_from{ 0 }; state_from < delta.num_of_states(); ++state_from)
    {
        for (const auto& transition_from_state: delta[state_from])
        {
            for (State state_to: transition_from_state.targets)
            {
                trans_sequence.push_back(Transition{ state_from, transition_from_state.symbol, state_to });
            }
        }
    }

    return trans_sequence;
}

std::vector<Transition> Nfa::get_trans_from_as_sequence(State state_from) const
{
    std::vector<Transition> trans_sequence{};

    for (const auto& transition_from_state: delta[state_from])
    {
        for (State state_to: transition_from_state.targets)
        {
            trans_sequence.emplace_back(state_from, transition_from_state.symbol, state_to);
        }
    }

    return trans_sequence;
}

Nfa Nfa::get_one_letter_aut(Symbol abstract_symbol) const {
    Nfa digraph{size(), StateSet(initial), StateSet(final) };
    collect_directed_transitions(*this, abstract_symbol, digraph);
    return digraph;
}

void Nfa::get_one_letter_aut(Nfa& result) const {
    result = get_one_letter_aut();
}

std::vector<Transition> Nfa::get_transitions_to(State state_to) const {
    std::vector<Transition> transitions_to_state{};
    const size_t num_of_states{ delta.num_of_states() };
    for (State state_from{ 0 }; state_from < num_of_states; ++state_from) {
        for (const SymbolPost& state_from_move: delta[state_from]) {
            const auto target_state{ state_from_move.targets.find(state_to) };
            if (target_state != state_from_move.targets.end()) {
                transitions_to_state.emplace_back(state_from, state_from_move.symbol, state_to );
            }
        }
    }
    return transitions_to_state;
}

StateSet Nfa::post(const StateSet& states, const Symbol& symbol) const {
    StateSet res{};
    if (delta.empty()) {
        return res;
    }

    for (const State state: states) {
        const StatePost& post{ delta[state] };
        const auto move_it{ post.find(symbol) };
        if (move_it != post.end()) {
            res.insert(move_it->targets);
        }
    }
    return res;
}

Nfa::const_iterator Nfa::const_iterator::for_begin(const Nfa* nfa)
{ // {{{
    assert(nullptr != nfa);

    const_iterator result;

    if (nfa->delta.transitions_begin() == nfa->delta.transitions_end()) {
        result.is_end = true;
        return result;
    }

    result.nfa = nfa;

    for (size_t trIt{ 0 }; trIt < nfa->delta.num_of_states(); ++trIt) {
        auto& moves{ nfa->delta.state_post(trIt) };
        if (!moves.empty()) {
            auto move{ moves.begin() };
            while (move != moves.end()) {
                if (!move->targets.empty()) {
                    result.trIt = trIt;
                    result.tlIt = moves.begin();
                    result.ssIt = result.tlIt->targets.begin();
                    break;
                }
                ++move;
            }
            break;
        }
    }

    result.refresh_trans();

    return result;
} // for_begin }}}

Nfa::const_iterator Nfa::const_iterator::for_end(const Nfa* /* nfa*/)
{ // {{{
    const_iterator result;
    result.is_end = true;
    return result;
} // for_end }}}

Nfa::const_iterator& Nfa::const_iterator::operator++()
{ // {{{
    assert(nullptr != nfa);

    ++(this->ssIt);
    const StateSet& state_set = this->tlIt->targets;
    assert(!state_set.empty());
    if (this->ssIt != state_set.end())
    {
        this->refresh_trans();
        return *this;
    }

    // out of state set
    ++(this->tlIt);
    const StatePost& tlist = this->nfa->delta.state_post(this->trIt);
    assert(!tlist.empty());
    if (this->tlIt != tlist.end())
    {
        this->ssIt = this->tlIt->targets.begin();

        this->refresh_trans();
        return *this;
    }

    // out of transition list
    ++this->trIt;
    assert(this->nfa->delta.transitions_begin() != this->nfa->delta.transitions_end());

    while (this->trIt < this->nfa->delta.num_of_states() &&
           this->nfa->delta.state_post(this->trIt).empty())
    {
        ++this->trIt;
    }

    if (this->trIt < this->nfa->delta.num_of_states())
    {
        this->tlIt = this->nfa->delta.state_post(this->trIt).begin();
        assert(!this->nfa->delta.state_post(this->trIt).empty());
        const StateSet& new_state_set = this->tlIt->targets;
        assert(!new_state_set.empty());
        this->ssIt = new_state_set.begin();

        this->refresh_trans();
        return *this;
    }

    // out of transitions
    this->is_end = true;

    return *this;
}

bool Nfa::const_iterator::operator==(const Nfa::const_iterator& rhs) const {
    if (this->is_end && rhs.is_end) { return true; }
    if ((this->is_end && !rhs.is_end) || (!this->is_end && rhs.is_end)) { return false; }
    return ssIt == rhs.ssIt && tlIt == rhs.tlIt && trIt == rhs.trIt;
}

// Other versions, maybe an interesting experiment with speed of data structures.
// Returns symbols appearing in Delta, pushes back to vector and then sorts
Mata::Util::OrdVector<Symbol> Nfa::get_used_symbols_vec() const {
#ifdef _STATIC_STRUCTURES_
    static std::vector<Symbol> symbols{};
    symbols.clear();
#else
    std::vector<Symbol>  symbols{};
#endif
    for (State q = 0; q< delta.num_of_states(); ++q) {
        const StatePost & post = delta[q];
        for (const SymbolPost & move: post) {
            Util::reserve_on_insert(symbols);
            symbols.push_back(move.symbol);
        }
    }
    Util::OrdVector<Symbol>  sorted_symbols(symbols);
    return sorted_symbols;
}

// returns symbols appearing in Delta, inserts to a std::set
std::set<Symbol> Nfa::get_used_symbols_set() const {
    //static should prevent reallocation, seems to speed things up a little
#ifdef _STATIC_STRUCTURES_
    static std::set<Symbol>  symbols;
    symbols.clear();
#else
    static std::set<Symbol>  symbols{};
#endif
    for (State q = 0; q< delta.num_of_states(); ++q) {
        const StatePost & post = delta[q];
        for (const SymbolPost & move: post) {
            symbols.insert(move.symbol);
        }
    }
    return symbols;
    //Util::OrdVector<Symbol>  sorted_symbols(symbols.begin(),symbols.end());
    //return sorted_symbols;
}

// returns symbols appearing in Delta, adds to NumberPredicate,
// Seems to be the fastest option, but could have problems with large maximum symbols
Mata::Util::SparseSet<Symbol> Nfa::get_used_symbols_sps() const {
#ifdef _STATIC_STRUCTURES_
    //static seems to speed things up a little
    static Util::SparseSet<Symbol>  symbols(64,false);
    symbols.clear();
#else
    Util::SparseSet<Symbol>  symbols(64);
#endif
    //symbols.dont_track_elements();
    for (State q = 0; q< delta.num_of_states(); ++q) {
        const StatePost & post = delta[q];
        for (const SymbolPost & move: post) {
            symbols.insert(move.symbol);
        }
    }
    //TODO: is it necessary to return ordered vector? Would the number predicate suffice?
    return symbols;
}

// returns symbols appearing in Delta, adds to NumberPredicate,
// Seems to be the fastest option, but could have problems with large maximum symbols
std::vector<bool> Nfa::get_used_symbols_bv() const {
#ifdef _STATIC_STRUCTURES_
    //static seems to speed things up a little
    static std::vector<bool>  symbols(64,false);
    symbols.clear();
#else
    std::vector<bool> symbols(64,false);
#endif
    //symbols.dont_track_elements();
    for (State q = 0; q< delta.num_of_states(); ++q) {
        const StatePost & post = delta[q];
        for (const SymbolPost & move: post) {
            reserve_on_insert(symbols,move.symbol);
            symbols[move.symbol]=true;
        }
    }
    //TODO: is it neccessary toreturn ordered vector? Would the number predicate suffice?
    return symbols;
}

BoolVector Nfa::get_used_symbols_chv() const {
#ifdef _STATIC_STRUCTURES_
    //static seems to speed things up a little
    static BoolVector  symbols(64,false);
    symbols.clear();
#else
    BoolVector symbols(64,false);
#endif
    //symbols.dont_track_elements();
    for (State q = 0; q< delta.num_of_states(); ++q) {
        const StatePost & post = delta[q];
        for (const SymbolPost & move: post) {
            reserve_on_insert(symbols,move.symbol);
            symbols[move.symbol]=true;
        }
    }
    //TODO: is it necessary to return ordered vector? Would the number predicate suffice?
    return symbols;
}

// returns max non-e symbol in Delta
Symbol Nfa::get_max_symbol() const {
    Symbol max = 0;
    for (State q = 0; q< delta.num_of_states(); ++q) {
        const StatePost & post = delta[q];
        for (const SymbolPost & move: post) {
            if (move.symbol > max)
                max = move.symbol;
        }
    }
    return max;
}

 void Nfa::unify_initial() {
    if (initial.empty() || initial.size() == 1) { return; }
    const State new_initial_state{add_state() };
    for (const State orig_initial_state: initial) {
        const StatePost& moves{ delta.state_post(orig_initial_state) };
        for (const auto& transitions: moves) {
            for (const State state_to: transitions.targets) {
                delta.add(new_initial_state, transitions.symbol, state_to);
            }
        }
        if (final[orig_initial_state]) { final.insert(new_initial_state); }
    }
    initial.clear();
    initial.insert(new_initial_state);
}

void Nfa::unify_final() {
    if (final.empty() || final.size() == 1) { return; }
    const State new_final_state{ add_state() };
    for (const auto& orig_final_state: final) {
        const auto transitions_to{ get_transitions_to(orig_final_state) };
        for (const auto& transitions: transitions_to) {
            delta.add(transitions.source, transitions.symbol, new_final_state);
        }
        if (initial[orig_final_state]) { initial.insert(new_final_state); }
    }
    final.clear();
    final.insert(new_final_state);
}

void Nfa::add_symbols_to(OnTheFlyAlphabet& target_alphabet) const {
    size_t aut_num_of_states{size() };
    for (Mata::Nfa::State state{ 0 }; state < aut_num_of_states; ++state) {
        for (const SymbolPost& move: delta[state]) {
            target_alphabet.update_next_symbol_value(move.symbol);
            target_alphabet.try_add_new_symbol(std::to_string(move.symbol), move.symbol);
        }
    }
}

Nfa& Nfa::operator=(Nfa&& other) noexcept {
    if (this != &other) {
        delta = std::move(other.delta);
        initial = std::move(other.initial);
        final = std::move(other.final);
        alphabet = other.alphabet;
        attributes = std::move(other.attributes);
        other.alphabet = nullptr;
    }
    return *this;
}

void Nfa::clear_transitions() {
    const size_t delta_size = delta.num_of_states();
    for (size_t i = 0; i < delta_size; ++i) {
        delta.mutable_state_post(i) = StatePost();
    }
}

State Nfa::add_state() {
    const size_t num_of_states{ size() };
    delta.increase_size(num_of_states + 1);
    return num_of_states;
}

State Nfa::add_state(State state) {
    if (state >= delta.num_of_states()) {
        delta.increase_size(state + 1);
    }
    return state;
}

size_t Nfa::size() const {
    return std::max({
        static_cast<unsigned long>(initial.domain_size()),
        static_cast<unsigned long>(final.domain_size()),
        static_cast<unsigned long>(delta.num_of_states())
    });
}

void Nfa::clear() {
    delta.clear();
    initial.clear();
    final.clear();
}

bool Nfa::is_identical(const Nfa& aut) {
    if (Util::OrdVector<State>(initial) != Util::OrdVector<State>(aut.initial)) {
        return false;
    }
    if (Util::OrdVector<State>(final) != Util::OrdVector<State>(aut.final)) {
        return false;
    }

    std::vector<Transition> this_trans;
    for (auto trans: *this) { this_trans.push_back(trans); }
    std::vector<Transition> aut_trans;
    for (auto trans: aut) { aut_trans.push_back(trans); }
    return this_trans == aut_trans;
}

OrdVector<Symbol> Nfa::get_used_symbols() const {
    //TODO: look at the variants in profiling (there are tests in tests-nfa-profiling.cc),
    // for instance figure out why NumberPredicate and OrdVedctor are slow,
    // try also with _STATIC_DATA_STRUCTURES_, it changes things.

    //below are different variant, with different data structures for accumulating symbols,
    //that then must be converted to an OrdVector
    //measured are times with "Mata::Nfa::get_used_symbols speed, harder", "[.profiling]" now on line 104 of nfa-profiling.cc

    //WITH VECTOR (4.434 s)
    //return get_used_symbols_vec();

    //WITH SET (26.5 s)
    //auto from_set = get_used_symbols_set();
    //return Util::OrdVector<Symbol> (from_set .begin(),from_set.end());

    //WITH NUMBER PREDICATE (4.857s) (NP removed)
    //return Util::OrdVector(get_used_symbols_np().get_elements());

    //WITH SPARSE SET (haven't tried)
    //return Util::OrdVector<State>(get_used_symbols_sps());

    //WITH BOOL VECTOR (error !!!!!!!):
    //return Util::OrdVector<Symbol>(Util::NumberPredicate<Symbol>(get_used_symbols_bv()));

    //WITH BOOL VECTOR (1.9s):
    std::vector<bool> bv = get_used_symbols_bv();
    Util::OrdVector<Symbol> ov;
    for(Symbol i = 0;i<bv.size();i++)
        if (bv[i]) {
            ov.push_back(i);
        }
    return ov;

    ///WITH BOOL VECTOR, DIFFERENT VARIANT? (1.9s):
    //std::vector<bool> bv = get_used_symbols_bv();
    //std::vector<Symbol> v(std::count(bv.begin(), bv.end(), true));
    //return Util::OrdVector<Symbol>(v);

    //WITH CHAR VECTOR (should be the fastest, haven't tried in this branch):
    //BEWARE: failing in one noodlificatoin test ("Simple automata -- epsilon result") ... strange
    //BoolVector chv = get_used_symbols_chv();
    //Util::OrdVector<Symbol> ov;
    //for(Symbol i = 0;i<chv.size();i++)
    //    if (chv[i]) {
    //        ov.push_back(i);
    //    }
    //return ov;
}
