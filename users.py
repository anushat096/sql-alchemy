import datetime
from sqlalchemy import Column, DateTime, Integer, String

from base import Base

class User(Base):
    __tablename__ = 'users'
    user_id= Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String, unique= True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
