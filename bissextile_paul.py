def main():
    istrue = True
    while istrue:
        value = input()
        if isinstance(value / 4, int):
            if not isinstance((value / 4) / 100, int):
                print(value + "est une année bissextile.")
            else:
                print(value + "n'est pas bissextile")
        elif value == 'sortie':
            istrue = False
        else:
            print('valeur incorrect')
