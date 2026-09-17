from supabase import Client

class UserService:
    @staticmethod
    def get_user_vocab(client: Client):
        response = client.table("user_vocab").select("*").limit(10).execute()
        return response.data

