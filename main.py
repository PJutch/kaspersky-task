from fastapi import FastAPI, File, UploadFile
from count_words import count_words

app = FastAPI()

@app.post("/public/report/export")
async def test(file: UploadFile = File(...)):
    binary = await file.read()
    text = binary.decode('utf-8')
    return count_words(text)
