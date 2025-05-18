from textnode import *
from node_splitters import *
from text_splitter import *
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # Order matters: code > bold > italic > images > links
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)


    return nodes
