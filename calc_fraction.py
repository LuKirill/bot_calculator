from calculations import div, mult, diff, sum
from my_ui import write_line
from fractions import Fraction


def calc_fraction(act, a, b, c, d):
    if act == "+":
        return write_line(sum(Fraction(a, b), Fraction(c, d)))
    elif act == "-":
        return write_line(diff(Fraction(a, b), Fraction(c, d)))
    elif act == "*":
        return write_line(mult(Fraction(a, b), Fraction(c, d)))
    elif act == "/":
        return write_line(div(Fraction(a, b), Fraction(c, d)))