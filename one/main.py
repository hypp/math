
import polynomial

def test():
    p1 = polynomial.Polynomial([13/5,1/5])
    s2 = p1.evaluate(2)
    s7 = p1.evaluate(7)

    print("f(2) = %s f(7) = %s" % (s2,s7))

def calc_term(points, i):
    print("-> calc_term: %s, %i" % (points, i))
    term = polynomial.Polynomial([1.])
    xi, yi = points[i]

    for j,p in enumerate(points):
        print("i: %s j: %s p: %s" % (i, j, p))
        if j == i:
            continue

        xj = p[0]
        term = term * polynomial.Polynomial([-xj / (xi - xj), 1.0 / (xi -xj)])

    term = term * polynomial.Polynomial([yi])
    print("<- calc_term: %s" % (term))
    return term

def interpolate(points):
    print("->interpolate: %s" % (points))
    if len(points) == 0:
        raise ValueError("Need at least one point")

    # extract all x from x,y pairs
    x_s = [p[0] for p in points]
    # check that all x_s are unique
    if len(set(x_s)) != len(x_s):
        raise ValueError("All x must be unique")

    # check that all x_s are larger than previous
    for i in range(1, len(x_s)):
        if x_s[i] <= x_s[i-1]:
            raise ValueError("x n must be larger tha x n-1")

    # Calcluate the terms of the polynomial
    # Loop through all points
    terms = [calc_term(points, i) for i in range(0, len(points))]
    s = sum(terms, polynomial.Polynomial([]))
    print("<-interpolate: %s" % s)
    return s

if __name__ == "__main__":
    test()

    points1 = [(1,1)]
    poly1 = interpolate(points1)
    print("poly1: %s" % (poly1))

    points2 = [(1,1), (2,0)]
    poly2 = interpolate(points2)
    print("poly2: %s" % (poly2))

    points3 = [(1,1), (2,4), (7,9)]
    poly3 = interpolate(points3)
    print("poly3: %s" % (poly3))
