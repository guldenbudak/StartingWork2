faktoriyel =1
number = int(input("Enter a number: "))
if number < 0:
    print("Number is negative")
elif number == 0:
    print("Number zero faktoriyel 1.")
elif number > 0:
    for sayi in range(1,number+1):
        faktoriyel = faktoriyel* sayi
print(faktoriyel)