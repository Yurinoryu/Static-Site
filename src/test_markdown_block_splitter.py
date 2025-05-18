import unittest
from markdown_block_splitter import *

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_paragraphs_and_list(self):
        md  = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and 'code' here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """

        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and 'code' here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                    ],
                )

    def test_heading_and_paragraph(self):
        md = """
        # Heading

        A paragraph below the heading.
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "# Heading",
                    "A paragraph below the heading.",
                    ],
                )


    def test_excessive_newlines(self):
        md = """


        First block


        Second block


        Third block
        

        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "First block",
                    "Second block",
                    "Third block",
                    ],
                )

    def test_single_block(self):
        md = "Just a single block with no double newlines"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                ["Just a single block with no double newlines"]
                )

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()
