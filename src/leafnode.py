from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props={}):
        super().__init__(tag=tag,value=value,children=None,props=props)

    def to_html(self):
        if self.value is None or self.value == "":
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None or self.tag == "":
            return self.value
        return f"<{self.tag}>{self.value}</{self.tag}>"