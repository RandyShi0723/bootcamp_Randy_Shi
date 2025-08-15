from dotenv import load_dotenv
import os
from pathlib import Path
from typing import Optional

def load_env():
    """
    Load environment variables from a .env file if present.
    """
    load_dotenv()

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    """
    Fetch an environment variable safely.
    """
    return os.getenv(name, default)

# Example project paths
PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"

if __name__ == "__main__":
    # Demo: only runs if you call python src/config.py
    load_env()
    print("PROJECT_ROOT:", PROJECT_ROOT)
    print("DATA_DIR:", DATA_DIR)
    print("API_KEY present:", get_key("API_KEY") is not None)
