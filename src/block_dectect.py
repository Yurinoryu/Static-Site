from blocktype import *

def block_to_block_type(block):
    lines = block.split('\n')

    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE

    if lines[0].startswith('#'):
        if 1<= len(lines[0].split(' ')[0]) <= 6 and lines[0][len(lines[0].split(' ')[0])] == ' ':
            return BlockType.HEADING

    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE

    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i + 1}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
