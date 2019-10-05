from itertools import zip_longest

class Polynomial(object):
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def evaluate(self, x):
        sum = self.coefficients[0]
        xpow = x
        for i in range(1,len(self.coefficients)):
            sum += self.coefficients[i] * xpow
            xpow *= x

        return sum

    def __mul__(self, other):
        coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                coeffs[i+j] += a*b

        while len(coeffs) > 0 and coeffs[-1] == 0:
            print("remove last element: %s" % (coeffs))
            coeffs.pop(-1)

        return Polynomial(coeffs)

    def __add__(self, other):
        coeffs = [
            sum(x) for x in zip_longest(self.coefficients, other.coefficients, fillvalue=0.)
        ]
        return Polynomial(coeffs)

    def __repr__(self):
        msg = ""
        for c in self.coefficients:
            msg += "%s," % c
        return msg

