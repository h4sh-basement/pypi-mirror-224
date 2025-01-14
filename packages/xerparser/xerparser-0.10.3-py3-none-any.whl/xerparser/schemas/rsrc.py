# xerparser
# rsrc.py

from typing import Any
from xerparser.schemas.udftype import UDFTYPE


class RSRC:
    """
    A class to represent a Resource.
    """

    def __init__(self, **data) -> None:
        self.uid: str = data["rsrc_id"]
        self.clndr_id: str = data["clndr_id"]
        self.name: str = data["rsrc_name"]
        self.short_name: str = data["rsrc_short_name"]
        self.type: str = data["rsrc_type"]
        self.user_defined_fields: dict[UDFTYPE, Any] = {}

    def __eq__(self, __o: "RSRC") -> bool:
        return all(
            (
                self.name == __o.name,
                self.short_name == __o.short_name,
                self.type == __o.type,
            )
        )

    def __hash__(self) -> int:
        return hash((self.name, self.short_name, self.type))
