"""The Number block separator is a concrete implementation of the abstract class Separator specifically designed
for this block-approach application"""

from number_2_word.containers.number_blocks_collection import NumberBlocksCollection
from number_2_word.number_separators.separator import Separator
from number_2_word.shared.number_utils import concat_numbers_in_blocks, strip_negative_symbol, is_number_negative
from number_2_word.shared.word_numbers import symbols_dict


class NumberBlockSeparator(Separator):

    def __init__(self, number) -> None:
        super().__init__(number)
        self.number = number
        self.is_negative = False

    def create_collection(self, number):
        number_string = str(number)
        if is_number_negative(number):
            number_string = strip_negative_symbol(number_string)
            self.is_negative = True
        blocks_collection = NumberBlocksCollection(concat_numbers_in_blocks(number_string))
        if self.is_negative:
            blocks_collection.iterator.full_number = symbols_dict["-"] + blocks_collection.iterator.full_number
        return blocks_collection
