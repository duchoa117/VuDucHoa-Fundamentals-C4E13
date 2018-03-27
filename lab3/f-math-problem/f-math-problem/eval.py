from random import randint,choice
op = choice(['+','-','*',"/"])
def calc(x, y, op): # ngam dinh

    if op == '+':
        f = x + y
    if op == '-':
        f = x-y
    if op == '*':
        f = x*y
    if op == '/':
        f = x/y
    return f








# print(f)
# argument, parameter ( gia tri truyen vao)
# calc(1, 7, '+')
