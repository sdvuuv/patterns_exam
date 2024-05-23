from file_reading import file_reading


class counter:

    def __init__(self, count_num, filename):
        self.count_num = count_num
        self.filename = filename

    def count_in_file(self):
        count = 0
        file = file_reading(self.filename)
        text = file.read()
        whole_line = ''
        for line in text:
            whole_line+=str(line.decode("utf-8"))

        if self.count_num == '1' or self.count_num == '0':

            bytes_str = bytearray(str(whole_line), 'UTF-8')
            for single_byte in bytes_str:
                mask_bit = 0b00000001
                for i in range(8):
                    if (single_byte & mask_bit) and self.count_num == '1':
                        count += 1
                    elif self.count_num == '0':
                        count += 1
                    mask_bit <<= 1
        else:
            raise Exception("The value passed is not zero or one")

        return count
