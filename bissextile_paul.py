istrue = True
while istrue:
    value = input()
    try:
        int(value)
    except:
        if value == 'sortie':
            istrue = False
        else:
            print('valeur incorrect')
    else:
        intValue = int(value)
        if isinstance(intValue / 4, int):
            if not isinstance((intValue / 4) / 100, int):
                print(value + " est une année bissextile.")
            else:
                print(value + " n'est pas bissextile")
        else:
            print(value + " n'est pas bissextile")
