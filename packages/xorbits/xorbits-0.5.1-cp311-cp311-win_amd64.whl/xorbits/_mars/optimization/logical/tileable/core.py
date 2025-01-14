# Copyright 2022-2023 XProbe Inc.
# derived from copyright 1999-2021 Alibaba Group Holding Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List, Type

from ....core import OperandType, TileableGraph
from ..core import (
    OperandBasedOptimizationRule,
    OptimizationRecords,
    OptimizationRule,
    Optimizer,
)


class TileableOptimizer(Optimizer):
    """
    Tileable Optimizer
    """


def register_optimization_rule():
    def wrap(rule_type: Type[OptimizationRule]):
        TileableOptimizer.register_rule(rule_type)

    return wrap


def register_operand_based_optimization_rule(op_types: List[Type[OperandType]]):
    def wrap(rule_type: Type[OperandBasedOptimizationRule]):
        for op_type in op_types:
            rule_type.register_operand(op_type)
        TileableOptimizer.register_rule(rule_type)

    return wrap


def optimize(tileable_graph: TileableGraph) -> OptimizationRecords:
    return TileableOptimizer.optimize(tileable_graph)
