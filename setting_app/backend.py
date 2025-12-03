from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os

app = FastAPI()

# store files under the `mydata` directory
FILE_DIR = "mydata"
FILE_PATH = os.path.join(FILE_DIR, "usr.txt")


class TextData(BaseModel):
    text: str


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/save")
async def save_text(data: TextData):
    try:
        # ensure directory exists before writing
        if FILE_DIR:
            os.makedirs(FILE_DIR, exist_ok=True)

        with open(FILE_PATH, "a") as f:
            f.write(data.text + "\n")
        return {"message": "Text saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
