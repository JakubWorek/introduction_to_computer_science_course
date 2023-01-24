#Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi. Proszę
#zaimplementować funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
#(1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
#(2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
#Funkcja powinna zwrócić liczbę znalezionych trójek.

def nwd(a,b):
    while(b):
        a,b=b,a%b
    return a

def trojki(T):
    suma=0

    #brak przerw
    for i in range(len(T)-2):
        if(nwd(T[i],nwd(T[i+1],T[i+2]))==1): suma+=1

    #przerwa pomiędzy pierwszym i drugim
    for i in range(len(T)-3):
        if(nwd(T[i],nwd(T[i+2],T[i+3]))==1): suma+=1

    #przerwa pomiędzy drugim i trzecim
    for i in range(len(T)-3):
        if(nwd(T[i],nwd(T[i+1],T[i+3]))==1): suma+=1

    #przerwa pomiędzy pierwszym i drugim 
    # i przerwa pomiędzy drugim i trzecim
    for i in range(len(T)-4):
        if(nwd(T[i],nwd(T[i+2],T[i+4]))==1): suma+=1

    return suma

print(trojki([1,2,3,5,7,11,13,17]))