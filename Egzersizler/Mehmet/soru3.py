
# Soru 3:
# yas = input("yas Bilgisi Giriniz:")
# if yas.isdigit():
#     yas = int(yas)
#     if yas <= 1000:
#         print("Yoksulsunuz")
#     else:
#         print("Şanslısınız")
# else:
#     print("Yanlış Giriş")
# Yukarıda yer alan kod bloğundan faydalanarak 
# oy kullanma yaşınının 16 olduğu bir ülkede 
# kullanıcıdan alınan yaş bilgisi ile kontrol gerçekleştiriniz
# ve ekrana oy kullanabilirsin yazınız


yas = input("Yaşınızı Giriniz: ")
if yas.isdigit():
    yas = int(yas)
    if yas >= 16:
        print("Oy kullanabilirsiniz")
    else:
        print("Oy kullanmak için yaşınız yeterli değil")
else:
    print("Yanlış Giriş")
