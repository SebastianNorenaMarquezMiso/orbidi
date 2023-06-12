from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ApiCall(Base):
    __tablename__ = 'api_calls'
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    endpoint = Column(String)
    params = Column(String)
    result = Column(String)

    def __repr__(self):
        return f"<ApiCall(id='{self.id}', timestamp='{self.timestamp}', method='{self.method}', endpoint='{self.endpoint}', params='{self.params}', response='{self.response}')>"
