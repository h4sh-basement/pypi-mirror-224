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
#include "mata/nfa/delta.hh"
#include "mata/utils/sparse-set.hh"
#include "mata/nfa/nfa.hh"
#include "mata/nfa/algorithms.hh"
#include "mata/nfa/builder.hh"
#include <mata/simlib/explicit_lts.hh>

using std::tie;

using namespace Mata::Util;
using namespace Mata::Nfa;
using Mata::Symbol;

using StateBoolArray = std::vector<bool>; ///< Bool array for states in the automaton.

namespace {
    Simlib::Util::BinaryRelation compute_fw_direct_simulation(const Nfa& aut) {
        Symbol maxSymbol = 0;
        const size_t state_num = aut.size();
        Simlib::ExplicitLTS LTSforSimulation(state_num);

        for (const auto& transition : aut.delta.transitions()) {
            LTSforSimulation.add_transition(transition.source, transition.symbol, transition.target);
            if (transition.symbol > maxSymbol) {
                maxSymbol = transition.symbol;
            }
        }

        // final states cannot be simulated by nonfinal -> we add new selfloops over final states with new symbol in LTS
        for (State finalState : aut.final) {
            LTSforSimulation.add_transition(finalState, maxSymbol + 1, finalState);
        }

        LTSforSimulation.init();
        return LTSforSimulation.compute_simulation();
    }

    Nfa reduce_size_by_simulation(const Nfa& aut, StateRenaming &state_renaming) {
        Nfa result;
        const auto sim_relation = Algorithms::compute_relation(
                aut, ParameterMap{{ "relation", "simulation"}, { "direction", "forward"}});

        auto sim_relation_symmetric = sim_relation;
        sim_relation_symmetric.restrict_to_symmetric();

        // for State q, quot_proj[q] should be the representative state representing the symmetric class of states in simulation
        std::vector<size_t> quot_proj;
        sim_relation_symmetric.get_quotient_projection(quot_proj);

        const size_t num_of_states = aut.size();

        // map each state q of aut to the state of the reduced automaton representing the simulation class of q
        for (State q = 0; q < num_of_states; ++q) {
            const State qReprState = quot_proj[q];
            if (state_renaming.count(qReprState) == 0) { // we need to map q's class to a new state in reducedAut
                const State qClass = result.add_state();
                state_renaming[qReprState] = qClass;
                state_renaming[q] = qClass;
            } else {
                state_renaming[q] = state_renaming[qReprState];
            }
        }

        for (State q = 0; q < num_of_states; ++q) {
            const State q_class_state = state_renaming.at(q);

            if (aut.initial[q]) { // if a symmetric class contains initial state, then the whole class should be initial
                result.initial.insert(q_class_state);
            }

            if (quot_proj[q] == q) { // we process only transitions starting from the representative state, this is enough for simulation
                for (const auto &q_trans : aut.delta.state_post(q)) {
                    const StateSet representatives_of_states_to = [&]{
                        StateSet state_set;
                        for (auto s : q_trans.targets) {
                            state_set.insert(quot_proj[s]);
                        }
                        return state_set;
                    }();

                    // get the class states of those representatives that are not simulated by another representative in representatives_of_states_to
                    StateSet representatives_class_states;
                    for (const State s : representatives_of_states_to) {
                        bool is_state_important = true; // if true, we need to keep the transition from q to s
                        for (const State p : representatives_of_states_to) {
                            if (s != p && sim_relation.get(s, p)) { // if p (different from s) simulates s
                                is_state_important = false; // as p simulates s, the transition from q to s is not important to keep, as it is subsumed in transition from q to p
                                break;
                            }
                        }
                        if (is_state_important) {
                            representatives_class_states.insert(state_renaming.at(s));
                        }
                    }

                    // add the transition 'q_class_state-q_trans.symbol->representatives_class_states' at the end of transition list of transitions starting from q_class_state
                    // as the q_trans.symbol should be the largest symbol we saw (as we iterate trough getTransitionsFromState(q) which is ordered)
                    result.delta.mutable_state_post(q_class_state).insert(SymbolPost(q_trans.symbol, representatives_class_states));
                }

                if (aut.final[q]) { // if q is final, then all states in its class are final => we make q_class_state final
                    result.final.insert(q_class_state);
                }
            }
        }

        return result;
    }
}

