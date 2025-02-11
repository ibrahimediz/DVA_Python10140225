
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
a = 0
b = 0

for i in range(8,0,-2):
    print(" " * int(i / 2) + "*"*a) 
    a += 2
for j in range(8,0,-2):
    print(" "*b + "*"*j) 
    b += 1
   