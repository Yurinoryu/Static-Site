import unittest
from extractors import *

class TestExtractMarkdownFunctions(unittest.TestCase):

    def test_extract_images_basic(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_images_multiple(self):
        text = "![a](url1) text ![b](url2)"
        expected = [("a", "url1"), ("b", "url2")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_links_basic(self):
        text = "Check [this](http://example.com)"
        expected = [("this", "http://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_extract_links_multiple(self):
        text = "[one](url1) and [two](url2)"
        expected = [("one", "url1"), ("two", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_no_matches(self):
        text = "This has no markdown links or images."
        self.assertEqual(extract_markdown_links(text), [])
        self.assertEqual(extract_markdown_images(text), [])

    def test_ignore_image_links_in_link_extraction(self):
        text = "![not this](image.png) and [but this](page.html)"
        expected = [("but this", "page.html")]
        self.assertEqual(extract_markdown_links(text), expected)

if __name__ == "__main__":
    unittest.main()
