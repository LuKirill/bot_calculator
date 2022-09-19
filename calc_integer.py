def calc_integer(x, act, y):
    if act == "+":
        return f'{x} {act} {y} = {x + y}'
    elif act == "*":
        return f'{x} {act} {y} = {x * y}'
    elif act == "-":
        return f'{x} {act} {y} = {x - y}'
    elif act == "/":
        if y == 0:
            return "∞"
        else:
            return f'{x} {act} {y} = {x / y}'
