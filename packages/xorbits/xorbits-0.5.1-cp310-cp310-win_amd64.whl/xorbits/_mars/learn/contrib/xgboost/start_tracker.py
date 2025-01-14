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

from threading import Thread

from .... import opcodes as OperandDef
from ....core import NotSupportTile
from ....serialization.serializables import Int32Field
from ....utils import to_binary
from ...operands import LearnOperand, LearnOperandMixin, OutputType


class StartTracker(LearnOperand, LearnOperandMixin):
    _op_type_ = OperandDef.START_TRACKER
    _op_module_ = "learn.contrib.xgboost"

    n_workers = Int32Field("n_workers", default=None)

    def __init__(self, output_types=None, pure_depends=None, **kw):
        super().__init__(
            _output_types=output_types,
            _pure_depends=pure_depends,
            **kw,
        )
        if self.output_types is None:
            self.output_types = [OutputType.object]

    @classmethod
    def tile(cls, op):
        raise NotSupportTile("StartTracker is a chunk op")

    @classmethod
    def execute(cls, ctx, op):
        """Start Rabit tracker"""
        from .tracker import RabitTracker

        env = {"DMLC_NUM_WORKER": op.n_workers}
        rabit_context = RabitTracker(
            host_ip=ctx.get_local_host_ip(), n_workers=op.n_workers
        )
        env.update(rabit_context.worker_envs())

        rabit_context.start(op.n_workers)
        thread = Thread(target=rabit_context.join)
        thread.daemon = True
        thread.start()

        rabit_args = [to_binary(f"{k}={v}") for k, v in env.items()]
        ctx[op.outputs[0].key] = rabit_args
