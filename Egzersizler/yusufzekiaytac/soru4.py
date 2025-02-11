
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

n = input("Yıldız boyutu gir:")
if n.isdigit():
    n = int(n)
    for i in range(1, n, 2):
        print(" " * ((n - 1 - i) // 2) + "*" * i)
    for i in range(n - 3, 0, -2):
        print(" " * ((n - 1 - i) // 2) + "*" * i)
else:
    print("Sayi gir!!")