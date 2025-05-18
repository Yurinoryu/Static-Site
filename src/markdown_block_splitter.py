def markdown_to_blocks(markdown):

    raw_blocks = markdown.split('\n\n')
    cleaned_blocks = []
    for block in raw_blocks:
        lines = block.strip().split('\n')
        cleaned_lines = [line.strip() for line in lines]
        cleaned_block = '\n'.join(cleaned_lines)
        if cleaned_block:
            cleaned_blocks.append(cleaned_block)
    return cleaned_blocks
