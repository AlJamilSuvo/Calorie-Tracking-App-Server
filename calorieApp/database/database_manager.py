from .models.user import User
from .models.food_entry import FoodEntry
from .models.deleted_food_entry import DeletedFoodEntry
from .core_database import BaseModel
from .core_database import database_engine


def initialize_database():
    print('tables:')
    print(User.__table__)
    print(FoodEntry.__table__)
    print(DeletedFoodEntry.__table__)
    BaseModel.metadata.create_all(database_engine)
