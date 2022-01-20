from venv import create
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from testconfig import TestConfig

config = TestConfig()

engine = create_engine(config.db("URL"),
                        connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_models():
    Base.metadata.create_all(bind=engine)


#Create db session per each app request
def db_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()