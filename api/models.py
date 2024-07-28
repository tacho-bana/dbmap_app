# from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()

# class Bar(Base):
#     __tablename__ = 'bars'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     location = Column(String)
#     url = Column(String)

# class Beer(Base):
#     __tablename__ = 'beers'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)

# class BarBeer(Base):
#     __tablename__ = 'bar_beers'
#     bar_id = Column(Integer, primary_key=True, index=True)
#     beer_id = Column(Integer, primary_key=True, index=True)
