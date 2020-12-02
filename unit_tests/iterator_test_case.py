import random

from number_2_word.containers.number_blocks_collection import NumberBlocksCollection
from number_2_word.shared.definitions import range_dict
from number_2_word.shared.number_utils import concat_numbers_in_blocks, is_number_negative, strip_negative_symbol


def test_iterator_block():
    number = random.randrange(range_dict["minimumRange"], range_dict["maximumRange"])
    number_string = str(number)
    if is_number_negative(number):
        number_string = strip_negative_symbol(number_string)
    number_blocks = concat_numbers_in_blocks(number_string)
    collection = NumberBlocksCollection(number_blocks)
    iterator = collection.get_iterator()
    iterator.iterate_block()
    assert (iterator.full_number is not None)
