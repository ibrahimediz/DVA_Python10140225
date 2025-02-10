# Basit yazdırma
print("Merhaba, Dünya!")

# Birden fazla değeri yazdırmak
ad = "Ali"
yas = 25
print("Ad:", ad, "Yaş:", yas)

# F-String Kullanımı
print(f"Ad: {ad}, Yaş: {yas}")

# Format() metodu kullanımı
print("Ad: {}, Yaş: {}".format(ad, yas))

# Yazdırma sonrası satır başı (end parametresi)
print("Merhaba", end=" ")
print("Dünya!")

# Ayrı karakter ile yazdırmak (sep parametresi)
print(ad, yas, sep="-")

# Çift tırnak veya tek tırnak kullanmak
print('Merhaba Dünya!')
print("Merhaba Dünya!")

# Çok satırlı yazdırma
print("Birinci satır\nİkinci satır\nÜçüncü satır")

# Sayıları ve hesaplamaları yazdırmak
a = 5
b = 3
print("Toplam:", a + b)

# String ve sayıları birleştirmek
sayi = 10
print("Sayı: " + str(sayi))

# Örnek değişkenler
x = 5
y = "Merhaba"
z = [1, 2, 3]

# type() fonksiyonu ile tiplerini yazdırma
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
print(type(z))  # <class 'list'>
