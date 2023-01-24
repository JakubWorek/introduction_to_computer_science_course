#Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
#która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
#równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
#znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def lonIndSeq(T):
    N=len(T)
    maxLeng=1
    indSum=0
    elSum=T[0]
    leng=1

    for i in range(1,N):
        if(T[i-1]<T[i]):
            elSum+=T[i]
            indSum+=i
            leng+=1
        else:
            if(leng>maxLeng and elSum==indSum):
                maxLeng=leng
            leng=1
            indSum=i
            elSum=T[i]

    if(leng>maxLeng and elSum==indSum):
        maxLeng=leng
    
    return maxLeng
        
print(lonIndSeq([0,1,2]))