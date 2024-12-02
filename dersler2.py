prime_list = list()

prime_list.append(2)

sayi = 3

while True:
    prime = True
    for i in range(2, int(sayi ** 0.5) + 1): #0.5 kuvveti yani tam uyumlu 25/5 5 olur bu yüzden bundan büyükse yani +1 o zaman devam ediyoruz
        if sayi %i == 0:
            prime = False
            break
        if prime:
            prime_list.append(sayi)
            if len(prime_list) == 10000:
                break
    sayi += 1        

liste2 = [] # boş liste

for prime in prime_list:
    strprime = str(prime)
    if strprime.startswith("3") and strprime.endswith("7"):
      liste2.append(prime)

print(liste2)
print(len(liste2))