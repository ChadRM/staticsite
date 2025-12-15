from textnode import TextNode,TextType,text_node_to_html_node

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
        else: 
            new_nodes = node.text.split(delimiter)
            thisnodelist = []
            if len(new_nodes) > 1:
                thisnodelist.append(TextNode(new_nodes[0],TextType.TEXT))
                thisnodelist.append(TextNode(new_nodes[1],text_type))
                if len(new_nodes) > 2:
                    thisnodelist.append(TextNode(new_nodes[2],TextType.TEXT))
            output.extend(thisnodelist)
    return output