#Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
#cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001

def czyCyfry(l1,l2):
    cyfry=[0 for _ in range(10)]

    while(l1>0):
        cyf=l1%10
        cyfry[cyf]+=1
        l1//=10
    
    while(l2>0):
        cyf=l2%10
        cyfry[cyf]-=1
        l2//=10

    for i in range(10):
        if(cyfry[i]!=0): return False

    return True

def main():
    print(czyCyfry(61,16))

if __name__ == "__main__": main()