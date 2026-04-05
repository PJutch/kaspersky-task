from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from count_words import count_words
from presentation import word_counts_to_xlsx
import io

app = FastAPI()

@app.post("/public/report/export")
async def test(file: UploadFile = File(...)):
    binary = await file.read()
    text = binary.decode('utf-8')

    word_counts =  count_words(text)

    return StreamingResponse(
        io.BytesIO(word_counts_to_xlsx(word_counts)),
        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        headers={"Content-Disposition": "attachment; filename=async_export.xlsx"} )
