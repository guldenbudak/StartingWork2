toplam = 0
girilen_deger =int(input("Lütfen bir tamsayı giriniz :"))
for sayi in range(1,girilen_deger):
    if sayi % girilen_deger == 0:
        toplam = toplam + girilen_deger
if toplam == girilen_deger:
        print("Mükemmel sayı")
else:
        print("Mükemmel sayı değil")
