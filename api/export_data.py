import json
from database import SessionLocal, Bar, Beer, BarBeer

def export_data_to_json():
    db = SessionLocal()
    try:
        bars = db.query(Bar).all()
        beers = db.query(Beer).all()
        bar_beers = db.query(BarBeer).all()
        
        data = {
            "bars": [
                {
                    "id": bar.id,
                    "name": bar.name,
                    "location": bar.location,
                    "url": bar.url
                }
                for bar in bars
            ],
            "beers": [
                {
                    "id": beer.id,
                    "name": beer.name
                }
                for beer in beers
            ],
            "bar_beers": [
                {
                    "bar_id": bar_beer.bar_id,
                    "beer_id": bar_beer.beer_id
                }
                for bar_beer in bar_beers
            ]
        }
        
        with open('data.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    finally:
        db.close()

if __name__ == "__main__":
    export_data_to_json()