std::ostream &std::operator<<(std::ostream &os, const Mata::Nfa::Transition &trans) { // {{{
    std::string result = "(" + std::to_string(trans.source) + ", " +
                         std::to_string(trans.symbol) + ", " + std::to_string(trans.target) + ")";
    return os << result;
}

bool Mata::Nfa::make_complete(Nfa& aut, const Alphabet& alphabet, State sink_state) {
    return Mata::Nfa::make_complete(aut, alphabet.get_alphabet_symbols(), sink_state);
}

bool Mata::Nfa::make_complete(Nfa& aut, const Mata::Util::OrdVector<Symbol>& symbols, State sink_state) {
    bool was_something_added{ false };

    size_t num_of_states{ aut.size() };
    for (State state = 0; state < num_of_states; ++state) {
        OrdVector<Symbol> used_symbols{};
        for (auto const &move : aut.delta[state]) {
            used_symbols.insert(move.symbol);
        }
        Mata::Util::OrdVector<Symbol> unused_symbols{ symbols.difference(used_symbols) };
        for (Symbol symb : unused_symbols) {
            aut.delta.add(state, symb, sink_state);
            was_something_added = true;
        }
    }

    if (was_something_added && num_of_states <= sink_state) {
        for (Symbol symbol : symbols) {
            aut.delta.add(sink_state, symbol, sink_state);
        }
    }

    return was_something_added;
}

//TODO: based on the comments inside, this function needs to be rewritten in a more optimal way.
Nfa Mata::Nfa::remove_epsilon(const Nfa& aut, Symbol epsilon) {
    // cannot use multimap, because it can contain multiple occurrences of (a -> a), (a -> a)
    std::unordered_map<State, StateSet> eps_closure;

    // TODO: grossly inefficient
    // first we compute the epsilon closure
    const size_t num_of_states{aut.size() };
    for (size_t i{ 0 }; i < num_of_states; ++i)
    {
        for (const auto& trans: aut.delta[i])
        { // initialize
            const auto it_ins_pair = eps_closure.insert({i, {i}});
            if (trans.symbol == epsilon)
            {
                StateSet& closure = it_ins_pair.first->second;
                // TODO: Fix possibly insert to OrdVector. Create list already ordered, then merge (do not need to resize each time);
                closure.insert(trans.targets);
            }
        }
    }

    bool changed = true;
    while (changed) { // Compute the fixpoint.
        changed = false;
        for (size_t i = 0; i < num_of_states; ++i) {
            const StatePost& post{ aut.delta[i] };
            const auto eps_move_it { post.find(epsilon) };//TODO: make faster if default epsilon
            if (eps_move_it != post.end()) {
                StateSet& src_eps_cl = eps_closure[i];
                for (const State tgt: eps_move_it->targets) {
                    const StateSet& tgt_eps_cl = eps_closure[tgt];
                    for (const State st: tgt_eps_cl) {
                        if (src_eps_cl.count(st) == 0) {
                            changed = true;
                            break;
                        }
                    }
                    src_eps_cl.insert(tgt_eps_cl);
                }
            }
        }
    }

    // Construct the automaton without epsilon transitions.
    Nfa result{ Delta{}, aut.initial, aut.final, aut.alphabet };
    for (const auto& state_closure_pair : eps_closure) { // For every state.
        State src_state = state_closure_pair.first;
        for (State eps_cl_state : state_closure_pair.second) { // For every state in its epsilon closure.
            if (aut.final[eps_cl_state]) result.final.insert(src_state);
            for (const SymbolPost& move : aut.delta[eps_cl_state]) {
                if (move.symbol == epsilon) continue;
                // TODO: this could be done more efficiently if we had a better add method
                for (State tgt_state : move.targets) {
                    result.delta.add(src_state, move.symbol, tgt_state);
                }
            }
        }
    }
    return result;
}

