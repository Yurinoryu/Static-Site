import re
from textnode import *


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
        last_index = 0

        for match in re.finditer(pattern, text):
            start, end = match.span()
            alt_text, url = match.groups()

            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            last_index = end

        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        pattern = r"(?<!!)\[([^\]]+)\]\(([^)]+)\)"
        last_index = 0

        for match in re.finditer(pattern, text):
            start, end = match.span()
            anchor_text, url = match.groups()

            if start > last_index:
                new_nodes.append(TextNode(text[last_index:start], TextType.TEXT))

            new_nodes.append(TextNode(anchor_text, TextType.LINK, url))
            last_index = end

        if last_index < len(text):
            new_nodes.append(TextNode(text[last_index:], TextType.TEXT))

    return new_nodes
