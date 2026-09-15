from fastapi import FastAPI
from routers import vocab_router

app = FastAPI(title="Supabase FastAPI App")

app.include_router(vocab_router)