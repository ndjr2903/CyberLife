from cryptography.fernet import Fernet
from utils.key_manager import save_key, load_key
import os

KEY_NAME = "aes.key"


def generate_key():
    key = Fernet.generate_key()
    save_key(key, KEY_NAME)
    print("🔑 AES key generated and saved.")
    return key


def encrypt_file(file_path, replace_original=False):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    key = load_key(KEY_NAME)
    cipher = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)

    if replace_original:
        with open(file_path, "wb") as f:
            f.write(encrypted)

        print(f"✅ File encrypted (replaced): {file_path}")
        return file_path

    else:
        out_path = file_path + ".enc"

        with open(out_path, "wb") as f:
            f.write(encrypted)

        print(f"✅ File encrypted: {out_path}")
        return out_path


def decrypt_file(file_path, output_suffix=".dec"):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return None

    key = load_key(KEY_NAME)
    cipher = Fernet(key)

    with open(file_path, "rb") as f:
        encrypted = f.read()

    decrypted = cipher.decrypt(encrypted)

    if output_suffix is None:
        with open(file_path, "wb") as f:
            f.write(decrypted)

        print(f"✅ File decrypted (replaced): {file_path}")
        return file_path

    else:
        out_path = file_path.replace(".enc", output_suffix)

        with open(out_path, "wb") as f:
            f.write(decrypted)

        print(f"✅ File decrypted: {out_path}")
        return out_path
