# program wczytujący trzy liczby naturalne a,b,n i wypisujący rozwinięcie dziesiętne
#ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej

def main():
    a=int(input("podaj licznik:"))
    b=int(input("podaj mianownik:"))
    n=int(input("podaj dokladnosc:"))

    print(a//b, "." if a%b != 0 else "", sep="", end="")
    a %= b
    while a > 0 and n > 0:
        a *= 10
        print(a//b, end="")
        a %= b
        n -= 1
    
if __name__ == "__main__": main()