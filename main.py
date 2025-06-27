from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from pydantic import BaseModel
import os

from database import SessionLocal, engine, Base
from models import User
from security import encrypt_password, decrypt_password

# Security capability code for protected endpoints
CAPABILITY_CODE = "ALPHA"

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Serve static frontend files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Serve the main frontend page
@app.get("/")
def read_root():
    return FileResponse(os.path.join("frontend", "index.html"))

# Database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Check for valid capability code in the header
def check_capability(x_code: str = Header(...)):
    if x_code != CAPABILITY_CODE:
        raise HTTPException(status_code=403, detail="Unauthorized: Invalid capability code")

# Pydantic model for user input
class UserCreate(BaseModel):
    username: str
    password: str

# Register a new user
@app.post("/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    encrypted_password = encrypt_password(user.password)
    new_user = User(username=user.username, encrypted_password=encrypted_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}

# User login
@app.post("/login")
def login_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    x_code: str = Depends(check_capability)
):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found. Please register first")

    try:
        decrypted = decrypt_password(db_user.encrypted_password)
        if decrypted != user.password:
            raise HTTPException(status_code=401, detail="Incorrect password")
    except Exception:
        raise HTTPException(status_code=400, detail="Error decrypting password")

    return {"message": "Login successful!"}
