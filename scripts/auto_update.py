import os
import json
import feedparser
import yaml
import google.generativeai as genai
from datetime import datetime

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# We'll use a cheaper/faster model for basic extraction
model = genai.GenerativeModel('gemini-2.5-flash')

def fetch_arxiv_cs_ai():
    """Fetch recent papers from arXiv cs.AI."""
    print("Fetching arXiv cs.AI...")
    url = 'http://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=5'
    feed = feedparser.parse(url)
    return feed.entries

def generate_markdown_content(entry):
    """Use Gemini to extract info and generate markdown for models, labs, and researchers."""

    prompt = f"""
    You are an AI assistant helping to maintain a Japanese AI Information Catalog.
    Read the following abstract of an AI research paper/announcement and extract information about the primary AI Model, the Lab/Organization, and the main Researchers.

    Title: {entry.title}
    Authors: {', '.join([author.name for author in entry.authors])}
    Published: {entry.published}
    Link: {entry.link}
    Abstract: {entry.summary}

    Instructions:
    1. If a distinct AI Model is NOT introduced or discussed as the main topic, return an empty JSON object: {{}}.
    2. If a model IS introduced, generate structured data for the model, its lab, and its top 2 authors.
    3. Translate descriptions into professional Japanese.

    Output strictly as a JSON object with this structure (no markdown blocks, just raw JSON):
    {{
      "model": {{
        "id": "slug-format-model-name",
        "title": "Model Name",
        "lab": "Lab Name",
        "releaseDate": "YYYY-MM-DD",
        "contextWindow": "Unknown",
        "license": "Unknown",
        "description": "Short Japanese description (1-2 sentences)",
        "paperUrl": "URL",
        "modalities": ["Text"],
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=800&auto=format&fit=crop"
      }},
      "lab": {{
        "id": "slug-format-lab-name",
        "name": "Lab Name",
        "location": "Global",
        "description": "Short Japanese description of the lab",
        "image": "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=800&auto=format&fit=crop"
      }},
      "researchers": [
        {{
          "id": "slug-format-researcher-name",
          "name": "Researcher Name",
          "lab": "Lab Name",
          "role": "Researcher",
          "famousFor": "Mention this paper in Japanese",
          "image": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?q=80&w=800&auto=format&fit=crop",
          "links": {{ "scholar": "URL" }}
        }}
      ]
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

def save_markdown(directory, id, frontmatter, body=""):
    """Save data as a markdown file."""
    filepath = f"src/content/{directory}/{id}.md"

    # Don't overwrite if exists to prevent zero-touch from destroying manual edits,
    if os.path.exists(filepath):
        print(f"Skipping {filepath} (Already exists)")
        return False

    os.makedirs(f"src/content/{directory}", exist_ok=True)

    # Clean up dates for YAML serialization if needed, although PyYAML handles standard objects better
    # But since Astro's schema expects a Date for `releaseDate`, we can parse it first so PyYAML dumps it correctly.
    if 'releaseDate' in frontmatter and isinstance(frontmatter['releaseDate'], str):
        try:
             # Just leave it as a string that looks like a date, PyYAML handles unquoted dates, but explicit parsing is safer
             parsed_date = datetime.strptime(frontmatter['releaseDate'], '%Y-%m-%d').date()
             frontmatter['releaseDate'] = parsed_date
        except Exception:
             pass


    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("---\n")
        # Dump using yaml, allow_unicode ensures Japanese text isn't escaped
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
            print("No model extracted, skipping.")
            continue

        model_data = data['model']
        lab_data = data.get('lab')
        researchers_data = data.get('researchers', [])

        # Save Model
        model_id = model_data.pop('id')
        save_markdown('models', model_id, model_data, f"{model_data['title']}の詳細情報です。")

        # Save Lab
        if lab_data:
            lab_id = lab_data.pop('id')
            save_markdown('labs', lab_id, lab_data, f"{lab_data['name']}の概要です。")

        # Save Researchers
        for res_data in researchers_data:
            res_id = res_data.pop('id')
            save_markdown('researchers', res_id, res_data, f"{res_data['name']}のプロフィールです。")

if __name__ == "__main__":
    main()
