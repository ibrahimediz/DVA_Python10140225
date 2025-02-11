
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
n = 7
for i in range(1,n):
    print(" "*(n-i),"*"*(i+2)," "*(n-i))
# for i in range(n,0,-1):
#     print(" "*(n-i),"*"*i,sep="") 