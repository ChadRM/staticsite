from textnode import TextNode,TextType
from extract_markdown import extract_markdown_images, extract_markdown_links


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

def split_nodes_image(old_nodes):
    output = []
    for image in old_nodes:
        if image.text_type != TextType.TEXT:
            output.append(image)
        else:
            matches = extract_markdown_images(image.text)
            match = matches[0]
            splitter = f"![{match[0]}]({match[1]})"
            print(splitter)
            new_nodes = image.text.split(splitter,1)
            print(new_nodes)
            if new_nodes[0] != "":
                output.append(TextNode(new_nodes[0],TextType.TEXT))
            output.append(TextNode(match[0],TextType.IMAGE,match[1]))
            if new_nodes[1] != "":
                output.extend(split_nodes_image([TextNode(new_nodes[1],TextType.TEXT)]))
    return output

def split_nodes_link(old_nodes):
    output = []
    for link in old_nodes:
        if link.text_type != TextType.TEXT:
            output.append(link)
        else:
            matches = extract_markdown_links(link.text)
            match = matches[0]
            splitter = f"[{match[0]}]({match[1]})"
            print(splitter)
            new_nodes = link.text.split(splitter,1)
            print(new_nodes)
            if new_nodes[0] != "":
                output.append(TextNode(new_nodes[0],TextType.TEXT))
            output.append(TextNode(match[0],TextType.LINK,match[1]))
            if new_nodes[1] != "":
                output.extend(split_nodes_link([TextNode(new_nodes[1],TextType.TEXT)]))
    return output
