from typing import List

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

    @staticmethod
    def get_vocab_by_list(client: Client, word_list: List[str]):
        # Using a for loop becuase words may or may not have kanji
        found_words = []
        for word in word_list:
            response = client.table("vocab").select("*").eq("kanji", word).execute()
            if response.data:
                found_words.append(response[0])
            else:
                response = (
                    client.table("vocab")
                    .select("*")
                    .eq("reading", word)
                    .is_("kanji", "null")
                    .execute()
                )
                found_words.append(response[0])

                if not response.data:
                    pass
        return found_words
