#Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
#hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują? Do funkcji należy przekazać
#położenie hetmanów

def sprawdzSzachownice(tab):
    for het1 in tab:
        for het2 in tab:
            if het1 == het2:
                continue

            if het1[0] == het2[0] or het1[1] == het2[1]:
                return False

            a = (het1[1] - het2[1])/(het1[0]-het2[0])

            if a == 1.0 or a == -1.0:
                return False
    
    return True


print(sprawdzSzachownice([(1,1), (3, 4), (1, 6)]))