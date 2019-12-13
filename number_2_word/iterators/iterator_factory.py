"""Although the only type of iterator we have is for the approach we are using, having a factory allows that
     future implementations become easy, such as well as other separators. This is an approach based on the SOLID
     OCP principle"""
from number_2_word.iterators.iterator import Iterator
from number_2_word.iterators.number_blocks_iterator import NumberBlocksIterator


class IteratorFactory:

    def __init__(self, number) -> None:
        self.number = number

    def create_iterator(self) -> Iterator:
        iterator: Iterator = NumberBlocksIterator(self.number)
        return iterator





