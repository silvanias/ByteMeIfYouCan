from tokeniser import lex, tokenise
from tape import Tape
from program import Program
from time import sleep


def demo():
    print("\n")
    print("Entering demonstration\n")
    sleep(0.5)
    print("Here I present to you:")
    sleep(0.5)
    print(
        r"""
_______   .-------.       ____    .-./`) ,---.   .--. ________                _______   .--.   .--.   
\  ____  \ |  _ _   \    .'  __ `. \ .-.')|    \  |  ||        |    .-,       /   __  \  |  | _/  /    
| |    \ | | ( ' )  |   /   '  \  \/ `-' \|  ,  \ |  ||   .----' ,-.|  \ _   | ,_/  \__) | (`' ) /     
| |____/ / |(_ o _) /   |___|  /  | `-'`"`|  |\_ \|  ||  _|____  \  '_ /  |,-./  )       |(_ ()_)      
|   _ _ '. | (_,_).' __    _.-`   | .---. |  _( )_\  ||_( )_   | _`,/ \ _/ \  '_ '`)     | (_,_)   __  
|  ( ' )  \|  |\ \  |  |.'   _    | |   | | (_ o _)  |(_ o._)__|(  '\_/ \   > (_)  )  __ |  |\ \  |  | 
| (_{;}_) ||  | \ `'   /|  _( )_  | |   | |  (_,_)\  ||(_,_)     `"/  \  ) (  .  .-'_/  )|  | \ `'   / 
|  (_,_)  /|  |  \    / \ (_ o _) / |   | |  |    |  ||   |        \_/``"   `-'`-'     / |  |  \    /  
/_______.' ''-'   `'-'   '.(_,_).'  '---' '--'    '--''---'                   `._____.'  `--'   `'-'   
                                                                                                
            """
    )
    sleep(2)
    print("And here is the code required to make hello world:\n")
    print(
        ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++."
    )
    sleep(1)
    print("I will now pass it into the interpreter")
    sleep(0.5)
    user_inp = ">+++++++++[<++++++++>-]<.>+++++++[<++++>-]<+.+++++++..+++.[-]>++++++++[<++++>-] <.>+++++++++++[<++++++++>-]<-.--------.+++.------.--------.[-]>++++++++[<++++>- ]<+.[-]++++++++++."
    words = lex(user_inp)
    tokens = tokenise(words)
    program = Program(tokens, tape=Tape(100))

    while tokens and not program.eof:
        program.consume()

    sleep(0.5)
    print("Tada!")
