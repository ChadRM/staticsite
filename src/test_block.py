import unittest
from block import BlockType, block_to_block_type

class MyTestCase(unittest.TestCase):
    def test_heading1(self):
        markdown = "#Heading1"
        self.assertEqual(block_to_block_type(markdown), BlockType.HEADING)

    def test_codeblock(self):
        markdown = "```Codeblock correct```"
        self.assertEqual(block_to_block_type(markdown), BlockType.CODE)

    def test_codeblock_unclosed(self):
        markdown = "``` Not a code block"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_unordered_list_one_line(self):
        markdown = "- Correct single item unordered list"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_unordered_list_many_lines(self):
        markdown = "- Line One\n- Line Two\n- Line Three"
        self.assertEqual(block_to_block_type(markdown), BlockType.UNORDERED_LIST)

    def test_screwed_up_unordered_list(self):
        markdown = "- Line One\n- Line Two\n-Line Three"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_single_line_quote(self):
        markdown = "> Single Line Quote"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_multiple_line_quote(self):
        markdown = "> First Line Quote\n> Second Line Quote"
        self.assertEqual(block_to_block_type(markdown), BlockType.QUOTE)

    def test_multi_line_quote_screwed(self):
        markdown = ">FirstLineQuote\n >SecondLineQuote"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

    def test_ordered_list_one_line(self):
        markdown = "1. Correct single item ordered list"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_multi_line_ordered_list(self):
        markdown = "1. Line One\n2. Line Two\n3. Line Three"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_multiline_ordered_list_bigger_than_10(self):
        markdown = "1. Line One\n2. Line Two\n3. Line Three\n4. Line Four\n5. Line Five\n6. Line Six\n7. Line Seven\n8. Line Eight\n9. Line Nine\n10. Line 10"
        self.assertEqual(block_to_block_type(markdown), BlockType.ORDERED_LIST)

    def test_multiline_ordered_list_screwed(self):
        markdown = "1. Line One is okay but\n3. Where is number 2?"
        self.assertEqual(block_to_block_type(markdown), BlockType.PARAGRAPH)

if __name__ == '__main__':
    unittest.main()
