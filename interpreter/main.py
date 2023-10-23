from tokeniser import lex, tokenise
from tape import Tape
from program import Program
import sys
from demo_script import demo


def main():
    MEMORY_CELLS = 100
    tape = Tape(MEMORY_CELLS)
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        words = lex(user_inp)
        tokens = tokenise(words)
        program = Program(tokens, tape)

        while tokens and not program.eof:
            program.consume()
        tape.get_inst_ptr().reset_ptr()


if __name__ == "__main__":
    if (args_count := len(sys.argv)) > 2:
        print(f"One argument expected, got {args_count - 1}")
        raise SystemExit(2)
    elif args_count < 2:
        try:
            main()
        except KeyboardInterrupt:
            print("\nInterrupted")
    else:
        if sys.argv[1] == "demo":
            demo()
        else:
            print(f"{sys.argv[2]} is not supported")
