# services/user_service.py
from database import get_supabase

supabase = get_supabase()

class VocabService:
    @staticmethod
    def get_vocab():
        response = (supabase.table("vocab").select("*").limit(10).execute())
        return response.data

    @staticmethod
    def get_vocab_by_id(id: int):
        response = (supabase.table("vocab").select("*").eq("id", id).limit(10).execute())
        return response.data