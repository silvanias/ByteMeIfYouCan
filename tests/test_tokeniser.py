from interpreter.tokeniser import tokenise

def test_only_allowed_characters():
    result = tokenise("<>+-.,[]")
    assert result == ['<', '>', '+', '-', '.', ',', '[', ']']

def test_remove_other_characters():
    result = tokenise("abc123!@#%^&*()_+=-}.{,[:;]")
    assert result == ['+', '-', '.', ',', '[', ']']

def test_empty_string():
    result = tokenise("")
    assert result == []

def test_mixed_characters():
    result = tokenise("a<bc>d.e,f[g]h")
    assert result == ['<', '>', '.', ',', '[', ']']

def test_no_special_characters():
    result = tokenise("abcdefg")
    assert result == []
