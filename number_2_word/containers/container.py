"""It is responsible for storing the objects which will be iterated in the algorithm. That is why it contains a call for
the iterator."""

import abc

from number_2_word.iterators.iterator import Iterator


class Container(metaclass=abc.ABCMeta):

    def __init__(self, number_blocks) -> None:
        self.number_blocks = number_blocks
        self.iterator = None

    @abc.abstractmethod
    def get_iterator(self) -> Iterator:
        pass
