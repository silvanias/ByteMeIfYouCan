from interpreter.token_type import TokenType
from interpreter.tape import Tape


def eval_token(token, tape: Tape):
    inst_ptr = tape.get_inst_ptr()
    if token == TokenType.BRPB:
        if tape.get_cur_cell_value() != 0:
            print("Move instruction pointer back to previous bracket")
            # Need to figure out how to access the current token stream from here hmmmmmmm
            # program class?
        else:
            inst_ptr.inc_ptr()
    else:
        match token:
            case TokenType.INC_B:
                tape.inc_cur_cell()
            case TokenType.DEC_B:
                tape.dec_cur_cell()
            case TokenType.INC_PTR:
                tape.get_data_ptr().inc_ptr()
            case TokenType.DEC_PTR:
                tape.get_data_ptr().dec_ptr()
            case TokenType.OUT_B:
                print(tape.out_cur_cell())
            case TokenType.INP_B:
                print("TODO: Take in user input")
            case TokenType.BRZF:
                print("Enter loop")
        inst_ptr.inc_ptr()
