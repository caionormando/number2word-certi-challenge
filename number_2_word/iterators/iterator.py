"""This class is responsible for iterating between the elements of the collection and calling the necessary methods to
manipulate them."""

import abc


class Iterator(metaclass=abc.ABCMeta):

    def __init__(self, number_blocks) -> None:
        super().__init__()
        self.number_blocks = number_blocks

    @abc.abstractmethod
    def is_block_over(self) -> bool:
        pass

    @abc.abstractmethod
    def iterate_block(self) -> str:
        pass
