import datetime
import os

LOG_PATH = "logs/cyberlife.log"
REMOTE_LOG_PATH = "logs/remote.log"

def log_action(action, target):
    """
    Log a successful encryption or system action.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] ✅ {action} on {target}\n"
    _write_log(LOG_PATH, message)

def log_failed_attempt(error, target):
    """
    Log a failed encryption attempt or error.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] ❌ Failed attempt on {target}: {error}\n"
    _write_log(LOG_PATH, message)

def log_remote_action(action, ip, remote_path):
    """
    Log a remote encryption action via SSH.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"[{timestamp}] 🌐 Remote action: {action} | IP: {ip} | File: {remote_path}\n"
    _write_log(REMOTE_LOG_PATH, message)

def _write_log(path, message):
    """
    Internal helper to write log messages to a file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as log_file:
        log_file.write(message)
