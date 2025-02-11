
# Soru 4:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# yukarıda yer alan şekli elde edebilmek için gerekli python
# kodunu yazınız




sayi = input("baklava dilimi için çift sayı giriniz :")

if sayi.isdigit():
    if int(sayi) % 2 == 0:
        sayi1 = int(sayi)
        a = 1
        for i in range(sayi1,0,-2):
            print(" " * int(i / 2) + "*"*a) 
            a += 2
        for j in range(int(sayi1/2)+1):
            print(" "*j + "*"*a) 
            a -= 2
    else:
        print("lütfen çift sayı giriniz.")
else:
    print("lütfen sayı giriniz.")

