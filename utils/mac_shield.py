import subprocess

def check_filevault_status():
    """
    Checks whether FileVault is enabled on macOS.
    """
    try:
        result = subprocess.check_output(["fdesetup", "status"]).decode()
        print(f"🛡️ FileVault status: {result.strip()}")
    except Exception as e:
        print(f"❌ Unable to check FileVault status: {str(e)}")

def create_encrypted_dmg(volume_name, output_path, size="100m"):
    """
    Creates an encrypted DMG file with a password.
    """
    try:
        command = [
            "hdiutil", "create",
            "-encryption", "AES-256",
            "-size", size,
            "-fs", "HFS+",
            "-volname", volume_name,
            output_path
        ]
        subprocess.run(command, check=True)
        print(f"✅ Encrypted DMG created at: {output_path}")
    except Exception as e:
        print(f"❌ Failed to create DMG: {str(e)}")

def create_veracrypt_volume(path, password, size="500M"):
    """
    Creates a VeraCrypt encrypted volume (if VeraCrypt is installed).
    """
    try:
        command = [
            "/Applications/VeraCrypt.app/Contents/MacOS/VeraCrypt",
            "--create", path,
            "--password", password,
            "--size", size,
            "--encryption", "AES",
            "--filesystem", "APFS",
            "--silent"
        ]
        subprocess.run(command, check=True)
        print(f"✅ VeraCrypt volume created at: {path}")
    except Exception as e:
        print(f"❌ VeraCrypt failed: {str(e)}")
