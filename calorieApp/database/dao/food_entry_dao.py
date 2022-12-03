import datetime

from ...database.core_database import database_session
from ...database.models.food_entry import FoodEntry
from .delete_food_entry_dao import add_deleted_food_entry


def create_food_entry(user, name, calorie, time):
    last_modified_time = datetime.datetime.now()
    entry = FoodEntry(user_id=user.user_id, food_name=name, time=time, calorie=calorie,
                      last_modified_time=last_modified_time)
    database_session.add(entry)
    database_session.commit()
    return entry


def delete_food_entry_by_id(food_entry):
    res = database_session.query(FoodEntry).filter_by(entry_id=food_entry.entry_id).delete()
    add_deleted_food_entry(entry_id=food_entry.entry_id, user_id=food_entry.user_id)
    database_session.commit()
    return res > 0


def get_food_entry_by_id(entry_id):
    return database_session.query(FoodEntry).filter_by(entry_id=entry_id).first()


def get_all_entries():
    return database_session.query(FoodEntry)


def update_food_entry(food_entry):
    food_entry.last_update_time = datetime.datetime.now()
    database_session.commit()


def get_food_entry_list_for_user(user_id, from_time, to_time):
    return database_session.query(FoodEntry).filter_by(user_id=user_id).filter(
        FoodEntry.time.between(from_time, to_time))


def get_food_entry_list_for_all_user(from_time, to_time):
    return database_session.query(FoodEntry).filter(
        FoodEntry.time.between(from_time, to_time))


def get_food_entry_list_after_time_for_admin(last_time):
    return database_session.query(FoodEntry).filter(FoodEntry.last_modified_time > last_time)


def get_food_entry_list_after_time_for_user(last_time, user_id):
    return database_session.query(FoodEntry).filter_by(user_id=user_id).filter(FoodEntry.last_modified_time > last_time)
