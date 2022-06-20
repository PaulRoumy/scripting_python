string_list: list[str] = ["101000001", "01000010", "1000011", "1000100"]
"print(string_list)"


def string_list_transform():
    """
    turning string list into single string
    :rtype: string list
    """
    new_string_list = "".join(string_list)
    print(new_string_list)
    print(type(new_string_list))
    print("est-ce que c'est ok de laisser les prints ?")
    return new_string_list


string_list_transform()
