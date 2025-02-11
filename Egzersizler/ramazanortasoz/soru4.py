
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

# Üst kısmı çizmek için
for i in range(1, 8, 2):
    print(' ' * ((7 - i) // 2) + '*' * i)

# Alt kısmı çizmek için
for i in range(5, 0, -2):
    print(' ' * ((7 - i) // 2) + '*' * i)