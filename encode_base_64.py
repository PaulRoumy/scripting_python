def get_input():
    """
     Function getting the user input
    :return: the user input
    :rtype: a string
    """
    user_input = input("enter a string : ")
    try:
        str(user_input)
    except:
        print("Houston, we've got a problem.")

    else:
        print("I think it is working.")
    return user_input

get_input()
