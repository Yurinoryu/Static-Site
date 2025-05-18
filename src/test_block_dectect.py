import unittest
from block_dectect import *

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)

    def test_code_block(self):
        code = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote_block(self):
        quote = "> This is a quote\n> with multiple lines"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- Item 1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_incorrect_ordered_list(self):
        ol = "1. First\n3. Wrong number"
        self.assertEqual(block_to_block_type(ol), BlockType.PARAGRAPH)

    def test_paragraph(self):
        para = "This is just a normal paragraph with no special formatting."
        self.assertEqual(block_to_block_type(para), BlockType.PARAGRAPH)

    def test_heading_with_no_space(self):
        bad_heading = "##Heading without space"
        self.assertEqual(block_to_block_type(bad_heading), BlockType.PARAGRAPH)

    def test_quote_partial_lines(self):
        mixed_quote = "> A proper quote line\nNot a quote"
        self.assertEqual(block_to_block_type(mixed_quote), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
