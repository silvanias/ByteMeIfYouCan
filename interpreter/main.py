"""
Interpreter Module

This module provides the command line interface for Brainf*ck.
It also includes the controller interpret function.

Functions:
- `main(tape: Tape)`: Interpreter environment loop.
    Parameters:
    - `tape` (Tape): The tape to be used for interpretation.

- `interpret(user_inp, tape: Tape)`: Takes user input and pipes it through steps of interpretation.
    Parameters:
    - `user_input` (str): The user input string.
    - `tape` (Tape): The tape to be used for interpretation.
"""
import sys
from pathlib import Path
from tokeniser import lex, tokenise
from tape import Tape
from program import Program
from demo_script import demo


def main(tape: Tape):
    """
    Interpreter environment loop.

    Parameters:
    - `tape` (Tape): The tape to be used for the interpretation.
    """
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        interpret(user_inp, tape)


def interpret(user_inp, tape: Tape):
    """
    Takes the user input and pipes it through the process of interpretation
    including executing the program.

    Parameters:
    - `user_input` (str): The user input string.
    - `tape` (Tape): The tape to be used for the interpretation.
    """
    words = lex(user_inp)
    tokens = tokenise(words)
    program = Program(tokens, tape)

    while tokens and not program.eof:
        program.consume()
    tape.get_inst_ptr().reset_ptr()


if __name__ == "__main__":
    MEMORY_CELLS = 100
    tape_m = Tape(MEMORY_CELLS)

    if (args_count := len(sys.argv)) < 2:
        try:
            main(tape_m)
        except KeyboardInterrupt:
            print("\nInterrupted")
    elif args_count == 2:
        if sys.argv[1] == "demo":
            demo()
        else:
            target_file = Path(sys.argv[1])
            if not target_file.is_file():
                print(f'Target file "{sys.argv[1]}" does not exist')
                raise SystemExit(1)

            with open(target_file, encoding="utf-8") as f:
                for line in f:
                    interpret(line, tape_m)
    else:
        print(f"One argument expected, got {args_count - 1}")
        raise SystemExit(2)