Nfa Mata::Nfa::fragile_revert(const Nfa& aut) {
    const size_t num_of_states{ aut.size() };

    Nfa result(num_of_states);

    result.initial = aut.final;
    result.final = aut.initial;

    //COMPUTE NON-e SYMBOLS
    //This stuff is ugly because of our handling of epsilon, what about negative numbers?
    OrdVector<Symbol> symbols = aut.get_used_symbols();
    if (symbols.empty())
        return result;
    if (symbols.back() == EPSILON)
        symbols.pop_back();
    // size of the "used alphabet", i.e. max symbol+1 or 0
    Symbol alphasize =  (symbols.empty()) ? 0 : (symbols.back()+1);

#ifdef _STATIC_STRUCTURES_
    //STATIC DATA STRUCTURES:
    // Not sure that it works ideally, whether the space for the inner vectors stays there.
    static std::vector<std::vector<State>> sources;
    static std::vector<std::vector<State>> targets;
    static std::vector<State> e_sources;
    static std::vector<State> e_targets;
    if (alphasize>sources.size()) {
        sources.resize(alphasize);
        targets.resize(alphasize);
    }

    e_sources.clear();
    e_targets.clear();

    //WHEN ONLY MAX SYMBOL IS COMPUTED
    // for (int i = 0;i<alphasize;i++) {
    //     for (int i = 0;i<alphasize;i++) {
    //         if (!sources[i].empty())
    //         {
    //             sources[i].resize(0);
    //             targets[i].resize(0);
    //         }
    //     }
    // }

    //WHEN ALL SYMBOLS ARE COMPUTED
    for (Symbol symbol: symbols) {
        if(!sources[symbol].empty()) {
            sources[symbol].clear();
            targets[symbol].clear();
        }
    }
#else
    // NORMAL, NON STATIC DATA STRUCTURES:
    //All transition of delta are to be copied here, into two arrays of transition sources and targets indexed by the transition symbol.
    // There is a special treatment for epsilon, since we want the arrays to be only as long as the largest symbol in the automaton,
    // and epsilon is the maximum (so we don't want to have the maximum array lenght whenever epsilon is present)
    std::vector<std::vector<State>> sources (alphasize);
    std::vector<std::vector<State>> targets (alphasize);
    std::vector<State> e_sources;
    std::vector<State> e_targets;
#endif

    //Copy all transition with non-e symbols to the arrays of sources and targets indexed by symbols.
    //Targets and sources of e-transitions go to the special place.
    //Important: since we are going through delta in order of sources, the sources arrays are all ordered.
    for (State sourceState{ 0 }; sourceState < num_of_states; ++sourceState) {
        for (const SymbolPost &move: aut.delta[sourceState]) {
            if (move.symbol == EPSILON) {
                for (const State targetState: move.targets) {
                    //reserve_on_insert(e_sources);
                    e_sources.push_back(sourceState);
                    //reserve_on_insert(e_targets);
                    e_targets.push_back(targetState);
                }
            }
            else {
                for (const State targetState: move.targets) {
                    //reserve_on_insert(sources[move.symbol]);
                    sources[move.symbol].push_back(sourceState);
                    //reserve_on_insert(targets[move.symbol]);
                    targets[move.symbol].push_back(targetState);
                }
            }
        }
    }

    //Now make the delta of the reversed automaton.
    //Important: since sources are ordered, when adding them as targets, we can just push them back.
    result.delta.reserve(num_of_states);

    // adding non-e transitions
    for (const Symbol symbol: symbols) {
        for (size_t i{ 0 }; i < sources[symbol].size(); ++i) {
            State tgt_state =sources[symbol][i];
            State src_state =targets[symbol][i];
            StatePost & src_post = result.delta.mutable_state_post(src_state);
            if (src_post.empty() || src_post.back().symbol != symbol) {
                src_post.push_back(SymbolPost(symbol));
            }
            src_post.back().push_back(tgt_state);
        }
    }

    // adding e-transitions
    for (size_t i{ 0 }; i < e_sources.size(); ++i) {
        State tgt_state =e_sources[i];
        State src_state =e_targets[i];
        StatePost & src_post = result.delta.mutable_state_post(src_state);
        if (src_post.empty() || src_post.back().symbol != EPSILON) {
            src_post.push_back(SymbolPost(EPSILON));
        }
        src_post.back().push_back(tgt_state);
    }

    //sorting the targets
    //Hm I don't know why I put this here, but it should not be needed ...
    //for (State q = 0, states_num = result.delta.post_size(); q<states_num;++q) {
    //    for (auto m = result.delta.get_mutable_post(q).begin(); m != result.delta.get_mutable_post(q).end(); ++m) {
    //        sort_and_rmdupl(m->targets);
    //    }
    //}

    return result;
}

