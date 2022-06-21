def resizeStr(strdata: str) -> str:
    """
    :param strdata:
    :type strdata:
    :return resizedstr:
    :rtype str
    """
    resizedstr = strdata
    while resizedstr % 8 == 0 is False:
        resizedstr = resizedstr + "="
    return resizedstr
