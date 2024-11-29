metin = input("Bir metin giriniz: ")

metin2 = ""

for harf in metin:
    if harf == "a":
     harf = "A"
     metin2 += harf
    else:
     metin2 += harf
print(metin2)