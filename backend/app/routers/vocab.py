from fastapi import APIRouter
from models import VocabResponse
from services import VocabService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=VocabResponse)
def get_vocab():
  return VocabService.get_vocab()