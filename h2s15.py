enkucuksayi=100
girilensayi=int(input("Lütfen kaç değer girmek istediğinizi yazınız :"))
for x in range(girilensayi):
    sayi=int(input("Sayıyı giriniz (100'den küçük olmalıdır.) :"))
    if sayi > 100:
        print("Hata 100 den büyük bir değer giremezsiniz.")
        break
    if sayi < enkucuksayi:
        enkucuksayi = sayi
print("En küçük sayı :",enkucuksayi)
