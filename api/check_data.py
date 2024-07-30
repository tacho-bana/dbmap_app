from database import SessionLocal, Bar, Beer, BarBeer

def get_all_data():
    db = SessionLocal()
    try:
        bars = db.query(Bar).all()
        beers = db.query(Beer).all()
        bar_beers = db.query(BarBeer).all()

        print("Bars:")
        for bar in bars:
            print(f"ID: {bar.id}, Name: {bar.name}, Location: {bar.location}, URL: {bar.url}")

        print("\nBeers:")
        for beer in beers:
            print(f"ID: {beer.id}, Name: {beer.name}")

        print("\nBarBeers:")
        for bar_beer in bar_beers:
            print(f"Bar ID: {bar_beer.bar_id}, Beer ID: {bar_beer.beer_id}")

    finally:
        db.close()

if __name__ == "__main__":
    get_all_data()