Nfa Mata::Nfa::simple_revert(const Nfa& aut) {
    Nfa result;
    result.clear();

    const size_t num_of_states{ aut.size() };
    result.delta.increase_size(num_of_states);

    for (State sourceState{ 0 }; sourceState < num_of_states; ++sourceState) {
        for (const SymbolPost &transition: aut.delta[sourceState]) {
            for (const State targetState: transition.targets) {
                result.delta.add(targetState, transition.symbol, sourceState);
            }
        }
    }

    result.initial = aut.final;
    result.final = aut.initial;

    return result;
}

//not so great, can be removed
Nfa Mata::Nfa::somewhat_simple_revert(const Nfa& aut) {
    const size_t num_of_states{ aut.size() };

    Nfa result(num_of_states);

    result.initial = aut.final;
    result.final = aut.initial;

    for (State sourceState{ 0 }; sourceState < num_of_states; ++sourceState) {
        for (const SymbolPost &transition: aut.delta[sourceState]) {
            for (const State targetState: transition.targets) {
                StatePost & post = result.delta.mutable_state_post(targetState);
                //auto move = std::find(post.begin(),post.end(),Move(transition.symbol));
                auto move = post.find(SymbolPost(transition.symbol));
                if (move == post.end()) {
                    //post.push_back(Move(transition.symbol,sourceState));
                    post.insert(SymbolPost(transition.symbol, sourceState));
                }
                else
                    move->push_back(sourceState);
                    //move->insert(sourceState);
            }
        }
    }

    //sorting the targets
    for (State q = 0, states_num = result.delta.num_of_states(); q < states_num; ++q) {
        //Post & post = result.delta.get_mutable_post(q);
        //Util::sort_and_rmdupl(post);
        for (auto m = result.delta.mutable_state_post(q).begin(); m != result.delta.mutable_state_post(q).end(); ++m) {
            sort_and_rmdupl(m->targets);
        }
    }

    return result;
}

Nfa Mata::Nfa::revert(const Nfa& aut) {
    return simple_revert(aut);
    //return fragile_revert(aut);
    //return somewhat_simple_revert(aut);
}

bool Mata::Nfa::is_deterministic(const Nfa& aut)
{
    if (aut.initial.size() != 1) { return false; }

    if (aut.delta.empty()) { return true; }

    const size_t aut_size = aut.size();
    for (size_t i = 0; i < aut_size; ++i)
    {
        for (const auto& symStates : aut.delta[i])
        {
            if (symStates.size() != 1) { return false; }
        }
    }

    return true;
}
bool Mata::Nfa::is_complete(const Nfa& aut, const Alphabet& alphabet)
{
    Util::OrdVector<Symbol> symbs_ls = alphabet.get_alphabet_symbols();
    Util::OrdVector<Symbol> symbs(symbs_ls);

    // TODO: make a general function for traversal over reachable states that can
    // be shared by other functions?
    std::list<State> worklist(aut.initial.begin(),
                              aut.initial.end());
    std::unordered_set<State> processed(aut.initial.begin(),
                                        aut.initial.end());

    while (!worklist.empty())
    {
        State state = *worklist.begin();
        worklist.pop_front();

        size_t n = 0;      // counter of symbols
        if (!aut.delta.empty()) {
            for (const auto &symb_stateset: aut.delta[state]) {
                ++n;
                if (!haskey(symbs, symb_stateset.symbol)) {
                    throw std::runtime_error(std::to_string(__func__) +
                                             ": encountered a symbol that is not in the provided alphabet");
                }

                for (const auto &tgt_state: symb_stateset.targets) {
                    bool inserted;
                    tie(std::ignore, inserted) = processed.insert(tgt_state);
                    if (inserted) { worklist.push_back(tgt_state); }
                }
            }
        }

        if (symbs.size() != n) { return false; }
    }

    return true;
}

