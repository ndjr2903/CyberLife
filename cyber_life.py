from encryptors import rsa_encryptor
from encryptors import aes_encryptor
from encryptors import hybrid_encryptor
from utils.drive_shield import encrypt_with_bitlocker, encrypt_with_veracrypt
from utils.file_handler import is_supported_file, is_sensitive
from utils.remote_encryptor import encrypt_remote_file
from utils.logger import log_action, log_failed_attempt
from utils.stats import update_stats
from utils import stats
from getpass import getpass
import os

def show_logo():
 print(r"""
════════════════════════════════════════════════════════════╗
║                                                           ║
║ ░▒█▀▀▄░▒█░░▒█░▒█▀▀▄░▒█▀▀▀░▒█▀▀▄░▒█░░░░▀█▀░▒█▀▀▀░▒█▀▀▀     ║
║ ░▒█░░░░▒▀▄▄▄▀░▒█▀▀▄░▒█▀▀▀░▒█▄▄▀░▒█░░░░▒█░░▒█▀▀░░▒█▀▀▀     ║
║ ░▒█▄▄▀░░░▒█░░░▒█▄▄█░▒█▄▄▄░▒█░▒█░▒█▄▄█░▄█▄░▒█░░░░▒█▄▄▄     ║
║                                                           ║
║                                                           ║
║    Created by: (ndjr2903)                                 ║
║                                                           ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
""")
show_logo()
print("\n[+] Advanced encryption, file analysis, and usage statistics")
print("Powered by Python 3")
print("[*] Choose your encryption method\n")

print("1. AES - Symmetric encryption")
print("2. Hybrid - Combination of AES and RSA")
print("3. Remote encryption via SSH")
print("4. Encrypt entire drive (BitLocker or VeraCrypt)")
print("5. Encrypting mac computers \n")

choice = input("🔢 Enter your choice (1-5): ").strip()


if choice in ["1", "2"]:
    file_path = input("📁 Enter the full path to the file: ").strip()
    if not is_supported_file(file_path):
        print("❌ File not found or unsupported. Please check the path.")
        exit()

    if is_sensitive(file_path):
        print("[!] Sensitive file detected - encryption is strongly recommended.")

    if choice == "1":
        try:
            key = aes_encryptor.generate_key()
            encrypted_path = aes_encryptor.encrypt_file(file_path, replace_original=True)
            print(f"✅ AES encryption completed: {encrypted_path}")
            update_stats('AES', os.path.basename(file_path))
            log_action("✅ AES encryption completed", file_path)
        except Exception as e:
            print(f"❌ CRITICAL ERROR IN AES: {e}")

    elif choice == "2":
        try:
            print("[DEBUG] Starting Hybrid encryption process...")
            encrypted_path = hybrid_encryptor.encrypt(file_path)
            full_enc_path = os.path.abspath(encrypted_path if encrypted_path else file_path)
            print(f"✅ Hybrid encryption completed successfully!")
            print(f"📁 Encrypted file saved at: {full_enc_path}")
            update_stats('Hybrid', os.path.basename(file_path))
            log_action("✅ Hybrid encryption completed", file_path)
        except Exception as e:
            print(f"❌ CRITICAL ERROR IN HYBRID: {e}")

elif choice == "3":
    print("🔐 Remote encryption via SSH selected.")
    ip = input("🌐 Enter remote IP address: ").strip()
    username = input("👤 Enter SSH username: ").strip()
    password = getpass("🔑 Enter SSH password: ").strip()
    remote_path = input("📁 Enter full path to remote file: ").strip()

    try:
        encrypted_path = encrypt_remote_file(ip, username, password, remote_path)
        if encrypted_path:
            update_stats("Remote", os.path.basename(remote_path))
            log_action("✅ Remote AES encryption completed", remote_path)
            print(f"✅ Remote file encrypted and saved locally as: {encrypted_path}")
        else:
            print("❌ Remote encryption failed.")
    except Exception as error:
        log_failed_attempt(str(error), remote_path)
        update_stats("❌ Remote encryption failed", remote_path)
        log_action("❌ Remote encryption failed", remote_path)

elif choice == "4":
    method = input("🔒 Choose method (bitlocker / veracrypt / remote-bitlocker): ").strip().lower()
    
    if method == "bitlocker":
        drive = input("💽 Enter drive letter (e.g. D): ").strip().upper()
        encrypt_with_bitlocker(drive)
        
    elif method == "veracrypt":
        path = input("📁 Enter full path for VeraCrypt volume: ").strip()
        password = getpass("🔑 Enter password for VeraCrypt volume: ").strip()
        size = input("📦 Enter volume size (e.g. 500M, 1G): ").strip()
        encrypt_with_veracrypt(path, password, size)
        
    elif method == "remote-bitlocker":
        comp_name = input("🌐 Enter target computer name/IP: ").strip()
        user = input("👤 Enter remote administrator username: ").strip()
        pwd = getpass("🔑 Enter remote password: ").strip()
        drive = input("💽 Enter drive letter to encrypt (e.g. C): ").strip().upper()
        encrypt_remote_bitlocker(comp_name, user, pwd, drive)
        
    else:
        print("❌ Invalid method. Choose 'bitlocker', 'veracrypt', or 'remote-bitlocker'.")

elif choice == "5":
    from utils.mac_shield import check_filevault_status, create_encrypted_dmg, create_veracrypt_volume
    print("🍏 MacShield selected.")
    action = input("wrench: Choose action (filevault/dmg/veracrypt): ").strip().lower()

    if action == "filevault":
        check_filevault_status()
    elif action == "dmg":
        name = input("📁 Volume name: ").strip()
        path = input("📌 Output path (e.g. ~/Desktop/SecureVault.dmg): ").strip()
        size = input("📦 Size (e.g. 100m): ").strip()
        create_encrypted_dmg(name, path, size)
    elif action == "veracrypt":
        path = input("📌 Volume path: ").strip()
        password = input("🔑 Password: ").strip()
        size = input("📦 Size (e.g. 500M): ").strip()
        create_veracrypt_volume(path, password, size)
    else:
        print("❌ Invalid action.")

else:
    print("❌ Invalid choice. Please select a valid option (1-5).")
