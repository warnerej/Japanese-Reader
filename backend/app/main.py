from fastapi import FastAPI
from routers import vocab_router, user_router

app = FastAPI(title="Supabase FastAPI App")

app.include_router(vocab_router)
app.include_router(user_router)
