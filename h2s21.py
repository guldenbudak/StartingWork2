girilen_deger =int(input("Lütfen bir tamsayı giriniz :"))
toplam = 0
for sayi in range(1,girilen_deger):
    if girilen_deger % sayi == 0:
        toplam = toplam + sayi
if toplam == girilen_deger:
        print("Mükemmel sayı")
else:
        print("Mükemmel sayı değil")
