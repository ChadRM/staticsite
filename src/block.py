from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

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