from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()
UPLOAD_DIR = "files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    return {"status": "success", "filename": file.filename}
