
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
    # Şifre için gerekli karakter setlerini tanımlıyoruz
    lowercase = ascii_lowercase
    uppercase = ascii_uppercase
    punctuation_marks = punctuation
    numbers = digits

    # Şifreyi oluşturmak için başlangıçta 1 karakter seçiyoruz her kategoriden
    password = [
        choice(lowercase),  # En az 1 küçük harf
        choice(uppercase),  # En az 1 büyük harf
        choice(numbers),     # En az 1 rakam
        choice(punctuation_marks)  # En az 1 noktalama işareti
    ]
    
    # Şifreyi 8 karakter yapabilmek için kalan karakterleri rastgele seçiyoruz
    all_characters = lowercase + uppercase + punctuation_marks + numbers
    while len(password) < 8:
        password.append(choice(all_characters))

    # Şifreyi karıştırıyoruz
    shuffle(password)

    # Yan yana iki rakam veya iki harf olmaması için kontrol yapıyoruz
    for i in range(1, len(password)):
        # Eğer yan yana iki harf veya iki rakam varsa, şifreyi yeniden oluşturuyoruz
        if (password[i].isalpha() and password[i-1].isalpha()) or (password[i].isdigit() and password[i-1].isdigit()):
            return generate_password()
    
    # Şifreyi birleştirip döndürüyoruz
    return ''.join(password)

# Şifreyi oluştur ve yazdır
print(generate_password())
