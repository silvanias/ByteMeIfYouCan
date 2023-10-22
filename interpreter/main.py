from tokeniser import lex, tokenise
from eval import eval_token
from tape import Tape


def main():
    MEMORY_CELLS = 100
    tape = Tape(MEMORY_CELLS)
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        words = lex(user_inp)
        tokens = tokenise(words)

        while tape.get_inst_ptr().get_ptr() < len(tokens):
            eval_token(tokens[tape.get_inst_ptr().get_ptr()], tape)
        tape.get_inst_ptr().reset_ptr()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
