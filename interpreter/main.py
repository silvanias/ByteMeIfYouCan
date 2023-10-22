from tokeniser import lex, tokenise
from eval import eval_token
from tape import Tape


def main():
    tape = Tape()
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        words = lex(user_inp)
        tokens = tokenise(words)

        while tape.get_inst_ptr() < len(tokens):       
            eval_token(tokens[tape.get_inst_ptr()], tape)
        tape.reset_inst_ptr()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
