sozluk = []
asalsayisi = 0
asalsayisi2 = []
prime = True
sayi = 0
while asalsayisi <= 10000:
 for i in range(2, sayi): #bütün doğal sayılar 1'e bölünür
    if sayi %i == 0:
        prime = False
        break
    else:
        prime = True
 if prime == True:
        print(f"{sayi} sayisi asaldir")
        sozluk.append(sayi)
        asalsayisi +=1
        asalsayisi2.append(asalsayisi)
        sayi += 1
 else:
        print(f"{sayi} sayisi asal degildir")
        sayi += 1

temizsozluk = []
temizsozluksayisi = 0
for i in sozluk:
    if str(i).startswith("3") and str(i).endswith("7"):
     temizsozluk.append(i)
     temizsozluksayisi += 1

print(temizsozluk)
print(temizsozluksayisi)

#tamsozluk = list(zip(sozluk, asalsayisi2))

#print(tamsozluk)

""" sayi = int(input("Lütfen geçerli bir sayi giriniz: "))

prime = True
for i in range(2, sayi): #bütün doğal sayılar 1'e bölünür
    if sayi %i == 0:
        prime = False
        break
if prime == True:
    print(f"{sayi} sayisi asaldir")
else:
    print(f"{sayi} sayisi asal degildir")
sayi = int(input("Bir sayi giriniz: "))
 """


















""" 
liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

for harf in liste1:
    for rakam in liste2:
        print(harf, rakam)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9] """

""" for harf in metin:
    if harf in sozluk:
       sozluk[harf] += 1
    else:
       sozluk[harf] = 1

for harf, adet in sozluk.items():
    print(harf, adet) """