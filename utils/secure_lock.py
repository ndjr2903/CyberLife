import os
from encryptors import aes_encryptor

def lock_file(file_path):
    # הצפנה רגילה
    aes_encryptor.generate_key()
    aes_encryptor.encrypt_file(file_path)

    # מחיקת הקובץ המקורי (אופציונלי)
    os.remove(file_path)

    # יצירת קובץ "נעול" עם הודעת שגיאה
    locked_path = file_path + ".locked"
    with open(locked_path, "w") as f:
        f.write("❌ This file is encrypted and cannot be opened without the key.\n")
        f.write("🔐 Use CYBER LIFE PRO to decrypt this file securely.\n")

    print(f"🔒 File locked: {locked_path}")
