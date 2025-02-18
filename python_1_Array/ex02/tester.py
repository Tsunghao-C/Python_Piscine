from load_image import ft_load


print("------------------------")
print("Wrong input format")
try:
    print(ft_load(12))
except ValueError as e:
    print(e)


print("------------------------")
print("Wrong path")
try:
    print(ft_load("cat1.jpg"))
except FileNotFoundError as e:
    print(e)


print("------------------------")
print("Empty input")
try:
    print(ft_load(""))
except ValueError as e:
    print(e)


print("------------------------")
print("Missing input")
try:
    print(ft_load())
except TypeError as e:
    print(e)


print("------------------------")
print("Correct input")

try:
    print(ft_load("cat.jpg"))
except ValueError as e:
    print(e)
