from interpreter.token_type import TokenType
from interpreter.tape import Tape


class Program:
    """
    Class representing a program in the interpreter.

    Attributes:
    - `__token_l`: List of tokens representing the program.
    - `tape`: Tape object associated with the program.
    - `inst_ptr`: Instruction pointer for the program.
    - `data_ptr`: Data pointer for the program.
    - `eof`: Flag indicating whether the end of the program has been reached.

    Methods:
    - __init__(tokens, tape): Initializes the Program with a list of tokens and a tape.
    - consume(): Consumes the next token and evaluates it.
    - eval_token(token): Evaluates the given token and performs the corresponding action.
    """

    def __init__(self, tokens, tape: Tape) -> None:
        self.__token_l = tokens
        self.tape = tape
        self.inst_ptr = tape.get_inst_ptr()
        self.data_ptr = tape.get_data_ptr()
        self.eof = False

    def consume(self):
        """Consumes the next token and evaluates it."""
        self.eval_token(self.__token_l[self.inst_ptr.get_ptr()])

    def eval_token(self, token):
        """
        Evaluates the given token and performs the corresponding action.

        Parameters:
        - `token`: The token to be evaluated.
        """
        if token == TokenType.BRZF:
            if self.tape.get_cur_cell_value() == 0:
                while self.__token_l[self.inst_ptr.get_ptr()] != TokenType.BRPB:
                    self.inst_ptr.inc_ptr()
            else:
                self.inst_ptr.inc_ptr()

        elif token == TokenType.BRPB:
            if self.tape.get_cur_cell_value() != 0:
                while self.__token_l[self.inst_ptr.get_ptr()] != TokenType.BRZF:
                    self.inst_ptr.dec_ptr()
            else:
                self.inst_ptr.inc_ptr()

        else:
            match token:
                case TokenType.INC_B:
                    self.tape.inc_cur_cell()
                case TokenType.DEC_B:
                    self.tape.dec_cur_cell()
                case TokenType.INC_PTR:
                    self.tape.get_data_ptr().inc_ptr()
                case TokenType.DEC_PTR:
                    self.tape.get_data_ptr().dec_ptr()
                case TokenType.OUT_B:
                    print(self.tape.out_cur_cell())
                case TokenType.INP_B:
                    in_byte = input("Please input an integer\n")
                    try:
                        in_byte = int(in_byte)
                    except ValueError:
                        print("Could not format to integer")
                    self.tape.set_cur_cell_value(in_byte)
                case TokenType.EOF:
                    self.eof = True
            self.inst_ptr.inc_ptr()
