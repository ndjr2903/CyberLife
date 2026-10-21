SUSPICIOUS_KEYWORDS = [
    "payload", "reverse_tcp", "keylogger", "exec", "socket",
    "subprocess", "shellcode", "bind", "inject", "malware"
]

def is_suspicious(file_path):
    try:
        with open(file_path, "r", errors="ignore") as f:
            content = f.read().lower()
            for word in SUSPICIOUS_KEYWORDS:
                if word in content:
                    print(f"🚨 Suspicious keyword detected: {word}")
                    return True
        return False
    except Exception as e:
        print(f"❌ Failed to scan file: {e}")
        return False
