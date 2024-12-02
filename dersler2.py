# 3 basamaklı sayıların kaç tanaesi rakamların küplerine toplamına eşittir? **3
liste = []
liste2 = []
ucbasamak = range(100, 1000)

for sayi in ucbasamak:
    kupu = sayi ** 3
    birlesme = str(kupu)
    for rakam in birlesme:
    	liste2.append(int(rakam))
    	toplam = sum(liste2)
    	if sayi == toplam:
    	  liste.append(sayi)
print(len(liste))