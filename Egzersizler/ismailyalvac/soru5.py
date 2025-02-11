
# Soru 5:

# yukarıda yer alan kütüphanelerden faydalanarak
# 1. En az 8 karakter uzunluğunda
# 2. En az 1 Rakam 
# 3. En az 1 Küçük Harf 
# 4. En az 1 Büyük Harf
# 5. En az 1 Noktalama
# 6. Kharf ve Bharf yan yana gelmesin Numara ve kHarf yan yana gelmesin

from random import choice,shuffle
from string import ascii_lowercase,ascii_uppercase,punctuation,digits



a = choice(ascii_lowercase) + choice(punctuation) + choice(ascii_uppercase) + choice(digits)
b = choice(ascii_lowercase) + choice(punctuation) + choice(ascii_uppercase) + choice(digits)
password = a+b
print(password)

