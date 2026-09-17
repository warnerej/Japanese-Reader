from fastapi import APIRouter, Depends
from typing import List

from supabase import Client
from models import UserVocabResponse
from services import UserService
from dependencies import get_user_supabase

router = APIRouter(prefix="/user-vocab", tags=["User Vocab"])

@router.get("/", response_model=List[UserVocabResponse])
def get_user_vocab(client: Client = Depends(get_user_supabase)):
    return UserService.get_user_vocab(client)