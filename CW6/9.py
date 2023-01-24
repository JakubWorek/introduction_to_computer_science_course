#Poprzednie zadanie, ale wypisać odważniki.
stop=False

def waga(T,r,i=0,res=[]):
    global stop
    if(stop): return False
    if(r==0):
        print(res)
        stop=True
        return True
    if(r<0 or i>=len(T)): return False
    return waga(T,r-T[i],i+1,res+[T[i]]) or waga(T,r,i+1,res) or waga(T,r+T[i],i+1,res+[-(T[i])])
            #biore odwaznik         #nie biore      #daje do masy