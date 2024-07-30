from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, Bar, Beer, BarBeer, SessionLocal

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/bars")
def get_bars(beer_name: str, db: Session = Depends(get_db)):
    beer = db.query(Beer).filter(Beer.name == beer_name).first()
    if not beer:
        raise HTTPException(status_code=404, detail="Beer not found")

    bars = db.query(Bar).join(BarBeer).filter(BarBeer.beer_id == beer.id).all()
    return [{"name": bar.name, "location": bar.location, "url": bar.url} for bar in bars]

@app.get("/")
def read_root():
    return {"Hello": "World"}