bakiye = 1000
sec =""
yeniBakiye = ""
while sec != 4:
    sec =int(input("1)Bakiye Görüntüleme\n"
                   "2)Para Yatır\n"
                   "3)Para Çekme\n"
                   "4)Çıkış\n"
                   "Seçmek istediğiniz numarayı giriniz :"))
    if sec == 1:
        print("Bakiyeniz: ",yeniBakiye)
    elif sec == 2:
        eklenen =int(input("Yatırmak istediğiniz değeri giriniz:"))
        yeniBakiye = yeniBakiye + eklenen
        print("Bakiye : ",yeniBakiye)
    elif sec == 3:
        print("Bakiyeniz: ",bakiye)
        eksilen = int(input("Çekmek istediğiniz miktarı giriniz :"))
        yeniBakiye = bakiye - eksilen
        print("Bakiye : ",yeniBakiye)
    elif sec == 4:
        print("Çıkış : Güle Güle")

