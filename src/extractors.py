import re

def extract_markdown_images(text):
    # Matches: ![alt](url)
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    # Matches: [Text](url) but NOT ![alt](url)
    pattern = r"(?<!!)\[([^\]]+)\]\(([^)]+)\)"
    return re.findall(pattern, text)
