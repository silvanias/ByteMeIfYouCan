from interpreter.pointer import DataPointer, InstPointer


class Tape:
    """
    Class representing the tape in the interpreter.

    Attributes:
    - `memory`: List representing the memory cells.
    - `cur_cell`: Index of the current cell.
    - `inst_ptr`: Instruction pointer for the tape.
    - `data_ptr`: Data pointer for the tape.

    Methods:
    - __init__(memory_cells): Initializes Tape with an amt of memory cells.
    - inc_cur_cell(): Increments the value of the current cell.
    - dec_cur_cell(): Decrements the value of the current cell.
    - out_cur_cell(): Outputs the value of the current cell.
    - set_cur_cell_value(value): Sets the value of the current cell.
    - get_inst_ptr(): Returns the instruction pointer.
    - get_data_ptr(): Returns the data pointer.
    """

    def __init__(self, cells_len) -> None:
        self.__cells = [0] * cells_len
        self.__data_ptr = DataPointer(cells_len)
        self.__inst_ptr = InstPointer()

    def get_inst_ptr(self):
        return self.__inst_ptr

    def get_data_ptr(self):
        return self.__data_ptr

    def get_cur_cell_value(self):
        return self.__cells[self.__data_ptr.get_ptr()]

    def set_cur_cell_value(self, val):
        self.__cells[self.__data_ptr.get_ptr()] = val

    def inc_cur_cell(self):
        self.__cells[self.__data_ptr.get_ptr()] += 1

    def dec_cur_cell(self):
        if self.__cells[self.__data_ptr.get_ptr()] > 0:
            self.__cells[self.__data_ptr.get_ptr()] -= 1
        else:
            raise ArithmeticError("Cannot make cells value less than 0")

    def out_cur_cell(self):
        to_out = self.__cells[self.__data_ptr.get_ptr()]
        if 32 <= to_out <= 126:
            return chr(to_out)
        return to_out
