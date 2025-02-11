
# Soru 3:
# gsymh = input("GSYMH Bilgisi Giriniz:")
# if gsymh.isdigit():
#     gsymh = int(gsymh)
#     if gsymh <= 1000:
#         print("Yoksulsunuz")
#     else:
#         print("Şanslısınız")
# else:
#     print("Yanlış Giriş")
# Yukarıda yer alan kod bloğundan faydalanarak 
# oy kullanma yaşınının 16 olduğu bir ülkede 
# kullanıcıdan alınan yaş bilgisi ile kontrol gerçekleştiriniz
# ve ekrana oy kullanabilirsin yazınız

yas = int(input("Whats your age: "))
# if yas.isdigit():
if yas >= 16:
        print("Oy kullanabilirsiniz")
else:
        print("Oy kullanamazsınız")
# else:
#     print("Hatalı bilgi girişi yaptınız")