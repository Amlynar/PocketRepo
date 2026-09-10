from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class Source:
    type: str
    url: str

@dataclass
class Project:
    id: str
    name: str
    description: str
    source: Source
    destination: str
    options: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Project":
        source_data = data.get("source", {})
        source = Source(
            type=source_data.get("type", "github_zip"),
            url=source_data.get("url", "")
        )
        return cls(
            id=str(data.get("id")),
            name=data.get("name", ""),
            description=data.get("description", ""),
            source=source,
            destination=data.get("destination", ""),
            options=data.get("options", {})
        )
