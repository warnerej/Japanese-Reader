from supabase import Client


class VocabService:
    @staticmethod
    def get_vocab(client: Client):
        response = client.table("vocab").select("*").limit(10).execute()
        return response.data

    @staticmethod
    def get_vocab_by_id(client: Client, id: int):
        response = client.table("vocab").select("*").eq("id", id).limit(10).execute()
        return response.data

    @staticmethod
    def get_vocab_by_word(client: Client, word: str):
        response = client.table("vocab").select("*").eq("kanji", word).execute()
        if response.data:
            return response.data
        else:
            response = (
                client.table("vocab")
                .select("*")
                .eq("reading", word)
                .is_("kanji", "null")
                .execute()
            )
            return response.data
