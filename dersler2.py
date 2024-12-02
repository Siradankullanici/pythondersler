# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3 153 gibi = 1 küp 5 küp 3 küp farklı optimizasyonlar yapılabilir
liste = list(range(100, 1000))
liste2 = []
for sayi in liste:
    sayi2 = str(sayi)
    for rakam in sayi2:
        kup = rakam ** 3
        liste2.append(kup)
        sum(liste2)
