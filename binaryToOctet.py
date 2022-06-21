def binaryToOctet(binarylist: list) -> list:
    """
    :param binarylist:
    :type binarylist:
    :return octetlist:
    :rtype list:
    """
    octetlist = list
    #Foreach element in binarylist check if int value can be divised by 8
    for binary in binarylist:
        while binary % 8 == 0 is False :
                binary = "0" + binary
        octetlist.append(binary)
    return octetlist
