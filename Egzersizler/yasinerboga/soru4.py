
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

n = 6
for i in range(1,n):
    print(" "*i)
for j in range(n,0,-1):
    print("* "*j)

# n = int(input("Sayı giriniz:"))
n = 5
for i in range(1,n):
    print(" "*(n-i),"*"*i,sep="")
for i in range(n,0,-1):
    print(" "*(n-i),"*"*i,sep="")