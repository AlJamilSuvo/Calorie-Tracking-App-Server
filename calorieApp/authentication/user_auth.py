import jwt
from config.server_secret import server_secret
from ..database.dao.user_dao import get_user_by_user_id


def get_user_auth_token(user):
    payload = {'user_id': user.user_id, 'user_key': user.user_key}
    auth_token = jwt.encode(payload=payload, key=server_secret, algorithm='HS256')
    return auth_token


def authenticate_user(authorization_header):
    if authorization_header is None:
        return None
    tokenized = authorization_header.split(' ')
    if len(tokenized) != 2:
        return None

    auth_type = tokenized[0]
    auth_token = tokenized[1]
    if auth_type != 'Bearer':
        return None
    print(auth_token)
    payload = jwt.decode(auth_token, key=server_secret, algorithms='HS256')
    user_id = payload['user_id']
    user_key = payload['user_key']
    print(user_id, user_key)
    user = get_user_by_user_id(user_id)
    print(user)
    if user is None:
        return None
    print(user.user_key)
    print(user)

    if user.user_key != user_key:
        return None

    return user
