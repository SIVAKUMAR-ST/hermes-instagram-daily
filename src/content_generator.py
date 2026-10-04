import json
from pathlib import Path
from datetime import datetime, timezone
from .config import ROOT, settings

def load_business_context() -> str:
    return (ROOT / "content" / "business_context.txt").read_text(encoding="utf-8")

def load_history() -> list:
    path = ROOT / "data" / "topic_history.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_history(history: list):
    (ROOT / "data" / "topic_history.json").write_text(
        json.dumps(history, indent=2, ensure_ascii=False), encoding="utf-8"
    )

def demo_generate(context: str, history: list) -> dict:
    topics = [
        "5 skills every modern Data Engineer should build",
        "RAG vs fine-tuning: when should you use each?",
        "What is an AI Agent in simple terms?",
        "MCP explained for developers",
        "A practical GenAI project idea for Data Engineers",
        "Why Python alone is not enough for AI Engineering",
        "How Data Engineering changes in the GenAI era",
    ]
    used = {x.get("topic") for x in history if isinstance(x, dict)}
    topic = next((t for t in topics if t not in used), topics[0])
    return {
        "topic": topic,
        "hook": f"Stop learning AI randomly. Start with this: {topic}",
        "caption": (
            f"{topic}\n\n"
            "If you are a working technology professional, focus on practical "
            "skills that you can demonstrate through projects.\n\n"
            "Save this post and use it as a checklist for your next learning sprint."
        ),
        "cta": "Follow for practical AI and Data Engineering content.",
        "hashtags": ["#AI", "#GenerativeAI", "#DataEngineering",
                     "#AIEngineering", "#Python", "#TechCareer"],
        "image_concept": f"Clean professional carousel explaining: {topic}",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "demo"
    }

def generate_post() -> dict:
    context = load_business_context()
    history = load_history()

    # PLACEHOLDER:
    # Connect your preferred LLM here. Recommended prompt:
    # "Using the business context, create ONE Instagram post and return strict JSON
    # with topic, hook, caption, cta, hashtags and image_concept. Do not repeat a
    # topic from history and do not invent claims."
    if not settings.llm_api_key:
        return demo_generate(context, history)

    raise RuntimeError(
        "LLM_API_KEY is set, but no provider adapter is configured. "
        "Add your chosen LLM SDK/API call in generate_post()."
    )

def write_post(post: dict) -> Path:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = ROOT / "generated" / f"instagram_post_{timestamp}.json"
    out.write_text(json.dumps(post, indent=2, ensure_ascii=False), encoding="utf-8")
    return out
