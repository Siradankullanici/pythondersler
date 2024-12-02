# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3 153 gibi = 1 küp 5 küp 3 küp farklı optimizasyonlar yapılabilir
liste1 = list(range(100, 1000))
liste2 = []
liste3 = []

for eleman in liste1:
    eleman_str = str(eleman)
    for harf in eleman_str:
        harf_int = int(harf)
        harf_kup = harf_int ** 3
        liste3.append(harf_kup)
        toplam = sum(liste3)
        if eleman == toplam:
            liste2.append(sayi)
print(len(liste2))