import datetime

from ..core_database import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


class DeletedFoodEntry(BaseModel):
    __tablename__ = "deleted_food_entry"
    entry_id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.user_id', ondelete="CASCADE"))
    time = Column(DateTime)
