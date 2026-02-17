enbuyuksayi = 0
girilecek_sayilar = int(input("Lütfen kaç değer girmek istediğinizi yazın :"))
for i in range(girilecek_sayilar):

    sayi =int(input("Sayıyı giriniz :"))
    if sayi > enbuyuksayi:
        enbuyuksayi = sayi
print("En büyük sayı :",enbuyuksayi)

