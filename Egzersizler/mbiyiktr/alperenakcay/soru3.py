
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
    if int(yas) >= 16:
        print("Oy Kullanabilirsiniz.")
    else:
        print("Yaşınız yasal sınırın altında")
else:
    print("Lütfen doğru bilgi giriniz.")

    