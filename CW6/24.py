#Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
#wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
#2 niepustych podzbiorów tego zbioru

from math import inf
from math import sqrt

def centerOfGravity(points):
    if(len(points)==0): return inf,inf
    x = 0
    y = 0
    for point in points:
        x += point[0]
        y += point[1]
    return (x/len(points), y/len(points))

def euklidesLength(point1,point2):
    if(point1==(inf,inf) or point2==(inf,inf)): return inf
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def rek(T,taken=0,points1=[],points2=[]):
    n=len(T)

    if(taken==n):
        return euklidesLength(centerOfGravity(points1),centerOfGravity(points2))

    return min(rek(T,taken+1,points1,points2),\
        rek(T,taken+1,[*points1,T[taken]],points2),\
        rek(T,taken+1,points1,[*points2,T[taken]]))

T=[(2, 2), (3, 3), (1, 2)]
print(rek(T))