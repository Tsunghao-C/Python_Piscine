from give_bmi import give_bmi, apply_limit


height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# Error cases
try:
    # list size not the same
    bmi = give_bmi([1.75, 1.8, 1.65], [66, 77])
except ValueError as e:
    print(e)

try:
    # height is 0
    bmi = give_bmi([0, 1], [66, 77])
except ValueError as e:
    print(e)

try:
    # empty input
    bmi = give_bmi([], [66, 77])
except ValueError as e:
    print(e)

try:
    # list value not int or float
    bmi = give_bmi(["1.75", "1.8"], ["66", 77])
except ValueError as e:
    print(e)