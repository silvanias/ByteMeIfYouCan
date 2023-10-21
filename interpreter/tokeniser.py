import re
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


def lex(stream: str):
    stream = re.sub(r"[^<>+\-.,\[\]]", "", string=stream)
    stream = list(stream)
    return stream


def map_tokens(word: str):
    try:
        token_type = TokenType(word)
    except ValueError:
        raise ValueError(f"Invalid token_type: {word}")
    return token_type


def tokenise(words: list):
    tokens = list(map(map_tokens, words))
    return tokens
