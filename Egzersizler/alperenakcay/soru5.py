
# Soru 5:
# from random import choice
# from string import ascii_lowercase,ascii_uppercase,punctuation,digits

# yukarıda yer alan kütüphanelerden faydalanarak
# 1. En az 8 karakter uzunluğunda
# 2. En az 1 Rakam 
# 3. En az 1 Küçük Harf 
# 4. En az 1 Büyük Harf
# 5. En az 1 Noktalama
# 6. Kharf ve Bharf yan yana gelmesin Numara ve kHarf yan yana gelmesin

from random import choice
from string import ascii_lowercase,ascii_uppercase,punctuation,digits

uzunluk = int(input("şifre uzunluğu giriniz."))

sifre = ""

while len(sifre) < uzunluk:
    a = choice(ascii_lowercase)
    b = choice(ascii_uppercase)
    c = choice(punctuation)
    d = choice(digits)
    liste = [a,b,c,d]
    secilenKarakter = choice(liste)
    if secilenKarakter == a:
        liste.remove(b)
        liste.remove(d)
        secilenKarakter = choice(liste)
    elif secilenKarakter ==b:
        liste.remove(a)
        secilenKarakter = choice(liste)
    elif secilenKarakter == d:
        liste.remove(a)
        secilenKarakter = choice(liste)
    sifre = sifre + secilenKarakter
print(sifre)
