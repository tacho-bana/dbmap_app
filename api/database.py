from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Bar(Base):
    __tablename__ = "bars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)  # 座標をカンマ区切りの文字列として保存
    url = Column(String)

class Beer(Base):
    __tablename__ = "beers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

class BarBeer(Base):
    __tablename__ = "bar_beers"
    bar_id = Column(Integer, ForeignKey('bars.id'), primary_key=True)
    beer_id = Column(Integer, ForeignKey('beers.id'), primary_key=True)
    bar = relationship("Bar", back_populates="beers")
    beer = relationship("Beer", back_populates="bars")

Bar.beers = relationship("BarBeer", back_populates="bar")
Beer.bars = relationship("BarBeer", back_populates="beer")

Base.metadata.create_all(bind=engine)