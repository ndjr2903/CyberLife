from encryptors import aes_encryptor, rsa_encryptor
import os

def encrypt(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    print("🔐 Starting hybrid encryption (AES + RSA)...", flush=True)

    try:
        # שלב 1: הצפנת הקובץ באמצעות AES (דורס את הקובץ המקורי או מצפין אותו)
        aes_encryptor.generate_key()
        aes_encryptor.encrypt_file(file_path, replace_original=True)

        # שלב 2: יצירת מפתחות RSA והצפנת הקובץ / מפתח ה-AES
        rsa_encryptor.generate_keys()
        rsa_encryptor.encrypt_file(file_path)

        print(f"✅ Hybrid encryption completed successfully for: {file_path}", flush=True)
        return file_path
    except Exception as e:
        print(f"❌ Hybrid encryption internal error: {e}", flush=True)
        raise e

def decrypt(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return

    print("🔓 Starting hybrid decryption (RSA + AES)...", flush=True)

    try:
        # שלב 1: פענוח ה-RSA
        rsa_encryptor.decrypt_file(file_path)

        # שלב 2: פענוח ה-AES
        aes_encryptor.decrypt_file(file_path)

        print(f"✅ Hybrid decryption completed successfully.", flush=True)
        return file_path
    except Exception as e:
        print(f"❌ Hybrid decryption internal error: {e}", flush=True)
        raise e
