import unittest
from markdown_to_html import *

class TestMarkDownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

    def test_codeblock(self):
        md = """```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
                )

    def test_heading(self):
        md = "# Hello World"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><h1>Hello World</h1></div>"
                )

    def test_blockquote(self):
        md = "> This is a quote\n> across multiple lines"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><blockquote>This is a quote across multiple lines</blockquote></div>"
                )

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
                )

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
                html,
                "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>"
                )

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
        self.assertEqual(extract_title("#  Hello World  "), "Hello World")

    def test_missing_title(self):
        with self.assertRaises(Exception):
            exract_title("## Not a valid title\nText")


if __name__ == "__main__":
    unittest.main()
