def maximum(nombres):
    nb = nombres[0]
    for i in nombres : 
        if i > nb :
            nb = i 
    return nb



            


# Tests
assert maximum([98, 12, 104, 23, 131, 9]) == 131
assert maximum([-27, 24, -3, 15]) == 24

print(maximum([98, 12, 104, 23, 131, 9]))