from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag, children,props = {}):
        super().__init__(tag=tag,value=None,children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("parents must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("parents must have children")
        output = f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"
        return output
    
