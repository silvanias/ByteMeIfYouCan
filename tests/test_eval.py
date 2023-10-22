from interpreter.tape import Tape
from interpreter.token_type import TokenType
from unittest.mock import patch
from io import StringIO


def test_eval_token_INC_B():
    tape = Tape(100)
    eval_token(TokenType.INC_B, tape)
    assert tape.get_cur_cell_value() == 1


def test_eval_token_DEC_B():
    tape = Tape(100)
    tape.inc_cur_cell()
    eval_token(TokenType.DEC_B, tape)
    assert tape.get_cur_cell_value() == 0


def test_eval_token_INC_PTR():
    tape = Tape(100)
    eval_token(TokenType.INC_PTR, tape)
    assert tape.get_data_ptr().get_ptr() == 1


def test_eval_token_DEC_PTR():
    tape = Tape(100)
    tape.get_data_ptr().inc_ptr()  # Set data pointer to 1
    eval_token(TokenType.DEC_PTR, tape)
    assert tape.get_data_ptr().get_ptr() == 0


@patch("sys.stdout", new_callable=StringIO)
def test_eval_token_OUT_B_printable(mock_stdout):
    tape = Tape(100)
    for x in range(32):
        tape.inc_cur_cell()  # ASCII code for 'a'
    eval_token(TokenType.OUT_B, tape)
    assert mock_stdout.getvalue() == "a\n"


@patch("sys.stdout", new_callable=StringIO)
def test_eval_token_OUT_B_printable(mock_stdout):
    tape = Tape(100)
    for x in range(4):
        tape.inc_cur_cell()  # ASCII code for 'a'
    eval_token(TokenType.OUT_B, tape)
    assert mock_stdout.getvalue() == "4\n"
