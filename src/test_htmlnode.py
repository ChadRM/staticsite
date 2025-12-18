import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_create1(self):
        node = HTMLNode("a","anchor",props={"target":"_blank"})
        self.assertEqual(node.props["target"],"_blank")
    
    def test_create2(self):
        node = HTMLNode("html","hello world")
        self.assertEqual(node.tag,"html")
    
    def test_props_to_html(self):
        node = HTMLNode("a","anchor", props={"target":"_blank","href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' target="_blank" href="https://www.google.com" ')




if __name__ == "__main__":
    unittest.main()