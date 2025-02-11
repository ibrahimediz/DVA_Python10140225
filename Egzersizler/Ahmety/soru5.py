
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
from string import ascii_lowercase, ascii_uppercase, punctuation, digits

def generate_password():
    while True:
        password = []

        # Şifre koşullarını sağlamak için en az bir tane her karakter türünden ekliyoruz
        password.append(choice(ascii_lowercase))  # Küçük harf
        password.append(choice(ascii_uppercase))  # Büyük harf
        password.append(choice(digits))  # Rakam
        password.append(choice(punctuation))  # Noktalama işareti

        # Şifreyi oluşturmak için kalan kısmı rasgele seçiyoruz
        all_characters = ascii_lowercase + ascii_uppercase + digits + punctuation
        while len(password) < 8:
            password.append(choice(all_characters))

        # Şifreyi karıştırıyoruz
        for _ in range(100):  # Karıştırmayı iyileştirmek için birkaç kez yapıyoruz
            index1, index2 = choice(range(len(password))), choice(range(len(password)))
            password[index1], password[index2] = password[index2], password[index1]

        # Koşulları kontrol ediyoruz
        password_str = ''.join(password)

        # Küçük harf ve büyük harf yan yana gelmemeli
        if any(password_str[i].islower() and password_str[i+1].isupper() for i in range(len(password_str)-1)):
            continue
        
        # Numara ve küçük harf yan yana gelmemeli
        if any(password_str[i].isdigit() and password_str[i+1].islower() for i in range(len(password_str)-1)):
            continue

        # Şifreyi geçerli ise döndür
        return password_str

# Şifreyi oluştur
password = generate_password()
print("Oluşturulan Şifre: ", password)
