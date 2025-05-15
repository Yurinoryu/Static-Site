import unittest
from textnode import *
from text_splitter import *

class TestSplitNodeDelimiter(unittest.TestCase):

    def test_single_code_block(self):
        node = TextNode("Here is 'code' text", TextType.TEXT)
        result = split_nodes_delimiter([node], "'", TextType.CODE)
        expected = [
                TextNode("Here is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" text", TextType.TEXT)
                ]
        
        self.assertEqual(result, expected)

    def test_multiple_code_blocks(self):
        node = TextNode("'a' and 'b'", TextType.TEXT)
        result = split_nodes_delimiter([node], "'", TextType.CODE)
        expected = [
                TextNode("a", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("b", TextType.CODE)
                ]
        
        self.assertEqual(result, expected)

    def test_italic_text(self):
        node = TextNode("This _is_ italic", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
                TextNode("This ", TextType.TEXT),
                TextNode("is", TextType.ITALIC),
                TextNode(" italic", TextType.TEXT)
                ]
        
        self.assertEqual(result, expected)

    def test_bold_text(self):
        node = TextNode("Some **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
                TextNode("Some ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
                ]
        self.assertEqual(result, expected)

    def test_mixed_node_types(self):
        nodes = [
                TextNode("Hello _world_!", TextType.TEXT),
                TextNode("Not parsed", TextType.CODE)
                ]
        result = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
        expected = [
                TextNode("Hello ", TextType.TEXT),
                TextNode("world", TextType.ITALIC),
                TextNode("!", TextType.TEXT),
                TextNode("Not parsed", TextType.CODE)
                ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("Unmatched 'code block", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "'", TextType.CODE)

if __name__ == "__main__":
    unittest.main()
