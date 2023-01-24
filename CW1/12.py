# program wyznaczający największy wspólny dzielnik 3 zadanych liczb

def nwd(a,b):
    while (b>0):
        c = a % b
        a = b
        b = c
    return a

def main():
    l1=40
    l2=44
    l3=36
    print(nwd(nwd(l1,l2),l3))

if __name__ == "__main__": main()