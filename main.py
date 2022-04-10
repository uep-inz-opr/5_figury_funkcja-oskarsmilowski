import math

def licz_pole(*args):
    if len(args) == 1:
        return math.pi*(args[0]**2)
    elif len(args) == 2:
        return args[0]*args[1]
    elif len(args) == 3:
        p = (args[0] + args[1] + args[2])/2
        return math.sqrt(p * (p-args[0]) * (p-args[1]) * (p-args[2]))
    else:
        return "Błąd"     

def main():
    liczba_figur = int(input())
    figury = []
    for _ in range(liczba_figur):
        figura = input()
        figury.append(figura)
    wynik = 0.0

    for figura in figury:
        figura = figura.split(' ')
        figura = [float(x) for x in figura]
        pole = licz_pole(*figura)
        if pole == "Błąd":
            print("Błąd: można podać maksymalnie 3 liczby")
            return
        else:
            wynik += pole
        
    wynik = round(wynik, 2)
    print(wynik)
    

if __name__ == '__main__':
    main()