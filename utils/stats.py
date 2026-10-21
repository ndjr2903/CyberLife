import json
import os

STATS_FILE = "stats.json"

def update_stats(method, file_type):
    """
    Update encryption statistics by method and file type.
    Example key: 'aes_pdf' or 'hybrid_txt'
    """
    stats = {}

    # Load existing stats if file exists
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, "r", encoding="utf-8") as f:
                stats = json.load(f)
        except json.JSONDecodeError:
            print("⚠️ Stats file is corrupted. Starting fresh.")
        except Exception as e:
            print(f"❌ Failed to read stats file: {e}")

    # Normalize key
    method = method.strip().lower()
    file_type = file_type.strip().lower()
    key = f"{method}_{file_type}"

    # Update count
    stats[key] = stats.get(key, 0) + 1

    # Save updated stats
    try:
        with open(STATS_FILE, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=4)
        print(f"📊 Stats updated: {key} → {stats[key]}")
    except Exception as e:
        print(f"❌ Failed to update stats: {e}")
