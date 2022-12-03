import random
import string

key_char_list = string.digits + string.punctuation + string.ascii_letters


def generate_key(key_len):
    return ''.join(random.choice(key_char_list) for _ in range(key_len))


def user_key_generator():
    return generate_key(32)
