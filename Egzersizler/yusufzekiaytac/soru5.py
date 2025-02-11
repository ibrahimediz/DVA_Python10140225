
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

from random import choice, shuffle
from string import ascii_lowercase,ascii_uppercase,punctuation,digits

passwd = ""
while len(passwd) < 8:
    passwd += choice(ascii_lowercase)
    passwd += choice(ascii_uppercase)
    passwd += choice(digits)
    passwd += choice(punctuation)

print(passwd)

# Karakterlerin yerlerini karıştırma
passwd_list = list(passwd)
shuffle(passwd_list)

# Karıştırılmış şifreyi yazdırma
print("".join(passwd_list))