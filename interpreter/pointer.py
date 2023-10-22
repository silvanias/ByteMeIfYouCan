class Pointer:
    def __init__(self, cells_len) -> None:
        self.__address = 0
        self.__cells_len = cells_len

    def get_ptr(self):
        return self.__address

    def reset_ptr(self):
        self.__address = 0

    def inc_ptr(self):
        self.__address += 1

    def dec__ptr(self):
        self.__address -= 1


class DataPointer(Pointer):
    def inc_ptr(self):
        if self._Pointer__address == self._Pointer__cells_len - 1:
            self._Pointer__address = 0
        else:
            self._Pointer__address += 1

    def dec_ptr(self):
        if self._Pointer__address == 0:
            self._Pointer__address = self._Pointer__cells_len - 1
        else:
            self._Pointer__address -= 1


class InstPointer(Pointer):
    def dec_ptr(self):
        if self._Pointer__address == 0:
            raise IndexError("Cannot make inst ptr less than 0")
        else:
            self._Pointer__address -= 1
