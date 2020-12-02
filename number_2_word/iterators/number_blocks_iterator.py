""""This concrete implementation of the iterator abstract class iterates between number blocks and send each one of them
to the Block Handler, where the number block will get its word. After that, the Composer Handler is responsible for
joining the two blocks applying or not any modifications in the sentences (e.g. "e", "mil")."""

from number_2_word.block_handler.block_handler import BlockHandler
from number_2_word.block_handler.composer_handler import ComposerHandler
from number_2_word.iterators.iterator import Iterator


class NumberBlocksIterator(Iterator):
    index = 0

    def __init__(self, number_blocks) -> None:
        self.number_blocks = number_blocks
        self.blocks_sentences = []
        self.full_number = ''

    def is_block_over(self) -> bool:
        if self.index < len(self.number_blocks):
            return False
        return True

    def iterate_block(self):
        for block in range(1, len(self.number_blocks)):
            block_handler = BlockHandler()
            self.blocks_sentences.append(block_handler.get_block_sentence(self.number_blocks[block]))
            if not self.is_block_over():
                self.index = self.index + 1
            else:
                return None
        if len(self.blocks_sentences) == 1:
            self.full_number = self.blocks_sentences[0]
        else:
            word_composer = ComposerHandler(self.blocks_sentences)
            self.full_number = word_composer.compose_number()
        return self.full_number
