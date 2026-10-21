from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
import os

# שימוש בנתיב מוחלט לפי מיקום הקובץ הנוכחי כדי למנוע בעיות גישה לתיקייה
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_DIR = os.path.join(BASE_DIR, "keys")
PRIVATE_KEY_FILE = os.path.join(KEY_DIR, "rsa_private.pem")
PUBLIC_KEY_FILE = os.path.join(KEY_DIR, "rsa_public.pem")

def generate_keys():
    print("[DEBUG] Generating RSA keys...", flush=True)
    try:
        # וידוא שתיקיית המפתחות קיימת
        os.makedirs(KEY_DIR, exist_ok=True)
        print(f"[DEBUG] Keys directory verified at: {KEY_DIR}", flush=True)

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_key = private_key.public_key()

        with open(PRIVATE_KEY_FILE, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        with open(PUBLIC_KEY_FILE, "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))

        print("🔑 RSA key pair generated and saved successfully.", flush=True)
    except Exception as e:
        print(f"❌ CRITICAL ERROR in generate_keys: {e}", flush=True)

def load_public_key():
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        print("⚠️ RSA keys missing — generating new pair...", flush=True)
        generate_keys()

    with open(PUBLIC_KEY_FILE, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def load_private_key():
    if not os.path.exists(PRIVATE_KEY_FILE) or not os.path.exists(PUBLIC_KEY_FILE):
        print("⚠️ RSA keys missing — generating new pair...", flush=True)
        generate_keys()

    with open(PRIVATE_KEY_FILE, "rb") as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def encrypt_file(file_path):
    print(f"[DEBUG] rsa encrypt_file() called on: {file_path}", flush=True)
    if not os.path.exists(file_path):
        print(f"❌ File not found for RSA: {file_path}", flush=True)
        return

    try:
        public_key = load_public_key()
        with open(file_path, "rb") as f:
            data = f.read()

        encrypted = public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open(file_path, "wb") as f:
            f.write(encrypted)
        print(f"✅ RSA encryption step completed for: {file_path}", flush=True)
    except Exception as e:
        print(f"❌ RSA encryption failed: {e}", flush=True)

def decrypt_file(file_path):
    print(f"[DEBUG] rsa decrypt_file() called on: {file_path}", flush=True)
    if not os.path.exists(file_path):
        print(f"❌ File not found for RSA decrypt: {file_path}", flush=True)
        return

    try:
        private_key = load_private_key()
        with open(file_path, "rb") as f:
            encrypted_data = f.read()

        decrypted = private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"✅ RSA decryption step completed for: {file_path}", flush=True)
    except Exception as e:
        print(f"❌ RSA decryption failed: {e}", flush=True)
