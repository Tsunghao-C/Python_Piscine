from .count_in_list import count_in_list

# __init__.py serves as the package's entry point
# Here you define what gets "EXPOSED" when someone else
# import this pacakge.

# from .count_in_list -> means look for the "count_in_list" module
# in this package
# you can have several modules in a package

from .calculation import num_plus_one

# you can do "from ft_package import num_plus_one" directly
# however, we need to explicitly say "calculation.num_minus_one()"
# function since it is not exposed here
