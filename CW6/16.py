# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli:
# mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których 
# są zbudowane są identyczne, na przykład ula → 117, 108, 97
# oraz exe → 101, 120, 101. Proszę napisać funkcję wyraz(s1,s2), 
# która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru liter 
# zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna 
# wypisać znaleziony wyraz

def waga(s):
    wei=0
    lSam=0
    for i in range(len(s)):
        if s[i] in ['a','e','i','o','u','y']: lSam+=1
        wei+=ord(s[i])

    return (lSam,wei) 


def wyraz(s1,s2):
    def rek(s1,s2,curr,i):
        #print(s1,curr)
        
        if i>=len(s2):
            if waga(curr) == waga(s1):
                print(curr)
                return True
            else: return False

        return rek(s1,s2,curr,i+1) or rek(s1,s2,curr+s2[i],i+1)
    
    return rek(s1,s2,"",0)

print(wyraz("ula","exeal"))
        