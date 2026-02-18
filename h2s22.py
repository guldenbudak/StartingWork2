sayi1 =int(input("İlk sayıyı giriniz :"))
sayi2 =int(input("İkinci sayıyı giriniz :"))
for a in range(sayi1,sayi2+1):
    toplam = 0
    for b in range(1,a):
        if a %  b == 0:
            toplam = toplam + b
    if toplam == a:
        print(a)
