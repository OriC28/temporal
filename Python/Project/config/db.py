from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

url = "mysql+pymysql://root:Ori31525588$$.@localhost:3306/storedb"
engine = create_engine(url)


Session = sessionmaker(bind=engine)
session = Session()

