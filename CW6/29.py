#Punkt leżący w przestrzeni jest opisywany trójką liczb typu float (x,y,z). Tablica T[N] zawiera
#współrzędne N punktów leżących w przestrzeni. Punkty posiadają jednostkową masę. Proszę napisać funkcję,
#która sprawdza czy istnieje podzbiór punktów liczący co najmniej 3 punkty, którego środek ciężkości leży w
#odległości nie większej niż r od początku układu współrzędnych. Do funkcji należy przekazać tablicę T oraz
#promień r, funkcja powinna zwrócić wartość typu bool.

from math import sqrt

def wektor_na_dlugosc(a,b,c):
    return sqrt((a**2)+(b**2)+(c**2))

def rekurencjaop(T,r,iT=0,iS=0,a=0,b=0,c=0):
    if iS >= 3:
        if wektor_na_dlugosc(a/iS,b/iS,c/iS) < r:
            print(wektor_na_dlugosc(a/iS,b/iS,c/iS))
            return True

    return rekurencjaop(T,r,iT+1,iS+1,a + T[iT][0], b + T[iT][1], c + T[iT][2]) or rekurencjaop(T,r,iT+1,iS,a,b,c)


lista_tupl = [(10,21,69),(12,22,-420)]

print(rekurencjaop(lista_tupl,79))