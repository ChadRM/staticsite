import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from split_node_delimiter import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a test with no delimiters.",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**",TextType.TEXT)
        for node in new_nodes:
            self.assertEqual(node.text_type, TextType.TEXT)

    def test_bold(self):
        node = TextNode("This is text with a **bold* word.*",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type,TextType.BOLD)
    
    def test_ends(self):
        node = TextNode("This node ends in **bold**",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type,TextType.BOLD)

    def test_starts(self):
        node = TextNode("**Starts** with bold this time.",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"**",TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type,TextType.BOLD)

    def test_italics(self):
        node = TextNode("This is some _italics_ for you.",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"_",TextType.ITALIC)
        self.assertEqual(new_nodes[1].text_type,TextType.ITALIC)

    def test_code(self):
        node = TextNode("This is some `code` for you.",TextType.TEXT)
        new_nodes = split_nodes_delimiter([node],"`",TextType.CODE)
        self.assertEqual(new_nodes[1].text_type,TextType.CODE)

if __name__ == "__main__":
    unittest.main()