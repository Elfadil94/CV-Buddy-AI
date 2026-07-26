import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PROFILE_FILE = DATA_DIR / "profile.json"
CHAT_FILE = DATA_DIR / "chat.json"


def save_json(path: Path, data):

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_json(path: Path):

    if not path.exists():
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def clear_storage():

    if PROFILE_FILE.exists():
        PROFILE_FILE.unlink()

    if CHAT_FILE.exists():
        CHAT_FILE.unlink()