# This tester demos the efficiency between list comprehension and Generator
import time
import sys


g_family = [[i] for i in range(1000000)] + [5] + [[j] for j in range(1000000)]

# Check time usage
# List comprehension
start_time = time.time()
result1 = all([isinstance(row, list) for row in g_family])
end_time = time.time()
print(f"List comprehension time: {end_time - start_time:.4f} seconds")

# Generator expression
start_time = time.time()
result2 = all(isinstance(row, list) for row in g_family)
end_time = time.time()
print(f"Generator expression time: {end_time - start_time:.4f} seconds")

# Check memory usage
list_version = [isinstance(row, list) for row in g_family]
gen_version = (isinstance(row, list) for row in g_family)
print(f"\nMemory size of list version: {sys.getsizeof(list_version)} bytes")
print(f"Memory size of generator version: {sys.getsizeof(gen_version)} bytes")
