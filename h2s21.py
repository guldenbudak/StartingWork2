n =int(input("Lütfen bir değer giriniz :"))
toplam = 0
for i in range(1,n):
    if n % i == 0:
        toplam += i
if toplam == n:
    print("Mükemmel sayı.")
else:
    print("Mükemmel sayı değildir.")