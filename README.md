# Тестовое задание

## Использование
```bash
pip install -r requirements.txt
# conda env create -f environment.yml

uvicorn main:app
curl http://127.0.0.1:8000/public/report/export -F "file=@<input filename>" --output <output filename>
```
