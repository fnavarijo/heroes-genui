# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import logging
import os

logger = logging.getLogger(__name__)


def search_heroes(
    name: str = "",
    editorial: str = "",
    count: int = 5,
) -> str:
    """Call this tool to search for superheroes.

    'name' filters by a case-insensitive substring of the hero's name (pass an
    empty string to match any name). 'editorial' filters by publisher, e.g.
    'Marvel' or 'DC' (empty string matches any). 'count' is the maximum number
    of heroes to return.
    """
    logger.info(f"--- TOOL CALLED: search_heroes (count: {count}) ---")
    logger.info(f"  - Name: {name}")
    logger.info(f"  - Editorial: {editorial}")

    items = []
    try:
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "heroes_data.json")
        with open(file_path) as f:
            all_heroes = json.load(f)

        name_needle = name.strip().lower()
        editorial_needle = editorial.strip().lower()

        matches = [
            hero
            for hero in all_heroes
            if (not name_needle or name_needle in hero["name"].lower())
            and (not editorial_needle or editorial_needle == hero["editorial"].lower())
        ]

        # Slice the list to return only the requested number of items
        items = matches[:count]
        logger.info(
            f"  - Success: Matched {len(matches)} heroes, returning {len(items)}."
        )

    except FileNotFoundError:
        logger.error(f"  - Error: heroes_data.json not found at {file_path}")
    except json.JSONDecodeError:
        logger.error(f"  - Error: Failed to decode JSON from {file_path}")

    return json.dumps(items)
