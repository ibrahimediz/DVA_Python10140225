
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
for i in range(1,n+1, 2):
    spaces = (n - i) // 2
    print(' ' * spaces + '*' * i)
for i in range(n-2, 0, -2):
    spaces = (n - i) // 2
    print(' ' * spaces + '*' * i)
