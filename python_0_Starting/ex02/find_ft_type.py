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