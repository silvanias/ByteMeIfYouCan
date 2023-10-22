from interpreter.tape import Tape
from interpreter.token_type import TokenType
from interpreter.program import Program
from unittest.mock import patch
from io import StringIO


def test_eval_token_INC_B():
    tape = Tape(100)
    program = Program(
        [TokenType.INC_B],
        tape,
    )
    program.consume()
    assert tape.get_cur_cell_value() == 1


def test_eval_token_DEC_B():
    tape = Tape(100)
    tape.inc_cur_cell()
    program = Program(
        [TokenType.DEC_B],
        tape,
    )
    program.consume()
    assert tape.get_cur_cell_value() == 0


def test_eval_token_INC_PTR():
    tape = Tape(100)
    program = Program(
        [TokenType.INC_PTR],
        tape,
    )
    program.consume()
    assert tape.get_data_ptr().get_ptr() == 1


def test_eval_token_DEC_PTR():
    tape = Tape(100)
    tape.get_data_ptr().inc_ptr()
    program = Program(
        [TokenType.DEC_PTR],
        tape,
    )
    program.consume()
    assert tape.get_data_ptr().get_ptr() == 0


@patch("sys.stdout", new_callable=StringIO)
def test_eval_token_OUT_B_print_ASCII(mock_stdout):
    tape = Tape(100)
    for x in range(65):  # ASCII code for 'A'
        tape.inc_cur_cell()
    program = Program(
        [TokenType.OUT_B],
        tape,
    )
    program.consume()
    assert mock_stdout.getvalue() == "A\n"


@patch("sys.stdout", new_callable=StringIO)
def test_eval_token_OUT_B_print_INTP(mock_stdout):
    tape = Tape(100)
    for x in range(4):
        tape.inc_cur_cell()
    program = Program(
        [TokenType.OUT_B],
        tape,
    )
    program.consume()
    assert mock_stdout.getvalue() == "4\n"

def test_consume_eof():
    tape = Tape(100)
    program = Program([TokenType.EOF], tape)
    program.consume()
    assert program.eof
