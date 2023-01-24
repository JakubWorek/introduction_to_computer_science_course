# ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Napisać program, który znajdzie wyraz
# początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

def AodN(an):
    return (an % 2) * (3 * an + 1) + (1 - an % 2) * an / 2

def main():
    best=0
    wyraz=0
    for start in range(2,10001):
        proba=0
        an=start
        while(an != 1):
            proba+=1
            an=AodN(an)
        if(best<proba):
            best=proba
            wyraz=start

    print(wyraz)

if __name__ == "__main__": main()