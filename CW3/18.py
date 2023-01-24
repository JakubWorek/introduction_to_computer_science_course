#Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
#funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
#z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
#podciągu lub wartość 0 jeżeli taki podciąg nie istnieje

def czyPalindrom(s:str):
    i=0
    j=len(s)-1

    while(i<j):
        if(s[i]!=s[j]): return False
        i+=1; j-=1

    return True


def czyspojnypalindrom(T):
    maxlen=0
    currlen=0

    pal=""

    i=0
    while(i<len(T)):
        if(T[i]%2==1):
            currlen=1
            pal+=str(T[i])

            j=i+1
            while(T[j]%2==1):
                currlen+=1
                pal+=str(T[j])
                j+=1

            print(pal)
            
            if(czyPalindrom(pal)):
                if(currlen>maxlen): maxlen=currlen

        pal=""
        i+=1

    return maxlen


tab=[0,1,3,4,3,5,3,6,8]
print(czyspojnypalindrom(tab))