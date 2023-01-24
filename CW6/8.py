#Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.

def waga(T,r,i):
    if(r==0): return True
    if(r<0 or i>=len(T)): return False
    return waga(T,r-T[i],i+1) or waga(T,r,i+1) or waga(T,r+T[i],i+1)
            #biore odwaznik         #nie biore      #daje do masy