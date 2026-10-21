import os
from encryptors import aes_encryptor
from utils.file_handler import is_supported_file, is_sensitive

def encrypt_folder(folder_path):
    """
    Encrypt all supported files in the folder using AES.
    Sensitive files will be flagged before encryption.
    """
    for root, _, files in os.walk(folder_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            if os.path.isfile(full_path) and is_supported_file(full_path):
                if is_sensitive(full_path):
                    print(f"⚠️ Sensitive file detected: {filename}")
                aes_encryptor.encrypt_file(full_path)
                print(f"🔐 Encrypted: {filename}")
		else:
   		 print(f"❌ Unsupported file type: {filename}")
