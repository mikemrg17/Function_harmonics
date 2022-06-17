from typing import Union
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from tsf import compute
from pydantic import BaseModel


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Signal(BaseModel):
    signal: str
    less: int
    greater: int
    harmonics: int

@app.get("/")
def read_root():
    return {"Status": "Active"}


@app.post("/compute")
def get_body(signal: Signal):
    return compute(signal)