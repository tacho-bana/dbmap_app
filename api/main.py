from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# CORS設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 適切なオリジンに制限してください
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    with open("../data.json", "r") as file:
        data = json.load(file)
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)