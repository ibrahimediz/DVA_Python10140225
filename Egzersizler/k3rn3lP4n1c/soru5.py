
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
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

def generate_password():
    lower = ascii_lowercase
    upper = ascii_uppercase
    digits_str = digits
    punct = punctuation

    # Şifreye her bir türden bir karakter ekliyoruz
    password = []
    password.append(choice(lower))
    password.append(choice(upper))
    password.append(choice(digits_str))
    password.append(choice(punct))

    # Şifrenin uzunluğunu 12'ye tamamlamak için karışık karakterler ekliyoruz
    all_characters = lower + upper + digits_str + punct
    while len(password) < 12:
        password.append(choice(all_characters))
    
    # Karakterlerin sıralamasını karıştırıyoruz
    shuffle(password)
    
    # Şifreyi tekrar kontrol edip, istenmeyen yan yana geçişleri düzeltiyoruz
    final_password = []
    for i in range(len(password)):
        if i > 0 and ((password[i-1].isalpha() and password[i].isdigit()) or
                      (password[i-1].isdigit() and password[i].isalpha()) or
                      (password[i-1] in ascii_lowercase + ascii_uppercase and password[i] in ascii_lowercase + ascii_uppercase) or
                      (password[i-1] in digits_str and password[i] in digits_str)):
            # Yan yana gelen karakterler yanlışsa ekleme
            continue
        final_password.append(password[i])
    
    # Şifreyi döndürüyoruz
    return ''.join(final_password)

# Şifreyi yazdırıyoruz
print(generate_password())
