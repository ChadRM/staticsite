from textnode import TextNode,TextType

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    output = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            output.append(node)
        else: 
            new_nodes = node.text.split(delimiter)
            this_node_list = []
            if len(new_nodes) > 1:
                this_node_list.append(TextNode(new_nodes[0],TextType.TEXT))
                this_node_list.append(TextNode(new_nodes[1],text_type))
                if len(new_nodes) > 2:
                    this_node_list.append(TextNode(new_nodes[2],TextType.TEXT))
            output.extend(this_node_list)
    return output