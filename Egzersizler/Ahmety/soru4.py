
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

# 8 harfi
# print("  ***  ")
# print(" *   * ")
# print(" *   * ")
# print("  ***  ")
# print(" *   * ")
# print(" *   * ")
# print("  ***  ")


# Piramit yüksekliğini kullanıcıdan alalım
height = int(input("Piramit yüksekliğini giriniz: "))

# Üst piramid
for i in range(1, height + 1):
    print(" " * (height - i), end="")
    print("*" * (2 * i - 1))

# Alt ters piramid
for i in range(height - 1, 0, -1):
    print(" " * (height - i), end="")
    print("*" * (2 * i - 1))
