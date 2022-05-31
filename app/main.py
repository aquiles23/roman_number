from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class RomanNumber(BaseModel):
    text: str | None


@app.get("/search")
def max_roman_number(input: RomanNumber):
    
    return {"number": "LX", "value": 60}
