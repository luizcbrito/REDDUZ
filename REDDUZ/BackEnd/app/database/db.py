from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+psycopg://redduz_user:redduz123@localhost:5432/redduz"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={
        "options": "-c client_encoding=UTF8"
    }
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
