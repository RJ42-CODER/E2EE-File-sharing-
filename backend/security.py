from pwdlib import PasswordHash
import secrets
import hashlib

password_hash = PasswordHash.recommended()

def generate_session_token() -> str:
    return secrets.token_urlsafe(32)

def hash_session_token(token:str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()

def hash_password(password:str) -> str:
    return password_hash.hash(password)

def verify_password(password:str, hashed_password: str) -> bool:
    try:
        return password_hash.verify(password,hashed_password)
    except Exception:
        return False