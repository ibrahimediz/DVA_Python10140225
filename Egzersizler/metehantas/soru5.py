
# Soru 5:
import random
import string

# yukarıda yer alan kütüphanelerden faydalanarak
# 1. En az 8 karakter uzunluğunda
# 2. En az 1 Rakam 
# 3. En az 1 Küçük Harf 
# 4. En az 1 Büyük Harf
# 5. En az 1 Noktalama
# 6. Kharf ve Bharf yan yana gelmesin Numara ve kHarf yan yana gelmesin


harfler = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
passwordCreate = "".join(random.choice(harfler) for i in range(8)) 
print(passwordCreate)



