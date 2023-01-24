# sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗sqrt(0.5))) ∗ ... 
# ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π

from math import sqrt

def main():
    res=sqrt(0.5)
    last=res
    delta:float=1

    while(delta != 0):
        last = sqrt(0.5 + 0.5 * last)
        newRes = res * last
        delta = newRes - res
        res = newRes

    print(2/res)

if __name__ == "__main__": main()