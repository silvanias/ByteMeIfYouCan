from enum import Enum


class TokenType(Enum):
    INC_B = "+"
    DEC_B = "-"
    INC_PTR = ">"
    DEC_PTR = "<"
    OUT_B = "."
    INP_B = ","
    BRZF = "["
    BRPB = "]"
    EOF = "@"
