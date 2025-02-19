def all_thing_is_obj(obj: any) -> int:
    obj_types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    type_name = obj_types.get(type(obj), "Type not found")
    if type(obj) is str:
        print(f"{obj} is in the kitchen : {type(obj)}")
    elif type_name in obj_types.values():
        print(f"{type_name} : {type(obj)}")
    else:
        print(type_name)
    return 42

# type(obj) returns the type of the object
# use "is" to compare datatype, mem address
# use "==" operator to comparet the referenced value
