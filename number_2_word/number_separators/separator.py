"""The Separator is the class responsible for the first manipulation of the input number. It separates the digits of
each block and calls for a collection in order to store it."""

import abc

from number_2_word.containers.container import Container


class Separator (metaclass=abc.ABCMeta):

    def __init__(self, number) -> None:
        super().__init__()
        self.number = number

    @abc.abstractmethod
    def create_collection(self, number) -> Container:
        pass
