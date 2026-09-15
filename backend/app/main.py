from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import get_supabase
from supabase import Client

app = FastAPI(title="FastAPI + Supabase API")

class vocab(BaseModel):
    id: int
    kanji: str
    reading: str
    definition: str
    raw_jason: str

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Supabase!"}

# 1. Get all todos
@app.get("/vocab")
def get_vocab(db: Client = Depends(get_supabase)):
    response = db.table("vocab").select("*").limit(10).execute()
    return response.data