from fastapi import FastAPI
from fastapi import APIRouter, UploadFile

from werkzeug.utils import secure_filename

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


v1_router = APIRouter(prefix="/files", tags=["Files"])

@app.post(
    "/files",
)
async def upload(
    file: UploadFile,
):
    # Access the uploaded file and get its filename and content type
    filename = secure_filename(file.filename)
    content_type = file.content_type
    print(f"Filename: {filename}")