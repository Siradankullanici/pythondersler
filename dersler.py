isim = "isiminizi giriniz"
ali = '\nALI\t BABAPRO'.lower().capitalize()

print(isim[::2].upper()+ ali[0::4], isim[0::4].lower().capitalize().startswith("is"))
print(isim[0::4].lower().capitalize())

sayi30 = 4.234

sayi32 = 5

sayi49 = 5**100

print(sayi30)
print(type(sayi30), type(sayi32))
print(sayi49)

sayi50 = 22.001 / 7

print(sayi50)

print(3 + 4)

print(4 - 5)

print(16 / 5.1)

print(51 // 4)

print(round(abs(3.2)** 3 , 4)) # .000000000001 sebep olan şey yuvarlanir

print(isim[::2].upper()+ ali[0::4], isim[0::4].lower().capitalize().startswith("is") + 3)
print(isim[0::4].lower().capitalize())

print(3 + 5 * 6)

print((3 + 2) * 4 - 3 == 17.0)

sayi1 = 10

sayi2 = 11

sayi3 = 10
print(sayi1 > sayi2 - sayi2)
print(type(sayi30), type(sayi32))
print(round(abs(3.2)** 3 , 4)) # .000000000001 sebep olan şey yuvarlanir

print(sayi1 != sayi2)

print(sayi2 <= sayi3 )

a = 1

b = a

a = 5

print(b)

sayi4 = "100asd"
sayi4 = "100"
sayi8 = 100
sayi37 = int(sayi4)
print(type(sayi4))
print(type(sayi8))
print(sayi37 == sayi8)
sayi100 = int(-10.9)
print(sayi100)
sayi101 = int(round(-10.9))
print(sayi101)
sayi201 = 123

sayi203 = str(sayi201)

print(sayi203)
print(type(sayi203))

i = 1

i = i + 2

i += 2

i *= 5

print(i)

i /= 7

print(i)

i //= 7

print(i)

renklerim = ["Siyah", "Beyaz", "Sari", "Mavi", "Yeşil"]

print(type(renklerim))

print(renklerim)

print(type(len(renklerim)))

print(renklerim[1]) #0'dan başlar
print(renklerim[2:])
print(renklerim[:4])
print(renklerim[::2])
# input("cevap?")
print(renklerim)
renklerim.append("Gri")
print(renklerim)
renklerim.insert(0, "Pembe")
print(renklerim)
renklerim.remove("Pembe")
print(renklerim)

renklerim2 = ["Turuncu", "Pembis"]

renklerim.append(renklerim2)
print(renklerim)

renklerim = ["Siyah", "Beyaz", "Sari", "Mavi", "Yeşil"]

renklerim.extend(renklerim2)
print(renklerim)
renklerim.pop()

silinen = renklerim.pop()
print(renklerim)
print(silinen)

renklerim.reverse()

print(renklerim)

renklerim.sort()

renklerim.reverse()
renklerim.sort()
renklerim.reverse()
renklerim.sort(reverse = True)
print(renklerim2)

renklerim3 = ["Siyah", "Beyaz", "Sari", "Mavi", "Yeşil"]

print(renklerim3)
liste2 = sorted(renklerim3)
print(liste2)
print(renklerim3)
print(min(renklerim3))
sayilar = [1, 2, 39, 4, 3, 7, 8]
print(max(renklerim3))
print(sum(sayilar))

for renk in renklerim3:
    print(renk)

print(list(enumerate(renklerim3)))
print(list(enumerate(renklerim3, start=2)))
print ("Siyah" in renklerim3)
print ("Gri" in renklerim3)

stringrenkler = "".join(renklerim3)
print(stringrenkler)
stringrenkler = " ".join(renklerim3)
print(stringrenkler) #Aralarına baştaki arkadaşı koy mesela boşluk
print(type(stringrenkler))
stringrenkler = "".join(renklerim3)
print(stringrenkler),
stringrenkler = "-".join(renklerim3)
renklerimpro = stringrenkler.split("-")
print(renklerimpro)
stringrenkler = " - ".join(renklerim3)
renklerimpro = stringrenkler.split("-") #aynı muamleyi yapacağız yoksa arada boşluk olur
print(renklerimpro)
renklerimpro = "".join(renklerim3)
print(renklerimpro)
renklerimpro = str(renklerim3)
renklerimpro = " - ".join(renklerim3)
yazdir = print
yazdir(renklerimpro)
# renklerimpro2 = "Ma".split(renklerimpro) #Bu Ma olmasına sebep olur
renklerimpro2 = renklerimpro.split("Ma")
yazdir(renklerimpro2)

demet = {"Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah"}

print(type(demet))
demet2 = ("Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah")
print(type(demet2))
print(len(demet))
print(len(demet2))
for kor in demet:
    print(demet)
    print(kor)

# demet[2] = "Pembe" # Hatalı kod
print(demet)
for renkler in demet:
    print(renkler)
    print(demet)
for renkler in demet2:
    print(renkler)
    print(demet2)    
#demet2.append("Pembe") # Hatalı kod add olmalı
#demet.append("Pembe") # Hatalı kod add olmalı demet ve kümede olmaz
demet.add("SARI")
print(demet),
demet.remove("Sari") # Eğer yanlış girersem keyerror verir mesela demet.remove("Sari0")
demet.discard("Sari0") # Bunda hata olmaz keyerror çünkü olmasa dahi hata vermez
demet.discard("Sari")
print(demet)
kume1 = {"Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah"}
kume2 = {"Sari", "Mavi", "Yeşil", "Beyaz", "Gri"}
print(kume1.intersection(kume2)) # Yer değiştirsem aynı
print(kume1.union(kume2)) #Birliktelik ama aynıları göstermez
print(kume1.difference(kume2)) #Bunda farklılık olur sıra değiştirirsem
print(kume2.difference(kume1))
yazdir("Sari" in kume1)
yazdir("Gri" in kume1)
yazdir("Gri" in kume1.uniofn(kume2))
bosliste1 = []
bosliste2 = list()
bosdemet1 = ()
bosdemet2 = tuple()
boskume2 = set()
boskume1 = {} # BU!! bir sözlüktür
print(type(boskume1))

python = set("PYTHON")
print(python)
python2 = set((1, 2, 3, 4, 5))
print(python2)
kisi  = {"isim" : "ali" , "yas" : 20, "cinsiyet" : "m", "hobiler" : ["Sinema", "Konser", "Yazilim"]}
print(kisi["isim"])
print(kisi["cinsiyet"])
kisi["isim"] = "Ahmet"
print(kisi)
kisi.update({"isim" : "Ahmet", "yas" : 30})
print(kisi)
kisi["id"] = 12345
print(kisi)

del kisi["id"]
print(kisi)
for x in kisi:
    print(x)
    print(kisi[x])
print(kisi.keys())
print(kisi.values())
print(kisi.items)
for k, v in kisi.items():
    print(k, v)
#print(kisi["id"]) #hata verir
print(kisi.get("id"))
print(kisi.get("isim"))
print(kisi.get("isim0"))
print(kisi.get("isim", "Bulunamadi"))
print(kisi.get("id", "Bulunamadi"))
# input( "asdf")
print('asdfx')
kitapismi = "Moby Dick"
sayfasayisi = 195
kitapagirligi = 13.45
Yeni = True
#isimler = input("İsminiz Nedir? ")
#print("Merhaba " + isimler)
#yemek = input("En sevdiğiniz yemek? ")
#isminiznedir = input("İsminiz Nedir? ")
#print(isminiznedir + " " + yemek + " " + "Sever")
if False:
   print("Kosul yanlis")
   print("Halen if blogumuz icindeyiz")
if True:
   print("Kosul dogru")
   print("Halen if blogumuz icindeyiz")
if 3 + 5 == 8:
    print("3+5=8")
a = 10
b = 7
if a == b:
    print("a = b")
if a > b:
    print("a > b")
if a != b:
    print("a !=b b")
c = 5 
d = 5
if c != d:
    print("c != d")
else:
    print("c = d")
renk = "Siyah"
if renk == "Beyaz":
   print("Beyaz")
elif renk == "Sari":
    print("Sari")
elif renk == "Mavi":
    print("Mavi")
else: 
    print("Hic biri")

a = 5

b = 8 

c = 10

if a < b or c > a:
    print("koşul doğru")
else:
    print("koşul yanliş")

if a < b and c > a: # Her ikisi doğru olmak zorunda
    print("koşul doğru")
else:
    print("koşul yanliş")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = 4
if a in liste:
    print("Listede var")
else:
    print("Listede yok") # Listede yoksa tetiklenir

isim = "Python"

a = "p"

if a in isim:
    print("Listede var")
else:
    print("Listede yok") # Küçük p diye yok

if not a in isim:
    print("Listede yok")
else: 
    print("Listede var")

a = 8 
b = 10
if not a == b: 
    print("koşul doğru")
else:
    print("koşul yanliş")

a = "python"
b = "pytho"
b + "n"
print(a)
print(b)

if a == b:
    print("a = b")
else:
    print("a != b")

if a is b:
    print("a = b")
else:
    print("a != b")
    print(id(a))
    print(id(b))
isim = "Muhammet"
yas = 31
yas = str(yas)
print(isim + " " + str(yas) + " " + "Yasinda")
int()
float()
str()
bool()

x = 9

y = 5

""" print(x + y)
print(x - y)
print(x * y)
print(x / y)

 """

print(x // y) #1.8'den 1
print(x % y) #Kalan bulma
print(x ** y)
#sayigirme = int(input("Sayi giriniz: "))
#sayigirme2 = int(input("Ikinci sayiyi giriniz: "))
#
#print(int(sayigirme) + int(sayigirme2))

print(round(9.8))
print(abs(-9))
import math
print(math.sqrt(9))

print(min(9, 10, 56))
print(max(9, 10, 56))
mektup = """merhaba beyfendi
napiyosunuz beyfendi""" #aynen kaydedildi
isim = 'Muhammet'.capitalize() # ilk harfini büyük yap
print(isim)
print(isim[0])
print(isim[0:4])
print(isim[-1])
print(isim[-4:-1])
print(len(isim))
print(isim.capitalize())
isim = "python"
print(isim.find("th"))  # Çıktı: 2
print(isim.replace("th", "yh"))
#isimnedir = input("İsminiz nedir: ")
#print(isimnedir.capitalize())
yagmurlu = False
gunesli = True
if yagmurlu:
    print("hava yagmurlu")
elif gunesli:
    print("hava gunesli")
else: 
    print("Bilinmeyen durum") #ilk kontrol edilen if
ehliyet = False
araba = True
if ehliyet and araba:
    print("araba kullanabilirsiniz")
elif araba and not ehliyet:
    print("Bizim sürücü kursunu tercih ederek araba kullanmay başlayabilirsiniz.")
elif ehliyet or araba:
    print("Araba kullanmana çok az kaldi")
else:
    print("Araba kullanman icin daha cok zaman var")

sicaklik = -5

if sicaklik > 30:
    print("hava cok sicak")
elif sicaklik < 0:
    print("hava cok soguk")
elif sicaklik >= 0:
    print("hava cok soguk degil")

yas = 18
okul = False

#yas = int(input("yasiniz kac?: "))

#okul = (input("okula gidiyon mu? evet/hayir: ").lower())

if yas >= 18 and okul == "hayir":
    print("askere gitme yasiniz geldi")
elif yas >= 18 and okul == "evet":
    print("okulunuz bitince askere gideceksiniz")
elif yas < 18 and okul == "evet":
    print("Askere gitmene daha cok var")
else:
    print("okula git")

liste = [1, 2, 3, 4, 5, 6]

for rakam in liste:
    print(rakam)

isim = "Ahmet"

for harf in isim:
    print(harf)

demet = {1, 2, 3, 4}

for i in demet:
    print(i)

for i in range(0,10,2): #3. argüman ikişer ikişer git
    print(i)

sonuc = 1
for i in range(0,10):
   sonuc *= 2
print(sonuc)
liste1 = ["a", "b", "c"]
liste2 = [1, 2, 3]

for harf in liste1:
    for rakam in liste2:
        print(harf, rakam)

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in liste:
    if i == 3:
        print("3'ü atladik.")
        continue # break kullansam durar
    print(i)

liste = range(100)

for i in liste:
    if i %3 != 0:
        continue
    if i == 81:
        break
    print(i) 
#import os
#os.system('cls')
#while True:
#    print("yok oldun")
x = 2
y = 3
while x < 10:
    print(x)
    x += 1
print("x = ", x)

x = 2 #tekrar 2 yapıyoruz yoksa 10
while x * y < 1000:
    print(x, y)
    x += 2
    y += 2

i = 1
#while True:
#    print(i)
#    i += 1
#    if i == 10000:
#        break # belirtmezsem sonsuza kadar devam
"""     if i %2 == 0:
        i+= 1 # bunu unutursam yani arttırmazsam sadece bir kez 1 gösterir ve devam eder program çünkü 2 çift
        continue
    print(i)
    i += 1 #bunu unutursam yani attırmazsam sadece 1 yazar sürekli devamlı
    if i == 1000:
        break #shift+alt+a """
print("1")
print("2")
print("3")
print("4")
print("5")
i = 1 
#while i <= 1000:
#    print(i)
#    i = i + 1
isciler = ["Mehmet", "Ahmet", "Abdullah", "Kerim" "Ali"]
print(isciler[0])
print(isciler[0:3])

sayi1 = int(input("sayi gir: "))

sayi2 = int(input("sayi gir yine: "))

sayi3 = input("hangi islemi yapacagini gir: (+, -, :, *, **)")

if sayi3 == "+":
    sonuc = sayi1 + sayi2
    print(sonuc)
elif sayi3 == "-":
    sonuc = sayi1 - sayi2
    print(sonuc)
elif sayi3 == "*":
    sonuc = sayi1 * sayi2
    print(sonuc)
elif sayi3 == ":":
    sonuc = sayi1 / sayi2
    print(sonuc)
elif sayi3 == "**":
    sonuc = sayi1 ** sayi2
    print(sonuc)    
else:
    print("Gecersiz islem")
#Belki while ekleyebilirim
#Daha onca şey var string yanına . ekleyip eklediğimiz şeyler fstrip gibi ama onları sadece okudum yazmadım
#sayi = input("Bir sayi giriniz:") #stringdir ondan int çevir
#print(type(int(sayi)))
#sayi = int(input("Bir sayi giriniz: "))

#faktoriyel = 1

#i = 2
#while i <= sayi: #while aynı i += 1 ekstra olarak ekledim for in rangede yoktu
#for i in range(1, sayi + 1): #1 yazmazsam faktoriyel 0 ile carpar sıfır 0 olur
#    faktoriyel  *= i
#    i += 1
#print(f"{sayi}! = {faktoriyel}")
# artıra artıra çarpar 5 x 4 x 3 x 2 x 1 = 120
#i = sayi
#liste = range(1000000)
#while i <= sayi:
#    i /= sayi 
#    if i in liste:

#     print(i)
#    elif i == 0:
#      break   
""" asalbulucu2 = sayi - 1
asalbulucu2 = range(asalbulucu)
print(asalbulucu2)
print(type(asalbulucu2))
asalbulucu2 = asalbulucu2[1:]
print(asalbulucu2)
bolunensayi = 1 # Kendisi de bölen olduğu için 1 olacak
for sayi in asalbulucu2:
    if sayi % asalbulucu != 0:
        bolunensayi += 1
        continue
print(bolunensayi) """ 
sayi = int(input("Lütfen geçerli bir sayi giriniz: "))

bolensayi = 0
for i in range(1, sayi + 1):
    if sayi % i == 0:
        bolensayi += 1
print(bolensayi)
print(f"{sayi} sayisinin {bolen_sayisi} tanesi vardir")
sayi = int(input("Lütfen geçerli bir sayi giriniz: "))

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

toplam = 0

gecici_sayi = sayi

while gecici_sayi != 0:

   basamak = gecici_sayi % 10
   toplam += basamak
   gecici_sayi //= 10

print(toplam)

#str_sayi = str(sayi)
#for rakam in str_sayi:
#    toplam += int(rakam)
# ikinci yöntem
#print(toplam)
#sayi1 = int(input("bir sayi giriniz 1/5: "))
#sayi2 = int(input("bir sayi giriniz 2/5: "))
#sayi3 = int(input("bir sayi giriniz 3/5: "))
#sayi4 = int(input("bir sayi giriniz 4/5: "))
#sayi5 = int(input("bir sayi giriniz 5/5: "))
#if sayi1 > sayi2 and sayi1 > sayi3 and sayi1 > sayi4 and sayi1 > sayi5:
#    print(f"En büyük sayi bulundu:{sayi1}")
#if sayi1 < sayi2 and sayi1 < sayi3 and sayi1 < sayi4 and sayi1 < sayi5:
#    print(f"En küçük sayi bulundu:{sayi1}")    
sayilar = input("beş tane sayi giriniz: ")
sayilar_listesi = sayilar.split()
sayilar_listesi = [int(sayi) for sayi in sayilar_listesi]
en_kucuk = min(sayilar_listesi)
en_buyuk = max(sayilar_listesi)
print(f"En küçük: {en_kucuk} En büyük: {en_buyuk}")
liste = []
for i in range(5):
    sayi int(input("Bir sayi giriniz: "))
    liste.append(sayi)
print(f"en büyük sayi : {max(liste)}")
print(f"en küçük sayi : {min(liste)}")
sayi = int(input("Bir sayi giriniz: "))
karekok = sayi ** 0.5

if karekok == int(karekok):
    print("Tamkare")
else:
    print("Tamkare değil")
yazi = (input("Bir yazi giriniz: "))
yazilar_sayisi = 0
for harf in yazi:
    print(harf)
    

for i in yazilar:
    if i == i:
     yazilar_sayisi += 1
     yazi = i
print(f"{yazilar_sayisi}, {yazi}" )

metin = input("Bir metin giriniz: ")

sozluk = dict()

for harf in metin:
    if harf in sozluk:
       sozluk[harf] += 1
    else:
       sozluk[harf] = 1

for harf, adet in sozluk.items():
    print(harf, adet)
metin = input("Bir metin giriniz: ")

metin2 = ""

for harf in metin:
    if harf == "a":
     harf = "A"
     metin2 += harf
    else:
     metin2 += harf
print(metin2)
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