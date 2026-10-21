from encryptors import aes_encryptor, rsa_encryptor, hybrid_encryptor
from utils.file_handler import is_sensitive

def encrypt_by_sensitivity(file_path):
    level = is_sensitive(file_path)  # should return "low", "medium", or "high"

    try:
        if level == "low":
            aes_encryptor.generate_key()
            aes_encryptor.encrypt_file(file_path)
            print("🔐 Encrypted with AES (low sensitivity).")
        elif level == "medium":
            rsa_encryptor.generate_keys()
            rsa_encryptor.encrypt_file(file_path)
            print("🔐 Encrypted with RSA (medium sensitivity).")
        elif level == "high":
            hybrid_encryptor.hybrid_encrypt(file_path)
            print("🔐 Encrypted with HYBRID (high sensitivity).")
        else:
            print("⚠️ Unknown sensitivity level. Defaulting to AES.")
            aes_encryptor.generate_key()
            aes_encryptor.encrypt_file(file_path)
    except Exception as e:
        print(f"❌ Encryption failed: {e}")
