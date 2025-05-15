import unittest
from textnode import *
from text_parser import *

class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = (
                "This is **text** with an _italic_ word and a 'code block' and an "
                "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a "
                "[link](https://boot.dev)"
                )

        expected = [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev")
                ]
        result = text_to_textnodes(text)
        self.assertEqual(result, expected)


    def test_text_only(self):
        text = "Just plain text."
        expected = [TextNode("Just plain text.", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_mixed_inline_order(self):
        text = "**bold** and 'code' and _italic_"
        expected = [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                ]
        self.assertEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
    unittest.main()


