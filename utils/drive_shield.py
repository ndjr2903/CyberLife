import subprocess
import os

def encrypt_with_bitlocker(drive_letter):
    """
    Starts local BitLocker encryption on the specified drive.
    Requires administrator privileges.
    """
    print(f"🔐 Starting local BitLocker encryption on {drive_letter}:")
    command = f"manage-bde -on {drive_letter}: -RecoveryPassword"
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ Local BitLocker encryption started on {drive_letter}:")
    except subprocess.CalledProcessError:
        print("❌ BitLocker failed. Make sure you're running as administrator.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

def encrypt_with_veracrypt(volume_path, password, size="500M"):
    """
    Creates a VeraCrypt encrypted volume at the specified path.
    VeraCrypt must be installed on the system.
    """
    print(f"🔐 Creating VeraCrypt volume at {volume_path}")
    veracrypt_path = r"C:\Program Files\VeraCrypt\VeraCrypt.exe"
    command = (
        f'"{veracrypt_path}" /create "{volume_path}" '
        f'/password "{password}" /size {size} '
        f'/encryption AES /filesystem NTFS /silent'
    )
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"✅ VeraCrypt volume created at {volume_path}")
    except subprocess.CalledProcessError:
        print("❌ VeraCrypt failed. Make sure VeraCrypt is installed and path is correct.")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")

def encrypt_remote_bitlocker(computer_name, username, password, drive_letter="C"):
    """
    Enables BitLocker on a remote Windows computer using PowerShell Remoting (WinRM).
    Requires administrator credentials on the target machine.
    """
    print(f"🌐 Connecting to remote Windows machine: {computer_name}...")
    
    ps_command = (
        f"$secpasswd = ConvertTo-SecureString '{password}' -AsPlainText -Force; "
        f"$mycred = New-Object System.Management.Automation.PSCredential ('{username}', $secpasswd); "
        f"Invoke-Command -ComputerName '{computer_name}' -Credential $mycred -ScriptBlock {{"
        f"  Enable-BitLocker -MountPoint '{drive_letter}:' -EncryptionMethod XtsAes256 -UsedSpaceOnly -PasswordProtector"
        f"}}"
    )

    try:
        result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True, check=True)
        print(f"✅ Remote BitLocker encryption initiated successfully on {computer_name}!")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Remote BitLocker failed: {e.stderr.strip()}")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
