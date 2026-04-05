from fastapi import FastAPI
from count_words.controller import router

app = FastAPI()

app.include_router(router)
