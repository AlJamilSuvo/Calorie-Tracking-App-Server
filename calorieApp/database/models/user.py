from ..core_database import BaseModel
from sqlalchemy import Column, String, Boolean


class User(BaseModel):
    __tablename__ = "user"
    user_id = Column(String, primary_key=True)
    is_admin = Column(Boolean)
    user_key = Column(String)

    def __repr__(self):
        return "<User(user_id = '%s', user_name = '%d'>" \
               % (self.user_id, self.is_admin)
