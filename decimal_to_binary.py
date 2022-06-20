def decimal_to_binary(dec_val):
    """

    :param dec_val: take decimal number
    :type dec_val: int
    """
    if dec_val >= 1:
        decimal_to_binary(int(dec_val // 2))
        print(dec_val % 2, end='')


dec_val = int(input("Nombre décimal :  \n"))
decimal_to_binary(str(dec_val))
