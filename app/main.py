from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re

app = FastAPI()


class Payload(BaseModel):
    text: str


romanNumbersDict = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1,
}


def romanToInteger(romanNumber: str) -> int:
    number = 0
    for i, x in enumerate(romanNumber):
        if i == len(romanNumber) - 1:
            number += romanNumbersDict[x]
            break
        elif romanNumbersDict[x] < romanNumbersDict[romanNumber[i + 1]]:
            number -= romanNumbersDict[x]
        else:
            number += romanNumbersDict[x]
    return number


@app.post("/search")
def max_roman_number(payload: Payload) -> Union[str, dict]:
    """
    Give you the max roman Number:

    - **text**: one or more roman numbers divided by letter index. Example: "AXXBXXX"
    """
    if payload.text[0] in romanNumbersDict:
        raise HTTPException(
            status_code=400,
            detail="the payload don't start with a index like 'A', 'B', 'E' etc. it start with a roman number",
        )

    # separate roman numbers in a python list
    romanList = re.findall(r"[MDCLXVI]+", payload.text)

    numbersList = [romanToInteger(romanNumber) for romanNumber in romanList]

    # create a list of tuples of numberList and romanList values
    # and extract its max value based on numbersList value
    responseValues = max(zip(numbersList, romanList), key=lambda x: x[0])
    return {"number": responseValues[1], "value": responseValues[0]}
