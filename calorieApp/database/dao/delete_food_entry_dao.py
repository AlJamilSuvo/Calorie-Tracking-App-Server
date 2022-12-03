import datetime

from ..models.deleted_food_entry import DeletedFoodEntry
from ...database.core_database import database_session


def add_deleted_food_entry(entry_id, user_id):
    time = datetime.datetime.now()
    entry = DeletedFoodEntry(entry_id=entry_id, user_id=user_id, time=time)
    database_session.add(entry)
    database_session.commit()


def get_deleted_food_entry_list_after_time_for_admin(last_time):
    return database_session.query(DeletedFoodEntry).filter(DeletedFoodEntry.time > last_time)


def get_deleted_food_entry_list_after_time_for_user(last_time, user_id):
    return database_session.query(DeletedFoodEntry).filter_by(user_id=user_id).filter(DeletedFoodEntry.time > last_time)
