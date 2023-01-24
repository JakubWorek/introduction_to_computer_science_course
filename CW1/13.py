#  program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb

def nwd(a,b):
    while (b>0):
        c = a % b
        a = b
        b = c
    return a

def nww(a,b):
    return int((a*b)/nwd(a,b))

def main():
    l1=1
    l2=3
    l3=4
    print(nww(nww(l1,l2),l3))

if __name__ == "__main__": main()