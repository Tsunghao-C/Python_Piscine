# `is` used to compare if mem address, us 'is' for None (NULL) comparison
# `==` used to compare if value is identical
# Nan is a special case that "nan is nan" is alwasy false. Use str(number) == 'nan' or math.isnan() instead!

def NULL_not_found(object: any) -> int:
    null_values = {"Nothing" : None,
                   "Cheese" : float("NaN"),
                   "Zero" : 0,
                   "Empty" : '',
                   "Fake" : False}
    if isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese : nan {type(object)}")
        return 0
    for key, value in null_values.items():
        if object is value:
            print(f"{key}: {value} {type(object)}")
            return 0
    print("Type not Found")
    return 1

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ''
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))