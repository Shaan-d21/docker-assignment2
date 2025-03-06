# utils/security.py
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

# Secret key for JWT (replace with a secure key in production)
SECRET_KEY = "ff5667dc669c6a3bb3e230abb6e7ffd0fdc4a75bbabbeaf1a76345f45ea749dc"
ALGORITHM = "HS256"

# Password hashing context
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token authentication
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")

# Hash a password
def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)

# Verify a password against its hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)

# Create a JWT token
def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta) -> str:
    encode = {"sub": username, "id": user_id, "role": role}
    expires = datetime.utcnow() + expires_delta
    encode["exp"] = expires
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

# Decode a JWT token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# Get the current user from the token
async def get_current_user(token: str = Depends(oauth2_bearer)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    username = payload.get("sub")
    user_id = payload.get("id")
    role = payload.get("role")
    if not username or not user_id or not role:
        raise HTTPException(status_code=401, detail="Invalid token data")
    return {"username": username, "id": user_id, "role": role}

# Ensure the user is an admin
async def get_current_admin(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Must be an admin")
    return current_user

# Ensure the user is a participant
async def get_current_participant(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "participant":
        raise HTTPException(status_code=403, detail="Must be a participant")
    return current_user