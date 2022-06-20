def strHexal(datastr: str) -> list:
    """
    :param datastr:
    :type datastr:
    :return hexallist:
    :rtype list:
    """
    hexal = ""
    hexallist =list
    for character in datastr:
        if len(hexal) == 6:
            hexallist.append(hexal)
            hexal = ""
        else: hexal = hexal + character
    hexallist.append(hexal)
    return hexallist
