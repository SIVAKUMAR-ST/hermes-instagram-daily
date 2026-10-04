import json
import logging
from datetime import datetime
from src.config import ROOT, settings
from src.content_generator import generate_post, write_post, load_history, save_history
from src.instagram_publisher import publish_to_instagram

(ROOT / "logs").mkdir(exist_ok=True)
logging.basicConfig(
    filename=ROOT / "logs" / "automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

def main():
    logging.info("Starting daily Instagram workflow")
    post = generate_post()
    output_file = write_post(post)

    caption = (
        f"{post['hook']}\n\n{post['caption']}\n\n"
        f"{post['cta']}\n\n{' '.join(post['hashtags'])}"
    )

    if settings.dry_run:
        print("\nDRY RUN - NOTHING WILL BE PUBLISHED\n")
        print(caption)
        print(f"\nSaved to: {output_file}")
        logging.info("Dry run completed")
        return

    result = publish_to_instagram(caption)
    print("Instagram publish result:")
    print(json.dumps(result, indent=2))

    history = load_history()
    history.append({
        "topic": post["topic"],
        "published_at": datetime.now().isoformat(),
        "status": "published"
    })
    save_history(history)
    logging.info("Published topic: %s", post["topic"])

if __name__ == "__main__":
    main()
