from dataclasses import dataclass
from typing import List

@dataclass
class Project:
    id: int
    name: str
    repo_url: str
