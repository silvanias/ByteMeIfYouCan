class Tape:
    def __init__(self) -> None:
        self.__cells = [0] * 100
        self.__data_ptr = 0
        self.__inst_ptr = 0

    def get_inst_ptr(self):
        return self.__inst_ptr

    def reset_inst_ptr(self):
        self.__inst_ptr = 0

    def inc_inst_ptr(self):
        self.__inst_ptr += 1

    def dec_inst_ptr(self):
        if self.__inst_ptr == 0:
            raise IndexError("Cannot make inst ptr less than 0")
        else:
            self.__inst_ptr -= 1

    def get_data_ptr(self):
        return self.__data_ptr

    def inc_data_ptr(self):
        if self.__data_ptr == 99:
            self.__data_ptr = 0
        else:
            self.__data_ptr += 1

    def dec_data_ptr(self):
        if self.__data_ptr == 0:
            self.__data_ptr = 99
        else:
            self.__data_ptr -= 1

    def get_cur_cell_value(self):
        return self.__cells[self.__data_ptr]

    def inc_cur_cell(self):
        self.__cells[self.__data_ptr] += 1

    def dec_cur_cell(self):
        if self.__cells[self.__data_ptr] <= 0:
            raise ArithmeticError("Cannot make cells value less than 0")
        else:
            self.__cells[self.__data_ptr] -= 1

    def out_cur_cell(self):
        to_out = self.__cells[self.__data_ptr]
        if 32 <= to_out <= 126:
            return chr(to_out)
        else:
            return to_out
