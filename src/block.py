from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    markdown_list = markdown.split("\n\n")
    new_blocks = []
    for raw_block in markdown_list:
        raw_block = raw_block.strip()
        if raw_block != "":
            new_blocks.append(raw_block)
    return new_blocks


def block_to_block_type(markdown):
    if markdown.startswith("#"):
        return BlockType.HEADING
    elif markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    elif markdown.startswith(">"):
        all_items = markdown.split("\n")
        for item in all_items:
            if item.startswith(">"):
                pass
            else:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif markdown.startswith("- "):
        all_items = markdown.split("\n")
        for item in all_items:
            if item.startswith("- "):
                pass
            else:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif markdown.startswith("1. "):
        index = 1
        all_items = markdown.split("\n")
        for item in all_items:
            if item.startswith(f"{index}. "):
                index += 1
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH