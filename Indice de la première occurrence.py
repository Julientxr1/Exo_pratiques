def indice(element, tableau):
    n = -1
    for i in tableau :
        n += 1
        if element == i :
            return n
    return None

# tests

assert indice(1, [10, 12, 1, 56]) == 2
assert indice(1, [1, 50, 1]) == 0
assert indice(15, [8, 9, 10, 15]) == 3
assert indice(1, [2, 3, 4]) is None

print(indice(4, [2, 25, 5, 67, 35, 4, 78, 0]))
