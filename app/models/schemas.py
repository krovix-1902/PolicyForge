from dataclasses import dataclass
from typing import Optional


@dataclass
class PolicyRule:
    rule_id: str
    title: str
    actor: str
    action: str
    object: str
    condition: Optional[str] = None
    exception: Optional[str] = None
    owner: Optional[str] = None