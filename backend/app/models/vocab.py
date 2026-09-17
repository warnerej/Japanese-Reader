from pydantic import BaseModel
from typing import Any, Dict, List


class VocabResponse(BaseModel):
    id: int
    kanji: str | None
    reading: str
    definition: str
    raw_json: Dict[str, Any]
