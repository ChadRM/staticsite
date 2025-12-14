import unittest
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html2(self):
        node = LeafNode("i", "This is italics")
        self.assertEqual(node.to_html(),"<i>This is italics</i>")
    
    def test_leaf_no_child(self):
        node = LeafNode("a","random anchor text")
        self.assertIsNone(node.children)


if __name__ == "__main__":
    unittest.main()