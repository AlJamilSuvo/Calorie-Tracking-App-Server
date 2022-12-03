from ..database.dao.user_dao import create_admin, get_user_by_user_id, delete_user
from ..authentication.user_auth import get_user_auth_token


def add_admin_user(admin_id):
    print('creating admin ' + admin_id)
    admin_user = get_user_by_user_id(admin_id)
    if admin_user is not None:
        print(admin_id + ' already taken can not add admin with this id')
        return
    admin_user = create_admin(admin_id)
    auth_token = get_user_auth_token(admin_user)
    print('admin added. token :')
    print(auth_token)


def remove_admin_user(admin_id):
    admin_user = get_user_by_user_id(admin_id)
    if admin_user is None or not admin_user.is_admin:
        print(admin_id + ' no admin with this id')
        return
    delete_user(admin_user.user_id)
    print(admin_id + ' deleted')
