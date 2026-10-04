# Hermes Agent + Instagram Daily Automation

Windows + VS Code starter project for an EdTech Instagram content pipeline.

Workflow:
Windows Task Scheduler -> run_daily.py -> generate post -> save draft -> (optional) Meta Graph API -> Instagram

The project starts with DRY_RUN=true, so it will not publish anything.

## 1. Install Hermes

PowerShell:

    iex (irm https://hermes-agent.nousresearch.com/install.ps1)

Open a new terminal:

    hermes --version
    hermes doctor
    hermes setup

Optional quick setup:

    hermes setup --portal

Official docs:
https://hermes-agent.nousresearch.com/docs/getting-started/installation
https://hermes-agent.nousresearch.com/docs/getting-started/quickstart

## 2. Setup this project

Open this folder in VS Code.

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

Copy `.env.example` to `.env` and replace placeholders.

## 3. Configure business content

Edit:

    content/business_context.txt

This controls your audience, topics, tone and CTA.

## 4. Test

Run:

    python run_daily.py

With DRY_RUN=true it creates a post in `generated/` and prints the caption.

If no LLM key is configured, the included demo generator proves the complete workflow without requiring an API.

## 5. Real Instagram publishing

The publisher uses the Meta Graph API two-step image publishing pattern:
1. Create a media container.
2. Publish the container.

Configure in `.env`:

    META_GRAPH_API_VERSION=vXX.X
    INSTAGRAM_USER_ID=YOUR_INSTAGRAM_USER_ID
    META_ACCESS_TOKEN=YOUR_LONG_LIVED_ACCESS_TOKEN
    PUBLIC_IMAGE_URL=https://YOUR-PUBLIC-HOST/image.jpg
    DRY_RUN=false

The image URL must be publicly reachable by Meta. A local Windows path will not work.

Use an appropriate Instagram Professional account and Meta developer/API setup. Verify the currently supported Graph API version and permissions in Meta's official documentation before production use.

## 6. Daily scheduling

Use Windows Task Scheduler:
- Trigger: Daily
- Program: `C:\PATH\hermes_instagram_daily\.venv\Scripts\python.exe`
- Arguments: `run_daily.py`
- Start in: `C:\PATH\hermes_instagram_daily`
- Suggested time: 09:00

Keep DRY_RUN=true until everything is tested.

## 7. Hermes skill

A reusable skill is included at:

    hermes_skills/instagram_content/SKILL.md

It tells Hermes how to create educational Instagram content and avoid unsupported claims.

## 8. Important placeholders

Replace:
- YOUR_EDTECH_NAME
- YOUR_LLM_API_KEY
- YOUR_MODEL_NAME
- YOUR_INSTAGRAM_USER_ID
- YOUR_LONG_LIVED_ACCESS_TOKEN
- vXX.X
- https://YOUR-PUBLIC-HOST/image.jpg

Never commit `.env` to GitHub.

## Recommended production upgrades

- Human approval through Telegram/WhatsApp before publishing
- AI image generation
- Upload images to S3/R2/Cloudinary or another public object store
- Google Sheets/database for content history
- Analytics collection
- LinkedIn/Facebook publishing
