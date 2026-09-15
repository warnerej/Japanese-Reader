from fastapi import APIRouter
from typing import List
from models import VocabResponse
from services import VocabService

router = APIRouter(prefix="/vocab", tags=["Vocab"])


@router.get("/", response_model=List[VocabResponse])
def get_vocab():
  return VocabService.get_vocab()

@router.get("/{id}", response_model=List[VocabResponse])
def get_vocab_by_id(id: int):
  return VocabService.get_vocab_by_id(id)