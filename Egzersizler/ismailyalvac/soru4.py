
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

number = int(input("Sayı giriniz: "))
i = 0
a = number
while i <= number:
    print(" "*(a-i), "*"*i)
    i += 1
while i > 0:
    print("*"*i)
    i -= 1

     