std::pair<Run, bool> Mata::Nfa::get_word_for_path(const Nfa& aut, const Run& run)
{
    if (run.path.empty())
    {
        return {{}, true};
    }

    Run word;
    State cur = run.path[0];
    for (size_t i = 1; i < run.path.size(); ++i)
    {
        State newSt = run.path[i];
        bool found = false;

        if (!aut.delta.empty())
        {
            for (const auto &symbolMap: aut.delta[cur]) {
                for (State st: symbolMap.targets) {
                    if (st == newSt) {
                        word.word.push_back(symbolMap.symbol);
                        found = true;
                        break;
                    }
                }

                if (found) { break; }
            }
        }

        if (!found)
        {
            return {{}, false};
        }

        cur = newSt;    // update current state
    }

    return {word, true};
}

//TODO: this is not efficient
bool Mata::Nfa::is_in_lang(const Nfa& aut, const Run& run)
{
    StateSet cur(aut.initial);

    for (Symbol sym : run.word)
    {
        cur = aut.post(cur, sym);
        if (cur.empty()) { return false; }
    }

    return aut.final.intersects_with(cur);
}

/// Checks whether the prefix of a string is in the language of an automaton
// TODO: slow and it should share code with is_in_lang
bool Mata::Nfa::is_prfx_in_lang(const Nfa& aut, const Run& run)
{
    StateSet cur =  StateSet{ aut.initial };

    for (Symbol sym : run.word)
    {
        if (aut.final.intersects_with(cur)) { return true; }
        cur = aut.post(cur, sym);
        if (cur.empty()) { return false; }
    }

    return aut.final.intersects_with(cur);
}

bool Mata::Nfa::is_lang_empty(const Nfa& aut, Run* cex)
{ // {{{
    std::list<State> worklist(
            aut.initial.begin(), aut.initial.end());
    std::unordered_set<State> processed(
            aut.initial.begin(), aut.initial.end());

    // 'paths[s] == t' denotes that state 's' was accessed from state 't',
    // 'paths[s] == s' means that 's' is an initial state
    std::map<State, State> paths;
    for (State s : worklist)
    {	// initialize
        paths[s] = s;
    }

    while (!worklist.empty())
    {
        State state = worklist.front();
        worklist.pop_front();

        if (aut.final[state])
        {
            // TODO process the CEX
            if (nullptr != cex)
            {
                cex->path.clear();
                cex->path.push_back(state);
                while (paths[state] != state)
                {
                    state = paths[state];
                    cex->path.push_back(state);
                }

                std::reverse(cex->path.begin(), cex->path.end());
                cex->word = get_word_for_path(aut, *cex).first.word;
            }
            return false;
        }

        if (aut.delta.empty())
            continue;

        for (const auto& symb_stateset : aut.delta[state])
        {
            for (const auto& tgt_state : symb_stateset.targets)
            {
                bool inserted;
                tie(std::ignore, inserted) = processed.insert(tgt_state);
                if (inserted)
                {
                    worklist.push_back(tgt_state);
                    // also set that tgt_state was accessed from state
                    paths[tgt_state] = state;
                }
                else
                {
                    // the invariant
                    assert(haskey(paths, tgt_state));
                }
            }
        }
    }

    return true;
} // is_lang_empty }}}


Nfa Mata::Nfa::Algorithms::minimize_brzozowski(const Nfa& aut) {
    //compute the minimal deterministic automaton, Brzozovski algorithm
    return determinize(revert(determinize(revert(aut))));
}

Nfa Mata::Nfa::minimize(
                const Nfa& aut,
                const ParameterMap& params)
{
    Nfa result;
    // setting the default algorithm
    decltype(Algorithms::minimize_brzozowski)* algo = Algorithms::minimize_brzozowski;
    if (!haskey(params, "algorithm")) {
        throw std::runtime_error(std::to_string(__func__) +
            " requires setting the \"algo\" key in the \"params\" argument; "
            "received: " + std::to_string(params));
    }

    const std::string& str_algo = params.at("algorithm");
    if ("brzozowski" == str_algo) {  /* default */ }
    else {
        throw std::runtime_error(std::to_string(__func__) +
            " received an unknown value of the \"algo\" key: " + str_algo);
    }

    return algo(aut);
}

