# Brainfuck Interpreter

This is a simple Brainfuck interpreter written in Python. Brainfuck is an esoteric programming language known for its minimalistic design, consisting of only eight commands.

![Screenshot 2023-10-31 at 11 57 37](https://github.com/sikorosenai/ByteMeIfYouCan/assets/39854416/20ec0183-bd72-40db-b6c5-a6d7620b451e)


The language is also Turing complete.

## Usage

Before running the interpreter, set the Python path:

`$ export PYTHONPATH=. `


## Running the Interpreter

To enter the interpreter environment, use the following command in the root folder:

`$ python interpreter/main.py`

To run a Brainfuck script, provide the path to the script:

`$ python interpreter/main.py temp_script.txt`

For a quick demonstration of the interpreter, you can run:

`$ python interpreter/main.py demo`

## Running Tests
To run tests, use the following command:

`$ pytest -v`
