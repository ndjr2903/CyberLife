import os
from cryptography.fernet import Fernet

KEYS_DIR = "keys"

def generate_key():
    """Generate a new Fernet encryption key."""
    return Fernet.generate_key()

def save_key(key, filename):
    """Save the key to a file inside the keys directory."""
    os.makedirs(KEYS_DIR, exist_ok=True)
    path = os.path.join(KEYS_DIR, filename)
    try:
        with open(path, "wb") as f:
            f.write(key)
        print(f"🔑 Key saved to {path}")
    except Exception as e:
        print(f"❌ Failed to save key: {e}")

def load_key(filename):
    """Load the key from a file inside the keys directory."""
    path = os.path.join(KEYS_DIR, filename)
    if not os.path.exists(path):
        raise FileNotFoundError(f"❌ Key file not found: {path}")
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception as e:
        raise IOError(f"❌ Failed to load key: {e}")
