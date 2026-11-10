from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil

app = FastAPI(title="AI FaceSwap API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)
os.makedirs("results", exist_ok=True)


@app.get("/")
def home():
    return {"status": "Backend Running"}


@app.post("/upload")
async def upload(
    source: UploadFile = File(...),
    target: UploadFile = File(...)
):
    source_path = f"uploads/{source.filename}"
    target_path = f"uploads/{target.filename}"

    with open(source_path, "wb") as buffer:
        shutil.copyfileobj(source.file, buffer)

    with open(target_path, "wb") as buffer:
        shutil.copyfileobj(target.file, buffer)

    return {
        "message": "Images uploaded successfully",
        "source": source.filename,
        "target": target.filename
    }
