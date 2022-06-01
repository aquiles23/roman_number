from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()


class Payload(BaseModel):
    text: str
    def __list__(self):
        return self.text.split()

@app.get("/search")
def welcome():
    return 'welcome'

@app.post("/search")
def max_roman_number(input: Payload = None) -> Union[str, dict]:
    romanNumbers = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    if input.text[0] in romanNumbers:
        raise Exception('no index')
    number = 0
    # do a re.split


    return {"number": "LX", "value": 60}
