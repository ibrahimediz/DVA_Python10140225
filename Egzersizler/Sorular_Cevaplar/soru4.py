
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


# n = int(input("Sayı giriniz:"))
n = 8
for i in range(n):
    print(" "*(n-i-1),"*"*(2*i+1),sep="")
for i in range(n-2,-1,-1):
    print(" "*(n-i-1),"*"*(2*i+1),sep="")   