def all_thing_is_obj(object: any) -> int:
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String",

    }
    type_name = types.get(type(object), None)
    if type_name == "String":
        print(f"{object} is in the kitchen : {type(object)}")
    elif type_name:
        print(f"{type_name} : {type(object)}")
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