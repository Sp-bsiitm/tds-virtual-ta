from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load the course content
with open("data/course_content.json", encoding="utf-8") as f:
    course_data = json.load(f)

# Load the Discourse posts
try:
    with open("data/discourse_posts.json", encoding="utf-8") as f:
        discourse_data = json.load(f)
except FileNotFoundError:
    discourse_data = []

@app.route("/ask", methods=["POST"])
def ask():
    query = request.json.get("query", "").lower()
    results = []

    # Search course content
    for item in course_data:
        if query in item["content"].lower():
            results.append({
                "source": "course",
                "title": item["title"],
                "link": f"https://tds.s-anand.net/#/2025-01/{item['filename'].replace('.md', '')}"
            })

    # Search Discourse
    for item in discourse_data:
        if query in item.get("content", "").lower():
            results.append({
                "source": "discourse",
                "title": item.get("title", ""),
                "link": f"https://discourse.onlinedegree.iitm.ac.in/t/{item['slug']}"
            })

    answer = "Here are some relevant links." if results else "No relevant content found."
    links = [r["link"] for r in results]

    return jsonify({"answer": answer, "links": links})


if __name__ == "__main__":
    app.run(port=5050, debug=True)
    