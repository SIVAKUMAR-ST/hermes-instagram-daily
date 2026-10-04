import requests
from .config import settings

def validate_meta_settings():
    missing = []
    if not settings.instagram_user_id or "YOUR_" in settings.instagram_user_id:
        missing.append("INSTAGRAM_USER_ID")
    if not settings.meta_access_token or "YOUR_" in settings.meta_access_token:
        missing.append("META_ACCESS_TOKEN")
    if not settings.public_image_url or "YOUR-" in settings.public_image_url:
        missing.append("PUBLIC_IMAGE_URL")
    if not settings.meta_graph_api_version or "XX" in settings.meta_graph_api_version:
        missing.append("META_GRAPH_API_VERSION")
    if missing:
        raise ValueError("Missing Meta configuration: " + ", ".join(missing))

def publish_to_instagram(caption: str) -> dict:
    # Standard image publishing flow:
    # 1) POST /{ig-user-id}/media
    # 2) POST /{ig-user-id}/media_publish
    # The image_url must be public and fetchable by Meta.
    validate_meta_settings()

    base = f"https://graph.facebook.com/{settings.meta_graph_api_version}"

    create = requests.post(
        f"{base}/{settings.instagram_user_id}/media",
        params={
            "image_url": settings.public_image_url,
            "caption": caption,
            "access_token": settings.meta_access_token,
        },
        timeout=60,
    )
    create.raise_for_status()
    creation_id = create.json().get("id")

    if not creation_id:
        raise RuntimeError(f"Meta did not return a creation id: {create.text}")

    publish = requests.post(
        f"{base}/{settings.instagram_user_id}/media_publish",
        params={
            "creation_id": creation_id,
            "access_token": settings.meta_access_token,
        },
        timeout=60,
    )
    publish.raise_for_status()
    return publish.json()
