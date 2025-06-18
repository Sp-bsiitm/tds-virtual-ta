import os
import requests
import json
from datetime import datetime

DISCOURSE_URL = "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34/l/latest.json"

def extract_discourse_posts():
    print("Fetching posts from Discourse…")
    response = requests.get(DISCOURSE_URL)
    data = response.json()

    topics = data.get("topic_list", {}).get("topics", [])

    posts = []

    for topic in topics:
        created_at = topic.get("created_at")
        if not created_at:
            continue

        # Convert created_at to datetime
        created = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")

        # ✅ Filter between Jan 1 and Apr 14, 2025
        if datetime(2025, 1, 1) <= created <= datetime(2025, 4, 14):
            post = {
                "title": topic["title"],
                "id": topic["id"],
                "created_at": created_at,
                "link": f"https://discourse.onlinedegree.iitm.ac.in/t/{topic['slug']}/{topic['id']}"
            }
            posts.append(post)

    # Make sure data folder exists
    os.makedirs("data", exist_ok=True)

    # Save posts to JSON
    with open("data/discourse_posts.json", "w") as f:
        json.dump(posts, f, indent=2)

    print(f"✅ Saved {len(posts)} posts to data/discourse_posts.json")

if __name__ == "__main__":
    extract_discourse_posts()
