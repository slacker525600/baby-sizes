from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World!"}


@app.get("/{category}}/{week}")
def read_item(category: str, week: int):
    return {"category": category, "week": week}
