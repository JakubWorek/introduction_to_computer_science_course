# program wyszukujący liczby doskonałe mniejsze od miliona

import math

def doskonala(n):
    suma = -n

    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0 :
            suma += x
            if x != n // x:
                suma += n // x

    if n == suma:
        print(n)

def main():
    for i in range(1, 1000000):
        doskonala(i)

if __name__ == "__main__": main()