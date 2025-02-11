
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


yas = input("Yaşınızı giriniz.")
if yas.isdigit():
    yas = int(yas)
if yas <= 15:
    print("Oy kullanamazsınız, ülkemizde oy kullanma yaşı 16 yaş olarak belirlenmiştir.")
else:
    print("Oy kullanabilirsiniz.")
