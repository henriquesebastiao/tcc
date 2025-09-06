import hashlib

def hash_id(user_id: str) -> str:
    return hashlib.sha256(user_id.encode('utf-8')).hexdigest()