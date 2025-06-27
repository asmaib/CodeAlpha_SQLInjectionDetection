from sqlalchemy import Column, Integer, String
from database import Base

# Define the User model which maps to the 'users' table in the database
class User(Base):
    __tablename__ = "users"  # Name of the table in the database

    # Primary key column for the user ID
    id = Column(Integer, primary_key=True, index=True)

    # Username column
    # - String with a max length of 255 characters
    # - Must be unique (no duplicate usernames)
    # - Indexed for faster search
    # - Cannot be null
    username = Column(String(255), unique=True, index=True, nullable=False)

    # Encrypted password column
    # - String with a max length of 512 characters (to accommodate encrypted data)
    # - Cannot be null
    encrypted_password = Column(String(512), nullable=False)
