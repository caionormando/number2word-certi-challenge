"""The Collection is a concrete implementation of the abstract class 'Container', working as an interface."""

from number_2_word.containers.container import Container
from number_2_word.iterators.iterator import Iterator
from number_2_word.iterators.iterator_factory import IteratorFactory


class NumberBlocksCollection(Container):
    def __init__(self, number_blocks) -> None:
        super().__init__(number_blocks)
        self.number_blocks = number_blocks
        self.get_iterator()

    def get_iterator(self) -> Iterator:
        self.iterator = IteratorFactory(self.number_blocks).create_iterator()
        self.iterator.iterate_block()
        return self.iterator
