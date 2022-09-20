from my_ui import *
from fractions import Fraction


def calc_fraction(a, b, act, c, d):
    if act == "+":
        if b == 0 or d == 0:
            return "∞"
        else:
            return write_line(Fraction(a, b) + Fraction(c, d))
    elif act == "-":
        if b == 0 or d == 0:
            return "∞"
        else:
            return write_line(Fraction(a, b) - Fraction(c, d))
    elif act == "*":
        if b == 0 or d == 0:
            return "∞"
        else:
            return write_line(Fraction(a, b) * Fraction(c, d))
    elif act == "/":
        if b == 0 or d == 0:
            return "∞"
        else:
            return write_line(Fraction(a, b) / Fraction(c, d))
