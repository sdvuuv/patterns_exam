import unittest
from file_reading import file_reading
from counter import counter


class testing(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_file(self):
        name = "1.txt"
        file = file_reading(name)
        assert len(str(file.read())) != 0

    def test_bit(self):
        file = open("1.txt", "w+")
        file.write("a")
        file.close()
        file = open("1.txt", "r")
        counter_ones = counter('1', '1.txt')
        counter_zeros = counter('0', '1.txt')
        bit_1_cnt = counter_ones.count_in_file()
        bit_0_cnt = counter_zeros.count_in_file()
        assert len(str(file.read())) != 0
        assert bit_1_cnt == 3
        assert bit_0_cnt == 8