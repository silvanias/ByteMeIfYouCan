from tokeniser import lex, tokenise


def main():
    while True:
        user_inp = input("> ")
        if not user_inp:
            continue
        words = lex(user_inp)
        tokens = tokenise(words)
        print(tokens)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
