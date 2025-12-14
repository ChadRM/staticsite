from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag, value, props={}):
        super().__init__(self,tag,value,props=props)

    def to_html():
        if self.value == None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{tag}>{self.value}</{tag}>"