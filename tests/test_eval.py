from interpreter.eval import eval_token
from interpreter.token_type import TokenType
from unittest.mock import patch
from io import StringIO


class MockTape:
    def __init__(self):
        self.cells = [0] * 10
        self.data_ptr = 0


def test_eval_token_INC_B():
    tape = MockTape()
    eval_token(TokenType.INC_B, tape)
    assert tape.cells[tape.data_ptr] == 1


def test_eval_token_DEC_B():
    tape = MockTape()
    tape.cells[tape.data_ptr] = 3
    eval_token(TokenType.DEC_B, tape)
    assert tape.cells[tape.data_ptr] == 2


def test_eval_token_INC_PTR():
    tape = MockTape()
    eval_token(TokenType.INC_PTR, tape)
    assert tape.data_ptr == 1


def test_eval_token_DEC_PTR():
    tape = MockTape()
    tape.data_ptr = 2
    eval_token(TokenType.DEC_PTR, tape)
    assert tape.data_ptr == 1


@patch("sys.stdout", new_callable=StringIO)
def test_eval_token_OUT_B_printable(mock_stdout):
    tape = MockTape()
    tape.cells[tape.data_ptr] = 65  # ASCII code for 'A'
    eval_token(TokenType.OUT_B, tape)
    assert mock_stdout.getvalue() == "A\n"


@patch("sys.stdout", new_callable=StringIO)
def test_eval_token_OUT_B_printable(mock_stdout):
    tape = MockTape()
    tape.cells[tape.data_ptr] = 4  # ASCII code for 'A'
    eval_token(TokenType.OUT_B, tape)
    assert mock_stdout.getvalue() == "4\n"
