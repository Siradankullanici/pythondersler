# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3 153 gibi = 1 küp 5 küp 3 küp farklı optimizasyonlar yapılabilir
liste1 = list(range(100, 1000))
liste2 = []
liste3 = []
eleman_tmp = []
for eleman in liste1:
    eleman_str = str(eleman)
    for rakam in eleman_str:
        rakam = int(rakam)   
        harf_kup = rakam ** 3
        liste3.append(harf_kup)
        eleman_tmp.append(eleman)
print(liste3)
liste3_toplam = sum(int(liste3))          
if str(eleman_tmp) == str(liste3_toplam):
    liste2.append(eleman)
    liste3.clear()
    eleman_tmp.clear()
else:
    liste3.clear()
    eleman_tmp.clear()
print(liste2)
print(len(liste2))