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

from .cholesky import TensorCholesky, cholesky
from .dot import TensorDot, dot
from .inner import inner, innerproduct
from .inv import TensorInv, inv
from .lu import TensorLU, lu
from .matmul import TensorMatmul, matmul
from .norm import TensorNorm, norm
from .qr import TensorQR, qr
from .randomized_svd import randomized_svd
from .solve import solve
from .solve_triangular import TensorSolveTriangular, solve_triangular
from .svd import TensorSVD, svd
from .tensordot import TensorTensorDot, tensordot
from .vdot import vdot


def _install():
    from ..core import Tensor, TensorData

    setattr(Tensor, "__matmul__", matmul)
    setattr(Tensor, "dot", dot)
    setattr(TensorData, "__matmul__", matmul)
    setattr(TensorData, "dot", dot)


_install()
del _install
