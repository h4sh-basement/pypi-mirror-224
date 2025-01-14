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

from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractLifecycleAPI(ABC):
    @abstractmethod
    async def decref_tileables(
        self, tileable_keys: List[str], counts: List[int] = None
    ):
        """
        Decref tileables.

        Parameters
        ----------
        tileable_keys : list
            List of tileable keys.
        counts: list
            List of ref count.
        """

    @abstractmethod
    async def get_all_chunk_ref_counts(self) -> Dict[str, int]:
        """
        Get all chunk keys' ref counts.

        Returns
        -------
        key_to_ref_counts: dict
        """
