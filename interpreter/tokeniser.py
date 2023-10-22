import re
from interpreter.token_type import TokenType


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
    tokens.append(TokenType.EOF)
    return tokens
