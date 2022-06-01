from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()


class Payload(BaseModel):
    text: str
    def __list__(self):
        return self.text.split()

romanNumbersDict = {
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

def romanToInteger(romanNumber: str) -> int:
    # convert romanNumber into integer
    number = 0
    if len(romanNumber) == 1:
        number = romanNumbersDict[romanNumber]
    else:
        for i in range(1, len(romanNumber)+1):
            if romanNumbersDict[romanNumber[i]] > romanNumbersDict[romanNumber[i-1]]:
                number += romanNumbersDict[romanNumber[i-1:i+1]]
            else:
                number += romanNumbersDict[romanNumber[i-1]]
    return number

@app.get("/search")
def welcome():
    return 'Welcome'

@app.post("/search")
def max_roman_number(input: Payload = None) -> Union[str, dict]:    
    if input.text[0] in romanNumbersDict:
        raise Exception("there is no index")
    
    # separate roman numbers in a python list
    romanList = re.findall(r"[MDCLXVI]+", input.text)

    numbersList = [romanToInteger(romanNumber) for romanNumber in romanList]
    
    responseValues = max(zip(numbersList, romanList), key=lambda x: x[0])
    return {"number": responseValues[1], "value": responseValues[0]}