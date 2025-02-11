
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 
# kullanıcının girmiş olduğu veririnin ilk 2 karakterini ekrana yazdıran python kodunu yazınız
#isim = input("Lütfen isminizi giriniz: ")
#print("İsminizin ilk iki harfi:", isim[:2])


# Piramit yüksekliğini kullanıcıdan alalım
height = int(input("Piramit yüksekliğini giriniz: "))

# Üst piramidi yazdıralım
for i in range(1, height + 1):
    print(" " * (height - i), end="")
    print("*" * (2 * i - 1))

# Alt ters piramidi yazdıralım
for i in range(height - 1, 0, -1):
    print(" " * (height - i), end="")
    print("*" * (2 * i - 1))
