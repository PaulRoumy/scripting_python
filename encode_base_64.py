import argparse
import step2


def get_user_string_in_args():
    parser = argparse.ArgumentParser()
    # parser.parse_args()
    # parser.add_argument("string", help="letters", type=str)
    # parser.add_argument("echo",  help="echo the string you enter")

    parser.add_argument("-t", "--text_to_encode", help="encode in base 64", type=str)
    # parser.add_argument("-n", "--number", help="encode in base 64", type=int)
    args = parser.parse_args()
    print(args.text_to_encode)
    user_string_input = args.text_to_encode
    return user_string_input

    # def get_input():
    """
     Function getting the user input
    :return: the user input
    :rtype: a string
    """


#     user_input = input("enter a string : ")
#     try:
#         str(user_input)
#     except:
#         print("Houston, we've got a problem.")
#
#     else:
#         print("I think it is working. The user entered : " + user_input)
#     return user_input
#
#
# get_input()


# get_user_string_in_args()

step2.step2(get_user_string_in_args())
