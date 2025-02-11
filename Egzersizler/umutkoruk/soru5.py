
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

import random
import string

def generate_password():
    while True:
        password = []
        
        # En az 1 küçük harf
        password += random.choices(string.ascii_lowercase, k=1)
        
        # En az 1 büyük harf
        password += random.choices(string.ascii_uppercase, k=1)
        
        # En az 1 rakam
        password += random.choices(string.digits, k=1)
        
        # En az 1 noktalama işareti
        password += random.choices(string.punctuation, k=1)
        
        # Şifre uzunluğunu 8'e tamamla (geri kalan karakterler rastgele)
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=8-len(password))
        
        # Şifreyi karıştır
        random.shuffle(password)
        
        # Şifreyi oluştur
        password = ''.join(password)
        
        # Şifrenin kurallara uygun olup olmadığını kontrol et
        if (len(password) >= 8 and
            any(c.isdigit() for c in password) and
            any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c in string.punctuation for c in password) and
            not any(password[i].isupper() and password[i+1].islower() for i in range(len(password)-1)) and
            not any(password[i].islower() and password[i+1].isdigit() for i in range(len(password)-1))):
            return password

# Yeni şifre oluştur
new_password = generate_password()
print("HAYIRLI OLSUN :", new_password)
