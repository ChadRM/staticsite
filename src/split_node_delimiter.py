from inline_markdown import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
from block import markdown_to_blocks


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    from htmlnode import ParentNode
    from textnode import text_node_to_html_node, TextNode, TextType
    from block import block_to_block_type, BlockType

    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            # Join lines with a space to handle multi-line paragraphs in markdown
            lines = block.split("\n")
            paragraph_text = " ".join([line.strip() for line in lines])
            
            text_nodes = [TextNode(paragraph_text, TextType.TEXT)]
            text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
            text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
            text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
            text_nodes = split_nodes_image(text_nodes)
            text_nodes = split_nodes_link(text_nodes)

            html_nodes = [text_node_to_html_node(node) for node in text_nodes]
            children.append(ParentNode("p", html_nodes))

        elif block_type == BlockType.HEADING:
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            text = block[level:].strip()
            text_nodes = [TextNode(text, TextType.TEXT)]
            text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
            text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
            text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
            text_nodes = split_nodes_image(text_nodes)
            text_nodes = split_nodes_link(text_nodes)

            html_nodes = [text_node_to_html_node(node) for node in text_nodes]
            children.append(ParentNode(f"h{level}", html_nodes))

        elif block_type == BlockType.CODE:
            text = block[3:-3]
            text_nodes = [TextNode(text, TextType.CODE)]
            html_nodes = [text_node_to_html_node(node) for node in text_nodes]
            children.append(ParentNode("pre", [ParentNode("code", html_nodes)]))

        elif block_type == BlockType.QUOTE:
            lines = block.split("\n")
            text = " ".join([line[1:].strip() for line in lines])
            text_nodes = [TextNode(text, TextType.TEXT)]
            text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
            text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
            text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
            text_nodes = split_nodes_image(text_nodes)
            text_nodes = split_nodes_link(text_nodes)

            html_nodes = [text_node_to_html_node(node) for node in text_nodes]
            children.append(ParentNode("blockquote", html_nodes))

        elif block_type == BlockType.UNORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                text = line[2:]
                text_nodes = [TextNode(text, TextType.TEXT)]
                text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
                text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
                text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
                text_nodes = split_nodes_image(text_nodes)
                text_nodes = split_nodes_link(text_nodes)

                html_nodes = [text_node_to_html_node(node) for node in text_nodes]
                list_items.append(ParentNode("li", html_nodes))
            children.append(ParentNode("ul", list_items))

        elif block_type == BlockType.ORDERED_LIST:
            lines = block.split("\n")
            list_items = []
            for line in lines:
                text = line.split(". ", 1)[1]
                text_nodes = [TextNode(text, TextType.TEXT)]
                text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
                text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
                text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
                text_nodes = split_nodes_image(text_nodes)
                text_nodes = split_nodes_link(text_nodes)

                html_nodes = [text_node_to_html_node(node) for node in text_nodes]
                list_items.append(ParentNode("li", html_nodes))
            children.append(ParentNode("ol", list_items))

    return ParentNode("div", children)
