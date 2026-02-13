sayi = int(input("Lütfen pozitif bir sayı giriniz :"))
if sayi > 1:
    for i in range(2,sayi):
        if sayi % i == 0:
            print("Asal sayıdır .")
            break
    else:
            print("Asal sayı değildir.")

else:
    print("Asal sayı değildir.")



