from fastapi import APIRouter, Depends
from typing import List

from supabase import Client
from models import UserVocabResponse
from services import UserService
from dependencies import get_user_supabase

router = APIRouter(prefix="/user-vocab", tags=["User Vocab"])


@router.get("/", response_model=List[UserVocabResponse])
def get_user_vocab(session=Depends(get_user_supabase)):
    return UserService.get_user_vocab(session[0])


@router.post("/vocab-word/{word}")
def add_user_vocab_by_word(word: str, session=Depends(get_user_supabase)):
    UserService.add_user_vocab_by_word(session, word)
