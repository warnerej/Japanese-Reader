from fastapi import APIRouter, Depends
from typing import List

from supabase import Client
from models import VocabResponse
from services import VocabService
from dependencies import get_user_supabase

router = APIRouter(prefix="/vocab", tags=["Vocab"])

@router.get("/", response_model=List[VocabResponse])
def get_vocab(client: Client = Depends(get_user_supabase)):
  return VocabService.get_vocab(client)

@router.get("/id/{id}", response_model=List[VocabResponse])
def get_vocab_by_id(id: int, client: Client = Depends(get_user_supabase)):
  return VocabService.get_vocab_by_id(client, id)

@router.get("/word/{word}", response_model=List[VocabResponse])
def get_vocab_by_word(word: str, client: Client = Depends(get_user_supabase)):
  return VocabService.get_vocab_by_word(client, word)