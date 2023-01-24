#Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę
#napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących
#na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.

def field(sq)->int:
    x1,x2,y1,y2=sq
    return((x2-x1)*(y2-y1))

    
def doOverlap(sq1,sq2):
    x1,x2,y1,y2=sq1
    a1,a2,b1,b2=sq2

    if(x1<a1 and x2<a2) or (x1>a2 and x2>a2) or (a1<x1 and a2<x1) or (a1>x2 and a2>x2):
        return False

    if(y1<b1 and y2<b2) or (y1>b2 and y2>b2) or (b1<y1 and b2<y1) or (b1>y2 and b2>y2):
        return False

    if((x1<=a1<=x2<=a2) or (a1<=x1<=a2<=x2)):
        if((y2<b1) or (b2<y1)): return False

    if((y1<=b1<=y2<=b2) or (b1<=y1<=b2<=y2)):
        if((x2<a1) or (a2<x1)): return False

    return True


def rek(T,P,i=0,suma=0,zost=13,cnt=0):
    if(suma==2012 and zost==0): return True
    if(suma>2012): return False
    if(i==len(T)): return False

    for j in range(cnt):
        if(doOverlap(T[i],T[P[j]])):
            break
    else:
        if(rek(T,P,i+1,suma,zost,cnt)):
            return True

        P[cnt]=i
        return rek(T,P,i+1,suma+field(T[i]),zost-1,cnt+1)

    return rek(T,P,i+1,suma,zost,cnt)


T = [(1, 11, 11, 21),
    (11, 21, 31, 41),
    (21, 31, 51, 61),
    (31, 41, 71, 81),
    (41, 51, 91, 101),
    (51, 61, 111, 121),
    (61, 71, 131, 141),
    (71, 81, 151, 161),
    (81, 91, 171, 181),
    (91, 101, 191, 201),
    (101, 103, 201, 203),
    (103, 105, 204, 206),
    (105, 106, 206, 208)]

P=[0 for _ in range(len(T))]

print(P)

print(rek(T,P))

print(P)