from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base
from sqlalchemy import ForeignKey

class User(Base):
    __tablename__ = "users"

    # columns for the users table in the database. Each column is defined with its data type and constraints. The id column is the primary key and is indexed for faster lookups. The name, email, and password_hash columns store user information, with email being unique to prevent duplicate entries. The is_active column indicates whether the user account is active, and created_at stores the timestamp of when the user was created, with a default value of the current time.
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=True,nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Session(Base):
    __tablename__ = "sessions"

    # here, foreign keys used for users.id reference
    id = Column(
        Integer,
        primary_key=True,
        index=True
        )
    
    user_id = Column(
        Integer,ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False,
        index=True
        )
    
    token_hash = Column(
        String(64), 
        unique=True,
        nullable=False, 
        index=True
        )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    expires_at = Column(
        DateTime(timezone=True),
        nullable=False
    )

    revoked_at = Column(
        DateTime(timezone=True),
        nullable=True
    )
