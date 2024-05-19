import random
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This is roll-a-dice Microservier."}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/rolldice")
async def roll_dice():
    dice_val = random.randint(1, 6)
    return {"dice_val": dice_val}
