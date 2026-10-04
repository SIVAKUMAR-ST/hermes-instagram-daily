from dataclasses import dataclass
from pathlib import Path
import os
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")

@dataclass
class Settings:
    dry_run: bool = os.getenv("DRY_RUN", "true").lower() == "true"
    llm_api_key: str = os.getenv("LLM_API_KEY", "")
    llm_model: str = os.getenv("LLM_MODEL", "")
    meta_graph_api_version: str = os.getenv("META_GRAPH_API_VERSION", "vXX.X")
    instagram_user_id: str = os.getenv("INSTAGRAM_USER_ID", "")
    meta_access_token: str = os.getenv("META_ACCESS_TOKEN", "")
    public_image_url: str = os.getenv("PUBLIC_IMAGE_URL", "")

settings = Settings()
