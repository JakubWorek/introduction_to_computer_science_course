# Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
#różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie.

def szukaj(num,mask):
    result = 0
    prawa=num%mask
    lewa=num//(mask*10)

    lewa *= mask
    new_num=lewa+prawa

    if(new_num % 7 == 0 and new_num != 0): result+=1

    if(mask<new_num): result += szukaj(new_num,mask)
    if(mask*10<num): result+=szukaj(num,mask*10)

    return result


def main():
    liczba=int(input("podaj liczbe o nie powtarzajacych sie cyfach: "))
    print(szukaj(liczba,1))

if __name__ == "__main__": main()