def equilateral(sides):
    a, b, c = sides
    return _is_valid_triangle(sides) and (
        a == b
        and b == c
    )

def isosceles(sides):
    a, b, c = sides
    return _is_valid_triangle(sides) and (
        a == b
        or a == c
        or b == c
    )

def scalene(sides):
    a, b, c = sides
    return _is_valid_triangle(sides) and (
        a != b
        and a != c
        and b != c
    )

def _is_valid_triangle(sides):
    a, b, c = sides
    return (
        a != 0
        and b != 0
        and c != 0
        and a + b >= c
        and a + c >= b
        and b + c >= a
    )

