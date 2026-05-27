from fastapi import FastAPI
import logging

from .logging_config import  setup_logging
from .routes import airports

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(airports.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
