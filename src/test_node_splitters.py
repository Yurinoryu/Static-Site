import unittest
from textnode import TextNode, TextType
from node_splitters import split_nodes_image, split_nodes_link


class TestNodeSplitters(unittest.TestCase):

    def test_split_images(self):
        node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,)
        result = split_nodes_image([node])
        expected = [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                ]
        self.assertEqual(result, expected)

    def test_split_links(self):
        node = TextNode("Click [Google](https://www.google.com) or [GitHub](https://github.com)", TextType.TEXT,)
        result = split_nodes_link([node])
        expected = [
                TextNode("Click ", TextType.TEXT),
                TextNode("Google", TextType.LINK, "https://www.google.com"),
                TextNode(" or ", TextType.TEXT),
                TextNode("GitHub", TextType.LINK, "https://github.com"),
                ]
        self.assertEqual(result, expected)

    def test_split_no_links(self):
        node = TextNode("No links here!", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), [node])

    def test_split_no_images(self):
        node = TextNode("Just plain text.", TextType.TEXT)
        self.assertEqual(split_nodes_image([node]), [node])

    def test_ignores_non_text_nodes(self):
        node = TextNode("Should stay untouched", TextType.BOLD)
        self.assertEqual(split_nodes_link([node]), [node])
        self.assertEqual(split_nodes_image([node]), [node])

if __name__ == "__main__":
    unittest.main()

