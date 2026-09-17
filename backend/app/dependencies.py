from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from database import get_supabase_client
from supabase import Client

security = HTTPBearer()


def get_user_supabase(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> Client:
    client = get_supabase_client()
    token = credentials.credentials

    try:
        client.postgrest.auth(token)
        user_response = client.auth.get_user(token)
        user_id = user_response.user.id

        if not user_response or not user_response.user:
            raise HTTPException(status_code=401, detail="Invalid token")

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return client, user_id
