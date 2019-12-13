import random

from number_2_word.number_separators.number_block_separator import NumberBlockSeparator
from number_2_word.number_separators.number_separator_factory import NumberSeparatorFactory
from number_2_word.shared.definitions import range_dict


def test_create_separator():
    separator_factory = NumberSeparatorFactory(random.randrange(range_dict["minimumRange"], range_dict["maximumRange"]))
    separator = separator_factory.create_separator()
    assert (separator is not None)


def test_create_separator_collection():
    number = random.randrange(range_dict["minimumRange"], range_dict["maximumRange"])
    separator = NumberBlockSeparator(number)
    collection = separator.create_collection(number)
    assert (collection is not None)
