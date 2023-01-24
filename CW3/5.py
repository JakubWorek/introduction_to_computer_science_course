#program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
#wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów

#KOLEJKA PRIORYTETOWA O 10 MIEJSCACH

def insert(num,ind,tab):
    for i in range(0,ind):
        tab[i]=tab[i+1]
    #end for
    tab[ind]=num

    return tab

def isUnique(num,tab):
    for i in range(len(tab)):
        if (num == tab[i]): return False
    #end for

    return True

def findNthBiggest(n):
    tab=[0 for _ in range(n)]
    liczba=1

    while(liczba!=0):
        liczba=int(input("Liczba: "))
        if(isUnique(liczba,tab)):
            index=-1
            for i in range(n-1,-1,-1):
                if(tab[i]<liczba):
                    index=i
                    tab=insert(liczba,index,tab)
                    break
        #print(tab)
    #end while 

    return tab[0]
            

def main():
    print(findNthBiggest(10))

if __name__ == "__main__": main()