Nfa Mata::Nfa::uni(const Nfa &lhs, const Nfa &rhs) {
    Nfa union_nfa{ rhs };

    StateRenaming lhs_state_renaming;
    const size_t size = lhs.size();
    for (State lhs_state = 0; lhs_state < size; ++lhs_state) {
        lhs_state_renaming[lhs_state] = union_nfa.add_state();
    }

    for (State lhs_initial_state : lhs.initial) {
        union_nfa.initial.insert(lhs_state_renaming[lhs_initial_state]);
    }

    for (State lhs_final_state : lhs.final) {
        union_nfa.final.insert(lhs_state_renaming[lhs_final_state]);
    }

    for (State lhs_state = 0; lhs_state < size; ++lhs_state) {
        State union_state = lhs_state_renaming[lhs_state];
        for (const SymbolPost &lhs_symbol_post : lhs.delta[lhs_state]) {

            SymbolPost union_symbol_post{ lhs_symbol_post.symbol, StateSet{} };

            for (State target_state : lhs_symbol_post.targets) {
                union_symbol_post.insert(lhs_state_renaming[target_state]);
            }

            union_nfa.delta.mutable_state_post(union_state).insert(union_symbol_post);
        }
    }

    return union_nfa;
}

Simlib::Util::BinaryRelation Mata::Nfa::Algorithms::compute_relation(const Nfa& aut, const ParameterMap& params) {
    if (!haskey(params, "relation")) {
        throw std::runtime_error(std::to_string(__func__) +
                                 " requires setting the \"relation\" key in the \"params\" argument; "
                                 "received: " + std::to_string(params));
    }
    if (!haskey(params, "direction")) {
        throw std::runtime_error(std::to_string(__func__) +
                                 " requires setting the \"direction\" key in the \"params\" argument; "
                                 "received: " + std::to_string(params));
    }

    const std::string& relation = params.at("relation");
    const std::string& direction = params.at("direction");
    if ("simulation" == relation && direction == "forward") {
        return compute_fw_direct_simulation(aut);
    }
    else {
        throw std::runtime_error(std::to_string(__func__) +
                                 " received an unknown value of the \"relation\" key: " + relation);
    }
}

Nfa Mata::Nfa::reduce(const Nfa &aut, bool trim_input, StateRenaming *state_renaming, const ParameterMap& params) {
    if (!haskey(params, "algorithm")) {
        throw std::runtime_error(std::to_string(__func__) +
                                 " requires setting the \"algorithm\" key in the \"params\" argument; "
                                 "received: " + std::to_string(params));
    }

    Nfa aut_to_reduce{ aut };
    StateRenaming trimmed_state_renaming{};
    if (trim_input) {
        aut_to_reduce.trim(&trimmed_state_renaming);
    }

    Nfa result;
    std::unordered_map<State,State> reduced_state_map;
    const std::string& algorithm = params.at("algorithm");
    if ("simulation" == algorithm) {
        result = reduce_size_by_simulation(aut_to_reduce, reduced_state_map);
    } else {
        throw std::runtime_error(std::to_string(__func__) +
                                 " received an unknown value of the \"algorithm\" key: " + algorithm);
    }

    if (state_renaming) {
        state_renaming->clear();
        if (trim_input) {
            for (const auto& trimmed_mapping : trimmed_state_renaming) {
                const auto reduced_mapping{ reduced_state_map.find(trimmed_mapping.second) };
                if (reduced_mapping != reduced_state_map.end()) {
                    (*state_renaming)[trimmed_mapping.first] = reduced_mapping->second;
                }
            }
        } else { // Input has not been trimmed, the reduced state map is the actual input to result state map.
            *state_renaming = reduced_state_map;
        }
    }

    return result;
}

