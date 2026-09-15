# services/user_service.py
from database import get_supabase
from models import VocabResponse

supabase = get_supabase()

class VocabService:
    @staticmethod
    def get_vocab():
            response = (supabase.table("vocab").select("*").limit(10).execute())
            return response.data