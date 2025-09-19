from fastapi import FastAPI, UploadFile, File
import os
import uvicorn
from .config import settings
from pathlib import Path

app = FastAPI()
UPLOAD_DIR = "files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    return {"status": "success", "filename": file.filename}

@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = UPLOAD_DIR / filename
    if file_path.exists():
        return FileResponse(path=file_path, filename=filename, media_type="application/octet-stream")
    return {"error": "File not found"}

@app.on_event("startup")
async def startup_event():
    print(f"Server starting on {settings.HOST}:{settings.PORT}")

@app.get("/")
async def root():
    return {"message": "Hello, Widgets!"}

#if __name__ == "__main__":
#    uvicorn.run("server.server:app", host=settings.HOST, port=settings.PORT, reload=True)