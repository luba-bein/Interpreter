from lexer import Lexer
from pars import Parser
from transfer_to_pn import PN
from stack_machine import Stack_machine
from triad_processing import Triad

f = open('tests/test1.txt')
inp = f.read()
f.close()

# converting code into a sequence of tokens
print('\nlexer:')
lexer = Lexer()
tokens = lexer.tokenizing(inp)

# parser checks code for errors
parser = Parser(tokens)
pars = parser.parsing()
print('\nparser:', pars)

if pars:
    # transfer of expressions to Polish notation
    polish_notation = PN(tokens)
    pn_main, function_list = polish_notation.transfer_PN()

    # converting tokens into a sequence of triads and simplifying them
    triad = Triad(pn_main, function_list)
    triads, val = triad.triad_op()
    for i in range(len(function_list)):
        print("\nFunctions triads processing:")
        triad = Triad(function_list[i][-1], function_list)
        function_list[i][-1] = triad.triad_op(False)

    # calculating values using a stack machine
    print('\nstack machine:')
    stack_machine = Stack_machine(triads, val, function_list)
    stack_machine.stack_machine_run()
