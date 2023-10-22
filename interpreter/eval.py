from interpreter.token_type import TokenType
from interpreter.tape import Tape

def eval_token(token, tape: Tape):
    match token:
        case TokenType.INC_B:
            tape.inc_cur_cell()
            tape.inc_inst_ptr()
        case TokenType.DEC_B:
            tape.dec_cur_cell()
            tape.inc_inst_ptr()
        case TokenType.INC_PTR:
            tape.inc_data_ptr()
            tape.inc_inst_ptr()
        case TokenType.DEC_PTR:
            tape.dec_data_ptr()
            tape.inc_inst_ptr()
        case TokenType.OUT_B:
            print(tape.out_cur_cell())
            tape.inc_inst_ptr()
        case TokenType.INP_B:
            print("TODO: Take in user input")
            tape.inc_inst_ptr()
        case TokenType.BRZF:
            print("Enter loop")
            tape.inc_inst_ptr()
        case TokenType.BRPB:
            if tape.get_cur_cell_value != 0:
                print("Move instruction pointer back to previous bracket")
                # Need to figure out how to access the current token stream from here hmmmmmmm
                # program class?
            else:
                tape.inc_inst_ptr()

            
