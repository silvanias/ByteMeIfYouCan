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
        for token in tokens:
            eval_token(token, tape)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
