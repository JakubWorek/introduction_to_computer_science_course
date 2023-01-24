#Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n > 1) powtórzenie innego napisu o długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana
#jest tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
#napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.

def split(txt,ile):
    dlugosc = len(txt)
    if dlugosc % ile != 0:
        return []
    i = 0
    result = [[0]*ile for _ in range(dlugosc//ile)]
    for x in range(dlugosc):
        if x % ile == 0 and x != 0:
            i += 1
        result[i][x%ile] = txt[x]
    return result

def flag(T):
    for word in T:
        if word != T[0]:
            return False
    return True

def podciag(txt):
    leng = len(txt)
    if leng < 2:
        return 0
    for i in range(leng//2,0,-1):
        r = split(txt,i)
        if flag(r) and r!= []:
            return leng
    return 0

def multi(T):
    max_len = 0
    for txt in T:
        print(podciag(txt))
        max_len = max(podciag(txt), max_len)
    return max_len

T = ["ABCABCABC","AAAA","ABAABA","ABC"]

print(multi(T))