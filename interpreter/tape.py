from interpreter.pointer import DataPointer, InstPointer


class Tape:
    """
    Class representing the tape in the interpreter.

    Attributes:
    - `_cells`: List representing the memory cells.
    - `_data_ptr`: DataPointer obj - the data ptr for the tape.
    - `_inst_ptr`: InstPointer obj - the instruction ptr for the tape.


    Methods:
    - __init__(memory_cells): Initializes Tape with an amt of memory cells.
    - inc_cur_cell(): Increments the value of the current cell.
    - dec_cur_cell(): Decrements the value of the current cell.
    - out_cur_cell(): Outputs the value of the current cell.
    - set_cur_cell_value(value): Sets the value of the current cell.
    - get_inst_ptr(): Returns the instruction pointer.
    - get_data_ptr(): Returns the data pointer.
    - get_cur_cell_value(): Returns the value of the current cell.
    - get_cur_cell_addr(): Returns the address of the current cell.
    - get_inst_addr(): Returns the address of the instruction pointer.
    """

    def __init__(self, cells_len) -> None:
        self._cells = [0] * cells_len
        self._data_ptr = DataPointer(cells_len)
        self._inst_ptr = InstPointer()

    def get_inst_ptr(self) -> InstPointer:
        """Returns the instruction pointer."""
        return self._inst_ptr

    def get_data_ptr(self) -> DataPointer:
        """Returns the data pointer."""
        return self._data_ptr

    def get_cur_cell_value(self) -> int:
        """Returns the value of the current cell."""
        return self._cells[self._data_ptr.get_ptr()]

    def set_cur_cell_value(self, val) -> None:
        """Sets the value of the current cell."""
        self._cells[self._data_ptr.get_ptr()] = val

    def get_cur_cell_addr(self) -> int:
        """Returns the address of the current cell."""
        return self._data_ptr.get_ptr()

    def get_inst_addr(self) -> int:
        """Returns the address of the instruction pointer."""
        return self._inst_ptr.get_ptr()

    def inc_cur_cell(self) -> None:
        """Increments the value of the current cell."""
        self._cells[self._data_ptr.get_ptr()] += 1

    def dec_cur_cell(self) -> None:
        """Decrements the value of the current cell."""
        if self._cells[self._data_ptr.get_ptr()] > 0:
            self._cells[self._data_ptr.get_ptr()] -= 1
        else:
            raise ArithmeticError("Cannot make cells value less than 0")

    def out_cur_cell(self) -> int | str:
        """Outputs the value of the current cell."""
        to_out = self._cells[self._data_ptr.get_ptr()]
        if 32 <= to_out <= 126:
            return chr(to_out)
        return to_out
