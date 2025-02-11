
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


Yas = input("Yasınızı  Giriniz:")
if Yas.isdigit():
    Yas = int(Yas)
    if Yas <= 16:
        print("oy kullanmaz")
    else:
        print("SEÇMEN")
else:
     print("Yanlış Giriş")