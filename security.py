import os
from cryptography.fernet import Fernet

# Retrieve the Fernet encryption key from the environment variable 'FERNET_KEY'
FERNET_KEY = os.environ.get("FERNET_KEY")

# Raise an error if the environment variable is not set
if not FERNET_KEY:
    raise ValueError("FERNET_KEY not set in environment variables")

# Create a Fernet object using the provided encryption key
# The key must be in bytes, hence the use of .encode()
f = Fernet(FERNET_KEY.encode())

def encrypt_password(password: str) -> str:
    """
    Encrypts a plaintext password using Fernet encryption.

    Args:
        password (str): The plaintext password to encrypt.

    Returns:
        str: The encrypted password as a base64-encoded string.
    """
    return f.encrypt(password.encode()).decode()  # Encrypt and decode to string for storage/transmission

def decrypt_password(encrypted_password: str) -> str:
    """
    Decrypts an encrypted password using Fernet decryption.

    Args:
        encrypted_password (str): The base64-encoded encrypted password.

    Returns:
        str: The original plaintext password.
    """
    return f.decrypt(encrypted_password.encode()).decode()  # Decode encrypted string, decrypt, then decode to text
