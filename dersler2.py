sayi = 1
fibonacci_list = list()
fibonacci_list.append(1)
fibonacci_sayisi = 0
while True:
    sayi += sayi
    fibonacci_list.append(sayi)
    if len(fibonacci_list) == 100:
        break
print(fibonacci_list)