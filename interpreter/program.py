from interpreter.token_type import TokenType
from interpreter.tape import Tape


class Program:
    """
    Class representing a program in the interpreter.

    Attributes:
    - `_token_l`: List of tokens representing the program.
    - `tape`: Tape object associated with the program.
    - `inst_ptr`: Instruction pointer for the program.
    - `data_ptr`: Data pointer for the program.
    - `eof`: Flag indicating whether the end of the program has been reached.

    Methods:
    - __init__(tokens, tape): Initializes the Program with a list of tokens and a tape.
    - consume(): Consumes the next token and evaluates it.
    - eval_token(token): Evaluates the given token and performs the corresponding action.
    - branch_forward(): Executes forward branch operation based on current cell value.
    - branch_backward(): Executes backward branch operation based on current cell value
    - take_input(): Takes user input and sets the current cell value to the input integer.
    """

    def __init__(self, tokens, tape: Tape) -> None:
        self._token_l = tokens
        self.tape = tape
        self.inst_ptr = tape.get_inst_ptr()
        self.data_ptr = tape.get_data_ptr()
        self.eof = False

    def consume(self) -> None:
        """Consumes the next token and evaluates it."""
        self.eval_token(self._token_l[self.inst_ptr.get_ptr()])

    def eval_token(self, token) -> None:
        """
        Evaluates the given token and performs the corresponding action.

        Parameters:
        - `token`: The token to be evaluated.
        """
        lin_cmds = {
            TokenType.INC_B: self.tape.inc_cur_cell,
            TokenType.DEC_B: self.tape.dec_cur_cell,
            TokenType.INC_PTR: self.tape.get_data_ptr().inc_ptr,
            TokenType.DEC_PTR: self.tape.get_data_ptr().dec_ptr,
            TokenType.OUT_B: lambda: print(self.tape.out_cur_cell()),
            TokenType.INP_B: self.take_input,
            TokenType.EOF: lambda: setattr(self, "eof", True),
        }

        if token == TokenType.BRZF:
            self.branch_forward()

        elif token == TokenType.BRPB:
            self.branch_backward()

        else:
            lin_cmds[token]()
            self.inst_ptr.inc_ptr()

    def branch_forward(self) -> None:
        """Executes forward branch operation based on current cell value."""
        if self.tape.get_cur_cell_value() == 0:
            while self._token_l[self.inst_ptr.get_ptr()] != TokenType.BRPB:
                self.inst_ptr.inc_ptr()
        else:
            self.inst_ptr.inc_ptr()

    def branch_backward(self) -> None:
        """Executes backward branch operation based on current cell value."""
        if self.tape.get_cur_cell_value() != 0:
            while self._token_l[self.inst_ptr.get_ptr()] != TokenType.BRZF:
                self.inst_ptr.dec_ptr()
        else:
            self.inst_ptr.inc_ptr()

    def take_input(self) -> None:
        """Takes user input and sets the current cell value to the input integer."""
        in_byte = input("Please input an integer\n")
        try:
            in_byte = int(in_byte)
        except ValueError:
            print("Could not format to integer")
        self.tape.set_cur_cell_value(in_byte)
