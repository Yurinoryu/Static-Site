import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
        def test_eq(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is a text node", TextType.BOLD)
            self.assertEqual(node, node2)
            
        def test_not_equal_text(self):
            node1 = TextNode("Hello", TextType.TEXT)
            node2 = TextNode("Goodbye", TextType.TEXT)
            self.assertNotEqual(node1, node2)

        def test_not_equal_type(self):
            node1 = TextNode("Some text", TextType.ITALIC)
            node2 = TextNode("Some text", TextType.CODE)
            self.assertNotEqual(node1, node2)

        def test_equal_with_url(self):
            node1 = TextNode("Link", TextType.LINK, "https://example.com")
            node2 = TextNode("Link", TextType.LINK, "https://example.com")
            self.assertEqual(node1, node2)











if __name__ == "__main__":
    unittest.main()
