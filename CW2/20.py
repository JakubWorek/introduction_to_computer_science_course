#Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry. Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
#2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
#taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
#podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).

def common_digit(num1,num2,base):
    D=[False]*base

    while(num1!=0):
        d = num1 % base
        D[d]=True
        num1//=base
    
    while(num2!=0):
        if(D[num2%base]==True): return True
        num2//=base

    return False


def main():
    l1=int(input("Liczba1: "))
    l2=int(input("Liczba2: "))

    for bas in range(2,17):
        if(not common_digit(l1,l2,bas)):
            print(bas)
            break
    else:
        print("Nie ma takiego systemu")
    

if __name__ == "__main__": main()