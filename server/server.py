from fastapi import FastAPI, UploadFile, File
import os
import uvicorn
from .config import settings

app = FastAPI()
UPLOAD_DIR = "files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(await file.read())
    return {"status": "success", "filename": file.filename}

@app.on_event("startup")
async def startup_event():
    print(f"Server starting on {settings.HOST}:{settings.PORT}")

@app.get("/")
async def root():
    return {"message": "Hello, Widgets!"}

#if __name__ == "__main__":
#    uvicorn.run("server.server:app", host=settings.HOST, port=settings.PORT, reload=True)