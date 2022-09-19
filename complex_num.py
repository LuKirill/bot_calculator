def complex_num(k, m, comp_act, f, n):
    class ComplexNumber:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __add__(self, other):
            return f'z = {self.a + other.a} + ({self.b + other.b} * i)'

        def __mul__(self, other):
            return f'z = {self.a * other.a - (self.b * other.b)} + ({self.b * other.a} * i)'

        def __sub__(self, other):
            return f'z = {self.a - other.a} + ({self.b - other.b} * i)'

        def __truediv__(self, other):
            return f'z = {(self.a * other.a + self.b * other.b) / (other.a * other.a + other.b * other.b)}' \
                   f' - ({(self.a * other.b - self.b * other.a) / (other.a * other.a + other.b * other.b)} * i)'

    z_1 = ComplexNumber(k, m)
    z_2 = ComplexNumber(f, n)
    if comp_act == "+":
        return z_1 + z_2
    if comp_act == "-":
        return z_1 - z_2
    if comp_act == "*":
        return z_1 * z_2
    if comp_act == "/":
        return z_1 / z_2
