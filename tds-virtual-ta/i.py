from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")
    image_data = data.get("image", None)

    # Dummy response for now
    return jsonify({
        "answer": f"Received your question: '{question}'",
        "links": [
            {"url": "https://example.com", "text": "Sample link 1"},
            {"url": "https://example.com", "text": "Sample link 2"}
        ]
    })
