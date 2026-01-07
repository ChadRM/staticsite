import unittest
from textnode import TextNode, TextType
from inline_markdown import split_nodes_link

class TestSplitNodeLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link in it](https://i.imgur.com) and another [silly link](https://i.imgur.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("link in it", TextType.LINK, "https://i.imgur.com"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode(
                        "silly link", TextType.LINK, "https://i.imgur.com"
                    ),
                ],
            new_nodes,
        )


if __name__ == '__main__':
    unittest.main()
