#
# Copyright 2017-2023 - Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
r"""Free up disk space by removing temporary files and caches in a Renku project.

.. cheatsheet::
   :group: Misc
   :command: $ renku gc
   :description: Free up disk space used for caches and temporary files.
   :target: rp
"""

import click


@click.command()
def gc():
    """Cache and temporary files cleanup."""
    from renku.command.gc import gc_command

    gc_command().build().execute()
