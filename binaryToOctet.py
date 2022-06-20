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
        isOctet = False
        while not isOctet:
            if isinstance(int(binary) / 8, int):
                isOctet = True
            # if not add a zero before the value and retry
            else:
                binary = "0" + binary
        octetlist.append(binary)
    return octetlist
