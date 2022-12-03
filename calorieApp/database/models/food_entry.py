import datetime

from ..core_database import BaseModel
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Numeric


class FoodEntry(BaseModel):
    __tablename__ = "food_entry"
    entry_id = Column(Integer, primary_key=True, autoincrement=True)
    food_name = Column(String)
    user_id = Column(String, ForeignKey('user.user_id', ondelete="CASCADE"))
    time = Column(DateTime)
    calorie = Column(Numeric)
    last_modified_time = Column(DateTime)

    def to_json(self):
        return {
            'entry_id': self.entry_id,
            'food_name': self.food_name,
            'timestamp': int(datetime.datetime.timestamp(self.time) * 1000),
            'calorie': self.calorie.real,
            'user_id': self.user_id
        }

    def __repr__(self):
        return "<FoodEntry(entry_id = " + str(
            self.entry_id) + " food_name = " + self.food_name + ", user_id = " + self.user_id + ", time = " + str(
            self.time) + ", calorie = " + str(self.calorie) + ")>"
