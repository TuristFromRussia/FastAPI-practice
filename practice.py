import datetime
from typing import List
from loguru import logger
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel

class MembersGet(BaseModel):
    id: int
    surname: str
    firstname: str
    address: str
    zipcode: int
    telephone: str
    recommendedby: int | None
    joindate: datetime.datetime

    model_config = {
        "from_attributes": True 
    }


app = FastAPI()

@app.get("/")
def say_hui():
    return 'huilo'

@app.get("/minus")
def minus_two(a: int, b: int) -> int:
    return a - b

@app.get("/fuck/{print}")
def paint(print: str):
    ret = ''
    ret = print.upper()
    return ret

@app.post("/user")
def user(name):
    return {"message": f"hello, {name}"}


@app.get("/members/all", response_model=List[MembersGet])
def all_members():
    conn = psycopg2.connect("postgresql://postgres:valdorf2015@localhost:5432/exercises?client_encoding=WIN1252", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT memid AS id,
        surname,
        firstname, 
        address,
        zipcode, 
        telephone, 
        recommendedby, 
        joindate
    FROM cd.members
    """)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results







# python -m uvicorn practice:app --reload
# запуск локального сервера