from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from jinja2 import Environment, FileSystemLoader
from .database import SessionLocal, Bar
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

env = Environment(loader=FileSystemLoader('templates'))

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
def read_root(db: Session = Depends(get_db)):
    bars = db.query(Bar).all()
    api_key = os.getenv("AIzaSyCFeicvzF14E1Yt8XU615M0I0SBcv4NlcU")
    template = env.get_template('index.html')
    html_content = template.render(bars=bars, api_key=api_key)
    return HTMLResponse(content=html_content)
