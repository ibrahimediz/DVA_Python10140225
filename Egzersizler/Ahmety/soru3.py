
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
# Kullanıcıdan yaş bilgisini alalım



yas = input("Yaşınızı Giriniz: ")

# Yaş bilgisinin doğru formatta olup olmadığını kontrol edelim
if yas.isdigit():
    yas = int(yas)
    if yas >= 16:
        print("Oy kullanabilirsin")
    else:
        print("Oy kullanamazsınız")
else:
    print("Yanlış Giriş")
