from array2D import slice_me


family = [
    [1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]
]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))

# Error cases
try:
    # not a list
    slice_me("Not a list", 0, 1)
except ValueError as e:
    print(e)


try:
    # Empty list
    slice_me([], 0, 1)
except ValueError as e:
    print(e)


try:
    # not 100% a 2D list
    slice_me([[1, 2], "not a list", [32, 4.4]], 0, 1)
except ValueError as e:
    print(e)


try:
    # not an aligned 2D list
    slice_me([[1, 2, 3], [4, 5], [6, 7, 8]], 0, 1)
except ValueError as e:
    print(e)


try:
    # not a 2D list
    slice_me([[[0, 0], [0, 1]], [[1, 0], [1, 1]], [[2, 0], [2, 1]]], 0, 1)
except ValueError as e:
    print(e)
