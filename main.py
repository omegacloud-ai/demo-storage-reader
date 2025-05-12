from typing import List

import gradio as gr

from utils import format_article, load_articles

STORAGE_NAME = "arxiv"
STORAGE_PATH = f"/tmp/{STORAGE_NAME}"
MAX_ARTICLES = 10


def get_articles() -> List[gr.Markdown]:
    """Load and format articles for display"""
    articles = load_articles(STORAGE_PATH, MAX_ARTICLES)
    formatted_atticles = [format_article(article) for article in articles]
    # Pad with empty strings if we have less than MAX_ARTICLES
    formatted_atticles += [""] * (MAX_ARTICLES - len(formatted_atticles))
    return formatted_atticles


def main():
    with gr.Blocks(theme=gr.themes.Soft()) as app:
        # Add a title
        gr.Markdown("# ArXiv Paper Explorer")

        # Create a placeholder for articles
        with gr.Group():
            articles_placeholer = [gr.Markdown() for _ in range(MAX_ARTICLES)]

        # Load and format articles when the page is opened
        app.load(get_articles, outputs=articles_placeholer)

        # Launch the app
        app.launch()


if __name__ == "__main__":
    main()
