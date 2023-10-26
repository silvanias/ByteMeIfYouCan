"""
Lexical Analyzer Module

This module provides functions for lexical analysis, 
converting a given stream of characters into a list of tokens.

Functions:
- `lex(stream: str)`: Tokenizes a given stream of characters, filtering out invalid characters.
- `map_tokens(word: str)`: Maps a word to its corresponding TokenType.
- `tokenise(words: list)`: Converts a list of words into a list of tokens, appending an EOF token.
"""
import re
from interpreter.token_type import TokenType


def lex(stream: str) -> list:
    """
    Tokenizes a given stream of characters, filtering out invalid characters.

    Parameters:
    - `stream`: The input stream of characters.

    Returns:
    - A list of tokens extracted from the stream.
    """
    stream = re.sub(r"[^<>+\-.,\[\]]", "", string=stream)
    stream = list(stream)
    return stream


def map_tokens(word: str) -> TokenType:
    """
    Maps a word to its corresponding TokenType.

    Parameters:
    - `word`: The input word to be mapped.

    Returns:
    - The corresponding TokenType for the given word.

    Raises:
    - ValueError: If the word does not match any TokenType.
    """
    try:
        token_type = TokenType(word)
    except ValueError as exc:
        raise ValueError(f"Invalid token_type: {word}") from exc
    return token_type


def tokenise(words: list) -> list:
    """
    Converts a list of words into a list of tokens, appending an EOF token.

    Parameters:
    - `words`: The list of words to be converted to tokens.

    Returns:
    - A list of tokens.
    """
    tokens = list(map(map_tokens, words))
    tokens.append(TokenType.EOF)
    return tokens
