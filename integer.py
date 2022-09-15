from my_ui import write_line
from telegram import Update


def integer(x, act, y):
    if act == "+":
        return write_line(f'{x} {act} {y} = {x + y}')
    elif act == "*":
        return write_line(f'{x} {act} {y} = {x * y}')
    elif act == "-":
        return write_line(f'{x} {act} {y} = {x - y}')
    elif act == "/":
        if y == 0:
            return write_line("∞")
        else:
            return write_line(f'{x} {act} {y} = {x / y}')