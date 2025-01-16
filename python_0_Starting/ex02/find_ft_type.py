def all_thing_is_obj(obj: any) -> int:
    obj_types = {
        "List" : "list",
        "Tuple" : "tuple",
        "Set" : "set",
        "Dict" : "dict",
        "is in the kitchen" : "str"
    }
    for name, data_type in obj_types.items():
        if (type(obj).__name__ == data_type):
            if data_type == "str":
                print(f"{obj} {name} : {type(obj)}")
            else:
                print(f"{name} : {type(obj)}")
            return 42
    print("Type not found")
    return 42

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Toto")
# print(all_thing_is_obj(10))