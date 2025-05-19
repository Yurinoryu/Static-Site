from textnode import TextNode, TextType
import os
import shutil
from markdown_to_html import *
import sys


def main():
    node = TextNode("Hello, world!", TextType.TEXT)
    print(node)

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    current_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(current_dir, ".."))
    static_dir = os.path.join(root_dir, "static")
    docs_dir = os.path.join(root_dir, "docs")
    content_dir = os.path.join(root_dir, "content")
    template_path = os.path.join(root_dir, "template.html")
    

    copy_static(static_dir, docs_dir)
    generate_pages_recursive(content_dir, template_path, docs_dir, base_path)

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
        print(f"Deleted existing directory: {dest_dir}")

    os.makedirs(dest_dir)
    print(f"Created directory: {dest_dir}")

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isdir(source_path):
            copy_static(source_path, dest_path)
        else:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy(source_path, dest_path)
            print(f"Copied file: {source_path} -> {dest_path}")


def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown= f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    content_html = html_node.to_html()
    title = extract_title(markdown)

    output = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html)

    output = output.replace('href="/', f'href="{base_path}')
    output = output.replace('src="/', f'src="{base_path}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    for root, _, files in os.walk(dir_path_content):
        for file in files:
            if file.endswith(".md"):
                from_path = os.path.join(root, file)

                relative_path = os.path.relpath(from_path, dir_path_content)
                relative_html = os.path.splitext(relative_path)[0] + ".html"
                dest_path = os.path.join(dest_dir_path, relative_html)

                print(f"Generating page from {from_path} to {dest_path} using {template_path}")
                generate_page(from_path, template_path, dest_path, base_path)

if __name__ == "__main__":
    main()
