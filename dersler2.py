# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3 153 gibi = 1 küp 5 küp 3 küp farklı optimizasyonlar yapılabilir
liste1 = list(range(100, 1000))
liste2 = []


for eleman in liste1:
    elemankup = eleman ** 3
    liste2.append(elemankup)
    toplam = sum(liste2)
    if eleman == toplam:
        liste2.append(sayi)
print(len(liste2))