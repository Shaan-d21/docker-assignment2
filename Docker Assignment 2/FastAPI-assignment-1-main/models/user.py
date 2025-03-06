# models/user.py
from sqlalchemy import Column, Integer, String, Enum
from database import Base
import enum

# Define user roles as an Enum
class Role(enum.Enum):
    admin = "admin"
    participant = "participant"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)  # Unique username
    hashed_password = Column(String)                    # Store hashed password
    role = Column(Enum(Role))                           # Role: admin or participant