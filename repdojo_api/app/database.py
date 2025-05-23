from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base


DATABASE_URL = "sqlite:///../data/repdojo.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
