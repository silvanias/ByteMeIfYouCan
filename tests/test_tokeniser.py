import pytest
from interpreter.tokeniser import lex, map_tokens, tokenise, TokenType

def test_lex_empty_input():
    assert lex("") == []

def test_lex_valid_input():
    assert lex("++<>,.-[]") == ['+', '+', '<', '>', ',', '.', '-', '[', ']']

def test_lex_invalid_characters():
    assert lex("abc123!@#") == []

def test_map_tokens_valid_token():
    assert map_tokens("+") == TokenType.INC_B

def test_map_tokens_invalid_token():
    with pytest.raises(ValueError, match="Invalid token_type: invalid"):
        map_tokens("invalid")

def test_tokenise_empty_list():
    assert tokenise([]) == []

def test_tokenise_valid_tokens():
    assert tokenise(["+", "-", ".", "[", "]"]) == [TokenType.INC_B, TokenType.DEC_B, TokenType.OUT_B, TokenType.BRZF, TokenType.BRPB]

def test_tokenise_invalid_tokens():
    with pytest.raises(ValueError, match="Invalid token_type: invalid"):
        tokenise(["invalid", "+", "-"])

def test_lex_mixed_case_input():
    assert lex("AbCdEf") == []

def test_lex_whitespace_input():
    assert lex("  \t\n  ") == []

def test_lex_mixed_valid_and_invalid_characters():
    assert lex("+-*.,<>") == ['+', '-', '.', ',', '<', '>']

def test_map_tokens_valid_token_case_insensitive():
    assert map_tokens(".") == TokenType.OUT_B

def test_map_tokens_invalid_token_case_insensitive():
    with pytest.raises(ValueError, match="Invalid token_type: invalid_token"):
        map_tokens("invalid_token")

def test_tokenise_mixed_valid_and_invalid_tokens():
    with pytest.raises(ValueError, match="Invalid token_type: invalid_token"):
        tokenise(["+", "invalid_token", "-"])

def test_tokenise_mixed_valid_and_invalid_token_types():
    with pytest.raises(ValueError, match="Invalid token_type: 123"):
        tokenise(["+", 123, "-"])