def strHexal(datastr: str) -> list[str]:
    """
    :param datastr:
    :type datastr:
    :return hexallist:
    :rtype list:
    """
    hexal = ""
    hexallist =list[str]
    for character in datastr:
        if len(hexal) == 6:
            hexallist.append(hexal)
            hexal = ""
        else: hexal = hexal + character
    hexallist.append(hexal)
    return hexallist
