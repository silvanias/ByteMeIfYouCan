class Pointer:
    """
    Base class for a simple pointer with an address.

    Methods:
    - __init__(): Initializes the pointer with an initial address of 0.
    - get_ptr(): Returns the current address of the pointer.
    - reset_ptr(): Resets the address of the pointer to 0.
    - inc_ptr(): Increments the address of the pointer by 1.
    - dec_ptr(): Decrements the address of the pointer by 1.
    """

    def __init__(self) -> None:
        self.__address = 0

    def get_ptr(self):
        return self.__address

    def reset_ptr(self):
        self.__address = 0

    def inc_ptr(self):
        self.__address += 1

    def dec__ptr(self):
        self.__address -= 1


class DataPointer(Pointer):
    """
    Derived class for a pointer with handling for circular increment and decrement.

    Methods:
    - __init__(cells_len): Initializes the pointer with an address of 0 and specified cells length.
    - inc_ptr(): Increments the address of the data pointer, handling circular increment.
    - dec_ptr(): Decrements the address of the data pointer, handling circular decrement.
    """

    def __init__(self, cells_len) -> None:
        super().__init__()
        self.__cells_len = cells_len

    def inc_ptr(self):
        if self._Pointer__address == self.__cells_len - 1:
            self._Pointer__address = 0
        else:
            self._Pointer__address += 1

    def dec_ptr(self):
        if self._Pointer__address == 0:
            self._Pointer__address = self.__cells_len - 1
        else:
            self._Pointer__address -= 1


class InstPointer(Pointer):
    """
    Derived class for an instruction pointer with handling for preventing negative addresses.

    Methods:
    - dec_ptr(): Decrements address of pointer, handling prevention of negative addresses.
    """
    def dec_ptr(self):
        if self._Pointer__address != 0:
            self._Pointer__address -= 1
        else:
            raise IndexError("Cannot make inst ptr less than 0")
