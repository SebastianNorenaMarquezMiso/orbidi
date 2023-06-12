from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import Settings


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            engine = create_engine(Settings.DB_URL)
            SessionLocal = sessionmaker(
                autocommit=False, autoflush=False, bind=engine)
            cls._instance = SessionLocal()
        return cls._instance

    def __getattr__(self, name):
        return getattr(self._instance, name)


db = Database()
