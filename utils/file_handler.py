import mimetypes
import os

# Supported file extensions
SUPPORTED_EXTENSIONS = [".jpg", ".png", ".pdf", ".docx", ".txt", ".xlsx"]

# Sensitive keywords to scan for
SENSITIVE_KEYWORDS = ["password", "id", "secret", "confidential", "private", "token", "key"]

def is_supported_file(filename):
    """
    Check if the file has a supported extension or MIME type.
    """
    extension = os.path.splitext(filename)[1].lower()
    mime_type, _ = mimetypes.guess_type(filename)
    return extension in SUPPORTED_EXTENSIONS or (mime_type and mime_type.startswith(("text", "application")))

def is_sensitive(filename):
    """
    Check if the filename or file content contains sensitive keywords.
    """
    # Check filename itself
    if any(word in filename.lower() for word in SENSITIVE_KEYWORDS):
        return True

    # Try reading file content
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
            return any(word in content for word in SENSITIVE_KEYWORDS)
    except Exception:
        return False

