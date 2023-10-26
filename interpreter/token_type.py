from enum import Enum


class TokenType(Enum):
    """
    Enumerates the different token types.

    Members:
    - `INC_B`: Increment the value of the current memory cell.
    - `DEC_B`: Decrement the value of the current memory cell.
    - `INC_PTR`: Increment the data pointer.
    - `DEC_PTR`: Decrement the data pointer.
    - `OUT_B`: Output the value of the current memory cell.
    - `INP_B`: Input a value and store it in the current memory cell.
    - `BRZF`: Begin a loop, jump forward if the current memory cell is zero.
    - `BRPB`: End a loop, jump back to the corresponding '[' if the current memory cell is non-zero.
    - `EOF`: End of the program.
    """

    INC_B = "+"
    DEC_B = "-"
    INC_PTR = ">"
    DEC_PTR = "<"
    OUT_B = "."
    INP_B = ","
    BRZF = "["
    BRPB = "]"
    EOF = "@"