Nfa Mata::Nfa::determinize(
        const Nfa&  aut,
        std::unordered_map<StateSet, State> *subset_map) {

    Nfa result;
    //assuming all sets targets are non-empty
    std::vector<std::pair<State, StateSet>> worklist;
    bool deallocate_subset_map = false;
    if (subset_map == nullptr) {
        subset_map = new std::unordered_map<StateSet,State>();
        deallocate_subset_map = true;
    }

    result.clear();

    const StateSet S0 =  StateSet(aut.initial);
    const State S0id = result.add_state();
    result.initial.insert(S0id);

    if (aut.final.intersects_with(S0)) {
        result.final.insert(S0id);
    }
    worklist.emplace_back(std::make_pair(S0id, S0));

    (*subset_map)[Mata::Util::OrdVector<State>(S0)] = S0id;

    if (aut.delta.empty())
        return result;

    using Iterator = Mata::Util::OrdVector<SymbolPost>::const_iterator;
    Mata::Util::SynchronizedExistentialIterator<Iterator> synchronized_iterator;

    while (!worklist.empty()) {
        const auto Spair = worklist.back();
        worklist.pop_back();
        const StateSet S = Spair.second;
        const State Sid = Spair.first;
        if (S.empty()) {
            // This should not happen assuming all sets targets are non-empty.
            break;
        }

        // add moves of S to the sync ex iterator
        // TODO: shouldn't we also reset first?
        for (State q: S) {
            Mata::Util::push_back(synchronized_iterator, aut.delta[q]);
        }

        while (synchronized_iterator.advance()) {

            // extract post from the sychronized_iterator iterator
            std::vector<Iterator> moves = synchronized_iterator.get_current();
            Symbol currentSymbol = (*moves.begin())->symbol;
            StateSet T;
            for (auto m: moves){
                T = T.Union(m->targets);
            }

            const auto existingTitr = subset_map->find(T);
            State Tid;
            if (existingTitr != subset_map->end()) {
                Tid = existingTitr->second;
            } else {
                Tid = result.add_state();
                (*subset_map)[Mata::Util::OrdVector<State>(T)] = Tid;
                if (aut.final.intersects_with(T)) {
                    result.final.insert(Tid);
                }
                worklist.emplace_back(std::make_pair(Tid, T));
            }
            result.delta.mutable_state_post(Sid).insert(SymbolPost(currentSymbol, Tid));
        }
    }

    if (deallocate_subset_map) { delete subset_map; }

    return result;
}

std::ostream& std::operator<<(std::ostream& os, const Mata::Nfa::Nfa& nfa) {
    nfa.print_to_mata(os);
    return os;
}

void Mata::Nfa::fill_alphabet(const Mata::Nfa::Nfa& nfa, OnTheFlyAlphabet& alphabet) {
    for (const StatePost& state_post: nfa.delta) {
        for (const SymbolPost& symbol_post: state_post) {
            alphabet.update_next_symbol_value(symbol_post.symbol);
            alphabet.try_add_new_symbol(std::to_string(symbol_post.symbol), symbol_post.symbol);
        }
    }
}

Mata::OnTheFlyAlphabet Mata::Nfa::create_alphabet(const std::vector<std::reference_wrapper<const Nfa>>& nfas) {
    Mata::OnTheFlyAlphabet alphabet{};
    for (const auto& nfa: nfas) {
        fill_alphabet(nfa, alphabet);
    }
    return alphabet;
}

Mata::OnTheFlyAlphabet Mata::Nfa::create_alphabet(const std::vector<std::reference_wrapper<Nfa>>& nfas) {
    Mata::OnTheFlyAlphabet alphabet{};
    for (const auto& nfa: nfas) {
        fill_alphabet(nfa, alphabet);
    }
    return alphabet;
}

Mata::OnTheFlyAlphabet Mata::Nfa::create_alphabet(const std::vector<const Nfa *>& nfas) {
    Mata::OnTheFlyAlphabet alphabet{};
    for (const Mata::Nfa::Nfa* const nfa: nfas) {
        fill_alphabet(*nfa, alphabet);
    }
    return alphabet;
}

Mata::OnTheFlyAlphabet Mata::Nfa::create_alphabet(const std::vector<Nfa*>& nfas) {
    Mata::OnTheFlyAlphabet alphabet{};
    for (const Mata::Nfa::Nfa* const nfa: nfas) {
        fill_alphabet(*nfa, alphabet);
    }
    return alphabet;
}

Run Mata::Nfa::encode_word(const Alphabet* alphabet, const std::vector<std::string>& input) {
    return { .word = alphabet->translate_word(input) };
}
