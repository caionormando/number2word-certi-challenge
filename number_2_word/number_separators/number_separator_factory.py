"""Although the only type of separator we have is for the approach we are using, having a factory allows that
future implementations become easy, such as well as other separators. For more information, please check README.md"""
from number_2_word.number_separators.number_block_separator import NumberBlockSeparator
from number_2_word.number_separators.separator import Separator


class NumberSeparatorFactory:

    def __init__(self, number) -> None:
        self.number = number

    def create_separator(self) -> Separator:
        separator: Separator = NumberBlockSeparator(self.number)
        return separator
