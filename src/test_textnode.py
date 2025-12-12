import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This is a text node",TextType.BOLD,"http://hasurl.com")
        node2 = TextNode("This is a text node",TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_print(self):
        node = TextNode("This node has no URL",TextType.ITALIC)
        self.assertEqual(node.__repr__(),"TextNode(This node has no URL, italic)")

if __name__ == "__main__":
    unittest.main()