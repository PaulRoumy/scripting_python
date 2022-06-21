import argparse


parser = argparse.ArgumentParser()
# parser.parse_args()
parser.add_argument("year")
args = parser.parse_args()
print(args.year)


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
        print("I think it is working. The user entered : " + user_input)
    return user_input


get_input()
