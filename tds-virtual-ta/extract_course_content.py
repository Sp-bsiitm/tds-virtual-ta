import os
import json

src = "tools-in-data-science-public/2025-01"
output = []

for fname in os.listdir(src):
    if fname.endswith(".md"):
        path = os.path.join(src, fname)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        output.append({
            "filename": fname,
            "title": fname.replace(".md", "").replace("-", " ").title(),
            "content": text
        })

os.makedirs("data", exist_ok=True)
with open("data/course_content.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)

print(f"✅ Extracted {len(output)} files from course content.")

