from uuid import UUID
from pydantic import BaseModel


class UserVocabResponse(BaseModel):
    user_id: UUID
    vocab_id: int


class UserVocabCreate(UserVocabResponse):
    pass
