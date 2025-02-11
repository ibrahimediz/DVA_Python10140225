
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


oykullanim = input("Yasinizi Giriniz:")
if oykullanim.isdigit():
    oykullanim = int(oykullanim)
    if oykullanim <= 16:
        print("Oy kullanamazsiniz")
    else:
        print("Oy kullanabilirsiniz")
else:
    print("Sayisal veri giriniz....")

