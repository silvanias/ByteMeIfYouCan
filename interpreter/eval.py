from interpreter.token_type import TokenType
from interpreter.tape import Tape

def eval_token(token, tape: Tape):
    match token:
        case TokenType.INC_B:
            tape.inc_cur_cell()
        case TokenType.DEC_B:
            tape.dec_cur_cell()
        case TokenType.INC_PTR:
            tape.inc_data_ptr()
        case TokenType.DEC_PTR:
            tape.dec_data_ptr()
        case TokenType.OUT_B:
            print(tape.out_cur_cell())
        case TokenType.INP_B:
            print("TODO: Take in user input")
        case TokenType.BRZF:
            print("TODO: Branching")
        case TokenType.BRPB:
            print("TODO: Branching")
