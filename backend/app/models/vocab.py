from pydantic import BaseModel

class VocabResponse(BaseModel):
    id: int
    kanji: str
    reading: str
    definition: str
    raw_jason: str