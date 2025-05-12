import json
import os
from datetime import datetime
from typing import Any, Dict, List


def get_latest_file(storage_path: str) -> str:
    """Find the latest JSON file"""
    files = os.listdir(storage_path)
    json_files = [f for f in files if f.endswith(".json")]
    if not json_files:
        print("No JSON files found in", storage_path)
        return None

    json_files.sort()
    latest_file = os.path.join(storage_path, json_files[-1])
    return latest_file


def load_articles(storage_path: str, max_articles: int = 20) -> List[Dict[str, Any]]:
    """Load and parse the articles from the latest arxiv JSON file"""
    if file_path := get_latest_file(storage_path):
        try:
            with open(file_path, "r") as f:
                print(f"Loading articles from {file_path}")
                articles = json.load(f)
                return articles[:max_articles]

        except Exception as e:
            print(f"Error loading articles: {e}")

    # If no file is found, return an empty list
    return []


def format_date(date_str: str) -> str:
    """Format the date string to a more readable format"""
    try:
        dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
        return dt.strftime("%B %d, %Y")
    except Exception as e:
        print(f"Error formatting date: {e}")
        return date_str


def format_article(article) -> str:
    """Format article content for display"""
    title = article.get("title", "No Title")
    authors = ", ".join(article.get("authors", ["Unknown"]))
    abstract = article.get("abstract", "No abstract available")
    published = format_date(article.get("published", ""))
    url = article.get("url", "#")

    return (
        f"## [{title}]({url}) \n\n"
        f"**Authors:** {authors} \n\n"
        f"**Published:** {published} \n\n"
        f"{abstract} \n\n"
        "---"
    )
