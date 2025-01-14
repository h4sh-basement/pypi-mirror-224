# copyright 2022-2023 LOGILAB S.A. (Paris, FRANCE), all rights reserved.
# contact https://www.logilab.fr -- mailto:contact@logilab.fr
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
from cubicweb_api.constants import API_PATH_DEFAULT_PREFIX

options = (
    (
        "api-path-prefix",
        {
            "type": "string",
            "default": API_PATH_DEFAULT_PREFIX,
            "help": "prefix used for the url path. "
            "The api version number will be added after this prefix (only v1 for now).",
            "group": "api",
            "level": 2,
        },
    ),
)
