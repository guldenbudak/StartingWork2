values =int(input("Enter a value between 0 and 100 :"))
if 90 <= values <= 100:
    print("A")
elif 80 <= values <= 89:
    print("B")
elif 79 <= values <= 70:
    print("C")
elif 60 <= values <= 69:
    print("D")
elif 0 <= values <= 59:
    print("F")
else :
    print("Geçersiz")