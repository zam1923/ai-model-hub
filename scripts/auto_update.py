import os
import json
import feedparser
import yaml
import google.generativeai as genai
from datetime import datetime

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# We will use Gemini 1.5 Flash for the reporter task
model = genai.GenerativeModel('gemini-1.5-flash')

def fetch_arxiv_cs_ai():
    """Fetch recent papers from arXiv cs.AI."""
    print("Fetching arXiv cs.AI...")
    url = 'http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=5'
    feed = feedparser.parse(url)
    return feed.entries

def generate_markdown_content(entry):
    """Use Gemini to act as a senior tech journalist and write high-quality articles."""

    prompt = f"""
    You are a Senior Tech Journalist writing for a premium Japanese tech publication (like Wired or TechCrunch).
    Your task is to analyze the following academic paper/announcement and write a deep-dive, professional article about it.

    SOURCE INFO:
    Title: {entry.title}
    Authors: {', '.join([author.name for author in entry.authors])}
    Published: {entry.published}
    Link: {entry.link}
    Abstract: {entry.summary}

    Instructions:
    1. Determine if this paper introduces a significant AI Model, Lab, or Researcher. If it is minor or purely theoretical without a distinct entity to profile, return an empty JSON object: {{}}.
    2. Write a highly engaging, factual, and analytical article (1000+ Japanese characters) for the `body` field. Do not invent facts; base your analysis on the provided abstract but write it like a professional news feature.
    3. Include `sourceUrl` (the Link provided) and `sourceTitle` (the Title provided).
    4. Choose an `image_category` from: "abstract", "datacenter", "robotics", "office", "code".

    Output strictly as a JSON object with this structure (no markdown blocks, just raw JSON):
    {{
      "model": {{
        "id": "slug-format-model-name",
        "title": "Model Name",
        "lab": "Lab Name",
        "releaseDate": "YYYY-MM-DD",
        "contextWindow": "Unknown",
        "license": "Unknown",
        "description": "Catchy, professional 1-sentence summary.",
        "paperUrl": "{entry.link}",
        "sourceUrl": "{entry.link}",
        "sourceTitle": "論文: {entry.title}",
        "modalities": ["Text"],
        "image_category": "abstract",
        "body": "Journalistic deep-dive article (1000+ chars)..."
      }}
    }}
    """

    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if text.startswith('```json'):
            text = text[7:-3].strip()

        data = json.loads(text)
        return data
    except Exception as e:
        print(f"Error generating content via Gemini: {e}")
        return {}

IMAGE_MAP = {
    "abstract": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=800&auto=format&fit=crop",
    "datacenter": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=800&auto=format&fit=crop",
    "robotics": "https://images.unsplash.com/photo-1680868543815-b8666dba60f7?q=80&w=800&auto=format&fit=crop",
    "office": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=800&auto=format&fit=crop",
    "code": "https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=800&auto=format&fit=crop"
}

def save_markdown(directory, id, frontmatter, body=""):
    # Map image category to URL
    if "image_category" in frontmatter:
        cat = frontmatter.pop("image_category")
        frontmatter["image"] = IMAGE_MAP.get(cat, IMAGE_MAP["abstract"])

    filepath = f"src/content/{directory}/{id}.md"

    # Check if exists
    if os.path.exists(filepath):
        print(f"Skipping {filepath} (Already exists)")
        return False

    os.makedirs(f"src/content/{directory}", exist_ok=True)

    if 'releaseDate' in frontmatter and isinstance(frontmatter['releaseDate'], str):
        try:
             parsed_date = datetime.strptime(frontmatter['releaseDate'], '%Y-%m-%d').date()
             frontmatter['releaseDate'] = parsed_date
        except Exception:
             pass

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("---\n")
        yaml.dump(frontmatter, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        f.write("---\n\n")
        f.write(body)

    print(f"Created {filepath}")
    return True

def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("GEMINI_API_KEY is not set. Exiting.")
        return

    entries = fetch_arxiv_cs_ai()

    for entry in entries:
        print(f"Processing: {entry.title}")
        data = generate_markdown_content(entry)

        if not data or 'model' not in data:
            print("No suitable entity extracted, skipping.")
            continue

        model_data = data['model']

        model_id = model_data.pop('id', 'unknown-model')
        model_body = model_data.pop('body', f"詳細は提供されていません。")
        save_markdown('models', model_id, model_data, model_body)

if __name__ == "__main__":
    main()
