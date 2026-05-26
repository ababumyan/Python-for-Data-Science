def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object is None:
        print(f"Nothing: None {type(object)}")
        return 0
    elif obj_type is float:
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif obj_type is int:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif obj_type is str and object == "":
        print(f"Empty: {object} {type(object)}")
        return 0
    elif obj_type is bool:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not found!")
        return 1


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
