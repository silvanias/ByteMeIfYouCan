from tokeniser import lex, tokenise
from tape import Tape
from program import Program
import sys
from demo_script import demo
from pathlib import Path


def main(tape):
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        interpret(user_inp, tape)


def interpret(user_inp, tape: Tape):
    words = lex(user_inp)
    tokens = tokenise(words)
    program = Program(tokens, tape)

    while tokens and not program.eof:
        program.consume()
    tape.get_inst_ptr().reset_ptr()


if __name__ == "__main__":
    MEMORY_CELLS = 100
    tape = Tape(MEMORY_CELLS)

    if (args_count := len(sys.argv)) > 2:
        print(f"One argument expected, got {args_count - 1}")
        raise SystemExit(2)
    elif args_count < 2:
        try:
            main(tape)
        except KeyboardInterrupt:
            print("\nInterrupted")
    else:
        if sys.argv[1] == "demo":
            demo()
        else:
            target_file = Path(sys.argv[1])
            if not target_file.is_file():
                print(f'Target file "{sys.argv[1]}" does not exist')
                raise SystemExit(1)

            with open(target_file) as f:
                for line in f:
                    interpret(line, tape)
