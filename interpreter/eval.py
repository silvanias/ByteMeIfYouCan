from interpreter.token_type import TokenType


def eval_token(token, tape):
    match token:
        case TokenType.INC_B:
            tape.cells[tape.data_ptr] += 1
        case TokenType.DEC_B:
            tape.cells[tape.data_ptr] -= 1
        case TokenType.INC_PTR:
            tape.data_ptr += 1
        case TokenType.DEC_PTR:
            tape.data_ptr -= 1
        case TokenType.OUT_B:
            to_out = tape.cells[tape.data_ptr]
            if 32 <= to_out <= 126:
                print(chr(to_out))
            else:
                print(to_out)
        case TokenType.INP_B:
            print("TODO: Take in user input")
        case TokenType.BRZF:
            print("TODO: Branching")
        case TokenType.BRPB:
            print("TODO: Branching")
