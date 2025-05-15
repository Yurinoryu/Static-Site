import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="a", value="Link", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag="a", value="Link", props={
            "href": "https://google.com",
            "target": "_blank"
            })
        html = node.props_to_html()
        expected_1 = ' href="https://google.com" target="_blank"'
        expected_2 = ' target="_blank" href="https://google.com"'
        self.assertIn(html, (expected_1, expected_2))

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="p", value="Text")
        self.assertEqual(node.props_to_html(), "")

    # LeafNode Tests
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")


    def test_leaf_to_html_a_tag_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag_returns_raw_text(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_raises_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)



    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_mixed_children(self):
        node = ParentNode("p",
                          [
                              LeafNode("b", "Bold text"),
                              LeafNode(None, "Normal text"),
                              LeafNode("i", "italic text"),
                              LeafNode(None, "Normal text"),
                              ],
                              )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_to_html_raises_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "text")])

    def test_to_html_raises_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])



        

if __name__ == "__main__":
    unittest.main()
