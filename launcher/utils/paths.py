from pathlib import Path

APP_NAME = "GameLauncher"
ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data"
ASSETS_DIR = ROOT / "launcher" / "assets"
ICONS_DIR = ASSETS_DIR / "icons"

DATA_DIR.mkdir(exist_ok=True, parents=True)
ASSETS_DIR.mkdir(exist_ok=True, parents=True)
ICONS_DIR.mkdir(exist_ok=True, parents=True)
