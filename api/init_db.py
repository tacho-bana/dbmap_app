from sqlalchemy.orm import Session
from database import engine, Base, Bar, Beer, BarBeer

Base.metadata.create_all(bind=engine)

def init_db():
    db = Session(bind=engine)
    
    # テーブルをクリア
    db.query(BarBeer).delete()
    db.query(Bar).delete()
    db.query(Beer).delete()
    
    # データの追加
    bars = [
        Bar(name='てけてけ 大井町店', location='POINT(35.607402463191185, 139.73579221997014)', url='https://tabelog.com/tokyo/A1315/A131501/13208082/'),
        Bar(name='餃子酒場 大井町店', location='POINT(35.60828876379359, 139.73729332877033)', url='https://tabelog.com/tokyo/A1315/A131501/13245478/'),
        Bar(name='鳥貴族 大井町西口店', location='POINT(35.60755922095193, 139.73232659545533)', url='https://tabelog.com/tokyo/A1315/A131501/13145521/'),
        Bar(name='大井町かき殻荘', location='POINT(35.60762786456085, 139.7366815410772)', url='https://tabelog.com/tokyo/A1315/A131501/13158091/'),
        Bar(name='味の磯平', location='POINT(35.607773259116655, 139.7325847236955)', url='https://tabelog.com/tokyo/A1315/A131501/13156499/'),
        Bar(name='ひな鳥 そのだ', location='POINT(35.60713367480308, 139.74039953672656)', url='https://tabelog.com/tokyo/A1315/A131501/13137722/'),
        Bar(name='燻製キッチン', location='POINT(35.60335925463164, 139.73232935832797)', url='https://tabelog.com/tokyo/A1315/A131501/13060616/'),
        Bar(name='俺のやきとり 大井町', location='POINT(35.607907399307386, 139.73113005692971)', url='https://tabelog.com/tokyo/A1315/A131501/13109557/'),
        Bar(name='かき殻荘', location='POINT(35.607634076987466, 139.73668170693765)', url='https://tabelog.com/tokyo/A1315/A131501/13158091/')
    ]
    beers = [
        Beer(id=1, name='アサヒスーパードライ'),
        Beer(id=2, name='黒ラベル'),
        Beer(id=3, name='オリオン ザ・ドラフト'),
        Beer(id=4, name='一番搾り'),
        Beer(id=5, name='サントリー生ビール'),
        Beer(id=6, name='サッポロラガー'),
        Beer(id=7, name='ヱビスビール'),
        Beer(id=8, name='プレミアムモルツ'),
        Beer(id=9, name='その他')
    ]
    bar_beers = [
        BarBeer(bar_id=1, beer_id=7),
        BarBeer(bar_id=2, beer_id=8),
        BarBeer(bar_id=3, beer_id=2),
        BarBeer(bar_id=3, beer_id=6),
        BarBeer(bar_id=3, beer_id=9),
        BarBeer(bar_id=4, beer_id=8),
        BarBeer(bar_id=5, beer_id=4),
        BarBeer(bar_id=5, beer_id=9),
        BarBeer(bar_id=6, beer_id=1),
        BarBeer(bar_id=6, beer_id=9),
        BarBeer(bar_id=7, beer_id=8),
        BarBeer(bar_id=7, beer_id=6),
        BarBeer(bar_id=8, beer_id=2),
        BarBeer(bar_id=9, beer_id=2)
    ]
    db.add_all(bars + beers + bar_beers)
    db.commit()

if __name__ == "__main__":
    init_db()
