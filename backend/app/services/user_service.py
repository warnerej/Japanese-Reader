from supabase import Client
from services import VocabService
from models import UserVocabCreate
from uuid import UUID


class UserService:
    @staticmethod
    def get_user_vocab(client: Client):
        response = client.table("user_vocab").select("*").limit(10).execute()
        return response.data

    @staticmethod
    def add_user_vocab_by_word(session, word: str):
        client = session[0]

        # User my other method to fetch the vocab_id
        vocab_to_add = VocabService.get_vocab_by_word(client, word)
        vocab_id = vocab_to_add[0]["id"]
        print(vocab_id)

        payload = UserVocabCreate(user_id=session[1], vocab_id=vocab_id)

        response = (
            client.table("user_vocab").insert(payload.model_dump(mode="json")).execute()
        )
