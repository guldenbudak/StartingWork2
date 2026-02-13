toplam = 0
sayi1 =int(input("İlk sayıyı giriniz :"))
sayi2 =int(input("İkinci sayıyı giriniz :"))
for sayi in range(sayi1,sayi2):
    if x % sayi1 == 0 and x % sayi2 == 0:
        toplam += x
if toplam == x:
    print(x)
