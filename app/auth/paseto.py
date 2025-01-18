import time

import pyseto

from utils.paseto import private_key, public_key


def generate_paseto_token(user_id):
    now = int(time.time())
    payload = {
        "sub": user_id,
        "iat": now,
        "exp": now + 3600,
    }
    token = pyseto.encode(key=private_key, payload=payload)
    return token


def decode_paseto_token(token: bytes):
    content = pyseto.decode(keys=public_key, token=token)
    return content
