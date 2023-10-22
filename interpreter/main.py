from tokeniser import lex, tokenise
from tape import Tape
from program import Program


def main():
    MEMORY_CELLS = 100
    tape = Tape(MEMORY_CELLS)
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        words = lex(user_inp)
        tokens = tokenise(words)

        # Create program object here, pass in tokens, plus pointer
        program = Program(tokens, tape)

        while tokens and not program.eof:
            program.consume()
        tape.get_inst_ptr().reset_ptr()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
