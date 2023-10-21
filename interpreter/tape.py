class Tape:
    def __init__(self) -> None:
        self.cells = [0] * 100
        self.data_ptr = 0
        self.inst_ptr = 0
