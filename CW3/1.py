#Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16

def naSystem(num,base):
    base_num = []
    chars = [str(i) for i in range(10)] + [chr(i) for i in range(ord("A"), ord("F")+1)]
    # print(chars)

    while num > 0:
        base_num.append(chars[num%base])
        num //= base
    
    return "".join(base_num[::-1])

def dectoany(num, base):
    znaki="0123456789ABCDEF"
    wynik=""
    while(num>0):
        indeks=num%base
        wynik=znaki[indeks]+wynik
        num//=base

    return wynik

def main():
    print(dectoany(256,16))

if __name__ == "__main__": main()