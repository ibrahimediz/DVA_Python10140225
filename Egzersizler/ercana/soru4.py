
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


boyut=5
for i in range(boyut):
    for k in range((boyut)-i):
        print(" ",end="")
    for m in range(i*2-1):
        print("*",end="")
    print()
for i in range(boyut,0,-1):
    for k in range((boyut)-i):
        print(" ",end="")
    for m in range(i*2-1):
        print("*",end="")
    print()