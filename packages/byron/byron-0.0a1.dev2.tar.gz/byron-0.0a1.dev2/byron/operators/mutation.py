# -*- coding: utf-8 -*-
#############################################################################
#   __                          (`/\                                        #
#  |  |--.--.--.----.-----.-----`=\/\   This file is part of byron v0.1     #
#  |  _  |  |  |   _|  _  |     |`=\/\  An evolutionary optimizer & fuzzer  #
#  |_____|___  |__| |_____|__|__| `=\/  https://github.com/squillero/byron  #
#        |_____|                     \                                      #
#############################################################################
# Copyright 2022-2023 Giovanni Squillero and Alberto Tonda
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.

#############################################################################
# HISTORY
# v1 / June 2023 / Squillero (GX)

from byron.global_symbols import *
from byron.operators.unroll import *
from byron.user_messages import *
from byron.classes import *
from byron.registry import *
from byron.functions import *
from byron.randy import rrandom
from byron.tools.graph import *

from networkx import dfs_preorder_nodes


@genetic_operator(num_parents=1)
def single_parameter_mutation(parent: Individual, strength=1.0) -> list["Individual"]:
    offspring = parent.clone
    param = rrandom.choice(offspring.parameters)
    mutate(param, strength=strength)
    return [offspring]


@genetic_operator(num_parents=1)
def add_macro_to_bunch(parent: Individual, strength=1.0) -> list["Individual"]:
    offspring = parent.clone
    G = offspring.genome
    candidates = [
        n
        for n in offspring.genome
        if isinstance(G.nodes[n]["_selement"], FrameMacroBunch)
        and G.out_degree[n] < G.nodes[n]["_selement"].SIZE[1] - 1
    ]
    if not candidates:
        raise GeneticOperatorFail
    node = rrandom.choice(candidates)
    successors = get_successors(NodeReference(G, node))
    new_macro_type = rrandom.choice(G.nodes[node]["_selement"].POOL)
    new_macro_reference = unroll_selement(new_macro_type, G)
    G.add_edge(node, new_macro_reference.node, _type=FRAMEWORK)
    initialize_subtree(new_macro_reference)
    i = rrandom.randint(0, len(successors))
    set_successors_order(NodeReference(G, node), successors[:i] + [new_macro_reference.node] + successors[i:])
    return [offspring]


@genetic_operator(num_parents=1)
def remove_macro_from_bunch(parent: Individual, strength=1.0) -> list["Individual"]:
    offspring = parent.clone
    G = offspring.genome
    frame_candidates = [
        n
        for n in offspring.genome
        if isinstance(G.nodes[n]["_selement"], FrameMacroBunch) and G.out_degree[n] > G.nodes[n]["_selement"].SIZE[0]
    ]
    if not frame_candidates:
        raise GeneticOperatorFail
    frame_node = rrandom.choice(frame_candidates)
    candidates = [
        n
        for n in dfs_preorder_nodes(G, frame_node)
        if isinstance(G.nodes[n]["_selement"], Macro) and G.in_degree(n) == 1
    ]

    if not candidates:
        raise GeneticOperatorFail
    node = rrandom.choice(candidates)
    G.remove_node(node)
    return [offspring]
