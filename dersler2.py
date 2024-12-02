# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3 153 gibi = 1 küp 5 küp 3 küp farklı optimizasyonlar yapılabilir
liste = []
liste2 = []
liste3 = []

ucbasamak = range(100, 1000)

for sayi in ucbasamak:
    birlesme = str(sayi)
    for rakam in birlesme:
      liste2.append(int(rakam))
	  for eleman in liste2:
        elemankup = eleman ** 3
    	liste3.append(elemankup)
        toplam = sum(liste3)
    	    if sayi == toplam:
    	      liste.append(sayi)
print(len(liste))