from my_ui import *
from fractions import Fraction


def calc_fraction(a, b, act, c, d):
    if act == "+":
        return write_line(Fraction(a, b) + Fraction(c, d))
    elif act == "-":
        return write_line(Fraction(a, b) - Fraction(c, d))
    elif act == "*":
        return write_line(Fraction(a, b) * Fraction(c, d))
    elif act == "/":
        return write_line(Fraction(a, b) / Fraction(c, d))
