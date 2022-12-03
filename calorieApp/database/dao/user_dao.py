from ...database.core_database import database_session
from ...database.models.user import User
from ...util.key_generator import user_key_generator


def create_user(user_id):
    try:
        if get_user_by_user_id(user_id):
            return False
        user_key = user_key_generator()
        user = User(user_id=user_id, is_admin=False, user_key=user_key)
        database_session.add(user)
        database_session.commit()
        return user
    except:
        return False


def create_admin(user_id):
    try:
        if get_user_by_user_id(user_id):
            return False
        user_key = user_key_generator()
        user = User(user_id=user_id, is_admin=True, user_key=user_key)
        database_session.add(user)
        database_session.commit()
        return user
    except:
        return False


def delete_user(user_id):
    database_session.query(User).filter_by(user_id=user_id).delete()
    database_session.commit()


def check_user_exists(user_id):
    return get_user_by_user_id(user_id) is not None


def get_user_by_user_id(user_id):
    return database_session.query(User).filter_by(user_id=user_id).first()
