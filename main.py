import math

def pole_kola(r):
    return math.pi*r**2

def pole_prostokata(a,b):
    return a*b

def pole_trojkata(a,b,c):
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))



def main():
    liczba_figur = int(input())
    figury = []
    for i in range(liczba_figur):
        figura = input()
        figury.append(figura)

    print(figury)

if __name__ == '__main__':
    main()