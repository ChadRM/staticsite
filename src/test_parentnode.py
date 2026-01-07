import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_great_grandchildren(self):
        great_grandchild_node = LeafNode("b", "grandchild")
        grandchild_node = ParentNode("span",[great_grandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><span><b>grandchild</b></span></span></div>",
        )
    
    def test_parent_no_kids(self):
        sad_child = "Nope"
        parent_node = ParentNode("span",[sad_child])
        self.assertRaises(AttributeError,parent_node.to_html)


if __name__ == "__main__":
    unittest.main()