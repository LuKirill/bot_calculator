from calculations import div, mult, diff, sum
from my_ui import write_line


def integer(act, num1, num2):
    if act == "+":
        return write_line(sum(num1, num2))
    elif act == "-":
        return write_line(diff(num1, num2))
    elif act == "*":
        return write_line(mult(num1, num2))
    elif act == "/":
        if num2 == 0:
            return write_line("∞")
        elif num2 == 0 and num1 == 0:
            return write_line("nan")
        else:
            return write_line(div(num1, num2))