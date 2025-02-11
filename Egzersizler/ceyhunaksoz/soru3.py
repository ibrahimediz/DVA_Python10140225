
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

yas = input("Yaşınızı Giriniz: ")

# Yaş bilgisinin doğru olup olmadığını kontrol et
if yas.isdigit():
    yas = int(yas)
    if yas >= 16:
        print("Oy kullanabilirsiniz")
    else:
        print("Yaşınız yeterli değil")
else:
    print("Yanlış Giriş")
