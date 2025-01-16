def all_thing_is_obj(obj: any) -> int:
    obj_type = type(obj).__name__
    if (obj_type == "list"):
        print(f"List : {type(obj)}")
    elif (obj_type == "tuple"):
        print(f"Tuple : {type(obj)}")
    elif (obj_type == "set"):
        print(f"Set : {type(obj)}")
    elif (obj_type == "dict"):
        print(f"Dict : {type(obj)}")
    elif (obj_type == "str"):
        print(f"{obj} is in the kitchen : {type(obj)}")
    else:
        print("Type not found")
    return 42

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))