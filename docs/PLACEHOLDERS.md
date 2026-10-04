# Placeholder Guide

`.env`
- `LLM_API_KEY`: your selected LLM provider key
- `LLM_MODEL`: model name
- `META_GRAPH_API_VERSION`: currently supported Meta Graph API version
- `INSTAGRAM_USER_ID`: Instagram Professional account ID
- `META_ACCESS_TOKEN`: appropriate Meta access token
- `PUBLIC_IMAGE_URL`: public URL of the image
- `DRY_RUN`: true for testing, false only after production verification

`content/business_context.txt`
- Replace business name
- Add actual course names
- Add your real audience
- Add approved claims
- Add your preferred CTA

Image pipeline:
LLM -> image generation -> upload to public storage/CDN -> PUBLIC_IMAGE_URL -> Meta API

Do not put secrets in Python files or GitHub.
