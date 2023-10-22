from interpreter.pointer import DataPointer, InstPointer


class Tape:
    def __init__(self, cells_len) -> None:
        self.__cells = [0] * cells_len
        self.__data_ptr = DataPointer(cells_len)
        self.__inst_ptr = InstPointer(cells_len)

    def get_inst_ptr(self):
        return self.__inst_ptr

    def get_data_ptr(self):
        return self.__data_ptr

    def get_cur_cell_value(self):
        return self.__cells[self.__data_ptr.get_ptr()]

    def inc_cur_cell(self):
        self.__cells[self.__data_ptr.get_ptr()] += 1

    def dec_cur_cell(self):
        if self.__cells[self.__data_ptr.get_ptr()] <= 0:
            raise ArithmeticError("Cannot make cells value less than 0")
        else:
            self.__cells[self.__data_ptr.get_ptr()] -= 1

    def out_cur_cell(self):
        to_out = self.__cells[self.__data_ptr.get_ptr()]
        if 32 <= to_out <= 126:
            return chr(to_out)
        else:
            return to_out
