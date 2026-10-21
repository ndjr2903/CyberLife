import os
from encryptors import aes_encryptor, rsa_encryptor, hybrid_encryptor

def detect_encryption_type(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".enc":
        return "AES"
    elif ext == ".rsa":
        return "RSA"
    elif ext == ".hyb":
        return "HYBRID"
    return None

def auto_decrypt(file_path):
    encryption_type = detect_encryption_type(file_path)
    if not encryption_type:
        print("❌ Unknown encryption type.")
        return

    try:
        if encryption_type == "AES":
            aes_encryptor.decrypt_file(file_path)
        elif encryption_type == "RSA":
            rsa_encryptor.decrypt_file(file_path)
        elif encryption_type == "HYBRID":
            hybrid_encryptor.hybrid_decrypt(file_path)
        print(f"✅ Auto-decryption completed using {encryption_type}.")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")
