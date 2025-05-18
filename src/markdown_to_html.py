from blocktype import *
from block_dectect import *
from markdown_block_splitter import *
from text_parser import *
from html_converters import *
from htmlnode import *
from textnode import *

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            paragraph_text = " ".join(block.splitlines()).strip()
            children.append(ParentNode("p", children=text_to_children(paragraph_text)))

        elif block_type == BlockType.HEADING:
            level = len(block.split(" ")[0])
            text = block[level:].lstrip()
            children.append(ParentNode(f"h{level}", children=text_to_children(text.strip())))

        elif block_type == BlockType.CODE:
            code_text = "\n".join(block.split("\n")[1:-1]) + "\n" # removes ``` lines
            code_node = LeafNode("code", code_text)
            children.append(ParentNode("pre", children=[code_node]))

        elif block_type == BlockType.QUOTE:
            quote_lines = [line[1:].strip() for line in block.split("\n")]
            quote_text = " ".join(quote_lines)
            children.append(ParentNode("blockquote", children=text_to_children(quote_text)))

        elif block_type == BlockType.UNORDERED_LIST:
            items = [line[2:].strip() for line in block.split("\n")]
            li_nodes = [ParentNode("li", children=text_to_children(item)) for item in items]
            children.append(ParentNode("ul", children=li_nodes))

        elif block_type == BlockType.ORDERED_LIST:
            items = [line[line.find(".")+2:].strip() for line in block.split("\n")]
            li_nodes = [ParentNode("li", children=text_to_children(item)) for item in items]
            children.append(ParentNode("ol", children=li_nodes))

    return ParentNode("div", children=children)

def extract_title(markdown: str) -> str:
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No H1 header found")
