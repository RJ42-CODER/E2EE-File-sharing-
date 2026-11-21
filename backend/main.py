from fastapi import FastAPI,Depends, HTTPException, Response, Cookie
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal
from models import User,Session as DBSession
from schemas import UserCreate, UserResponse, UserLogin
from security import hash_password, verify_password, generate_session_token, hash_session_token

from datetime import datetime, timedelta, timezone
from fastapi import Response


app = FastAPI(
    title="E2EE Secure File Sharing API",
    description="Backend API for an end-to-end encrypted file-sharing system",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(
        session_token: str = Cookie(default=None),
        db: Session = Depends(get_db)
):
    if not session_token: 
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    token_hash = hash_session_token(session_token)

    user_session = db.query(DBSession).filter(
        DBSession.token_hash == token_hash
    ).first()

    if not user_session:
        raise HTTPException(
            status_code=401,
            detail="Invalid session"
        )

    if user_session.expires_at <= datetime.now(timezone.utc):
        raise HTTPException(
            status_code=401,
            detail="Session Expired"
        )

    if user_session.revoked_at is not None:
        raise HTTPException(
            status_code=401,
            detail="Session has been revoked!"
        )

    user = db.query(User).filter(
        User.id == user_session.user_id
    ).first()

    if not user or not user.is_active:
        raise HTTPException(
            status_code=401,
            detail="User account is unavailable"
        )

    return user


@app.get('/me')
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    return {
        "message": "You are authenticated!",
        "user": {
            "id": current_user.id,
            "name": current_user.name,
            "email": current_user.email
        }
    }


@app.get('/')
def home():
    return {"message": "Welcome to the E2EE Secure File Sharing API!"}

@app.get('/health')
def health_check():
    return {"status": "healthy"}

@app.post('/register',response_model=UserResponse, status_code= 201)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    # hashed password
    hashed_password = hash_password(user_data.password)

    # create new user instance
    new_user = User(
        name= user_data.name,
        email=user_data.email,
        password_hash=hashed_password
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Email is already registered."
        )

    return new_user


@app.post('/login')
def login_user(user_data: UserLogin, response: Response, db: Session=Depends(get_db)):

    # find user by email
    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    # checking whther user exists and password is correct
    if not user or not verify_password(
        user_data.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail = "Account is Disabled"
        )

    token = generate_session_token()

    token_hash = hash_session_token(token)

    expires_at = datetime.now(timezone.utc) + timedelta(hours=8)

    new_session = DBSession(
        user_id = user.id,
        token_hash = token_hash,
        expires_at = expires_at
    )

    db.add(new_session)
    db.commit()

    response.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=8*60*60,
        path="/"
    )

    return {
        "message": "Login successful",
        "user":{
            "id":user.id,
            "name":user.name,
            "email":user.email
        }
    }

@app.post('/logout')
def logout_user(
    response:Response, 
    session_token: str = Cookie(default=None),
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # find user's current session before logout
    token_hash = hash_session_token(session_token)

    user_session = db.query(DBSession).filter(
        DBSession.token_hash == token_hash,
        DBSession.user_id == current_user.id
    ).first()

    if not user_session:
        raise HTTPException(
            status_code=401,
            detail="Session not found"
        )

    # revoke the session in postgresql
    user_session.revoked_at == datetime.now(timezone.utc)

    db.commit()

    # delete the browser cookie!
    response.delete_cookie(
        key="session_token",
        httponly=True,
        secure=False,
        samesite="lax",
        path="/"
    )

    return{
        "message":"Logout Successful"
    }

