
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
a = 1
for i in range(10,0,-2):
    print(" " * int(i / 2) + "*"*a) 
    a += 2
for i in range(0,20,2):
    print(" " * int(i / 2) + "*"*a) 
    a -= 2