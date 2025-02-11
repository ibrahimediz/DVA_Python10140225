
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
b = 1
for i in range(20,0,-2):
    print(" " * int(i / 2) + "*"*a) 
    a += 2
for j in range(20,0,-2):
    print(" "*b + "*"*j) 
    b += 1