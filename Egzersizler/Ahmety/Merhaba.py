
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 
# kullanıcının girmiş olduğu veririnin ilk 2 karakterini ekrana yazdıran python kodunu yazınız
#isim = input("Lütfen isminizi giriniz: ")
#print("İsminizin ilk iki harfi:", isim[:2])

import random

# Oyuncu bilgileri
oyuncu_adi = input("Macera için bir isim girin: ")
oyuncu_can = 100
oyuncu_silah = "kavak dalı"
puan = 0

# Canavarlar ve savaş
def canavar_savas():
    global oyuncu_can
    canavarlar = ["Ork", "Zombi", "Tavuk", "Ejderha"]
    canavar = random.choice(canavarlar)
    canavar_can = random.randint(20, 50)
    print(f"\nBir {canavar} ile karşılaştınız! Canı: {canavar_can}")
    
    while canavar_can > 0 and oyuncu_can > 0:
        secim = input("Saldırmak için 'A' ya da kaçmak için 'K' tuşlayın: ").upper()
        
        if secim == 'A':
            oyuncu_vurus = random.randint(10, 25)
            canavar_can -= oyuncu_vurus
            print(f"Sen {oyuncu_vurus} hasar verdin! Canavarın canı: {canavar_can}")
            
            if canavar_can <= 0:
                print(f"Tebrikler, {canavar}'ı yendiniz!")
                return 20  # Yenen canavardan puan al
        elif secim == 'K':
            kacma_basari = random.randint(1, 2)
            if kacma_basari == 1:
                print(f"{canavar} size saldırmadan kaçmayı başardınız!")
                return 0
            else:
                hasar = random.randint(5, 15)
                oyuncu_can -= hasar
                print(f"{canavar} size saldırdı! {hasar} hasar aldınız. Canınız: {oyuncu_can}")
        else:
            print("Geçersiz seçim!")

        if oyuncu_can <= 0:
            print(f"\nÜzgünüz {oyuncu_adi}, öldünüz.")
            return -1  # Oyuncu ölürse oyun biter

    return 0

# Zindanı gezerken karşılaşabileceğiniz durum
def zindan():
    global oyuncu_can, puan
    print(f"\nHoşgeldin {oyuncu_adi}, zindanın derinliklerine inmeye başlıyorsun.")
    print("Hazırlıklı ol, zindanda seni birçok tehlike bekliyor!")

    while oyuncu_can > 0:
        print(f"\nCanınız: {oyuncu_can} | Puanınız: {puan}")
        olay = random.choice(["canavar", "tespih", "hazine", "tuzağa düşme", "çıkışa ulaşma"])
        
        if olay == "canavar":
            print("\nBir canavarla karşılaştınız!")
            puan_eklendi = canavar_savas()
            if puan_eklendi == -1:
                break
            puan += puan_eklendi
        
        elif olay == "tespih":
            print("\nBir tespih buldunuz, moral kaynağınız oldu!")
            oyuncu_can += 10
            print(f"Canınız arttı! Şu anki canınız: {oyuncu_can}")
        
        elif olay == "hazine":
            print("\nBir hazine odasına girdiniz! Puan kazandınız.")
            puan += 50
            print(f"Puanınız: {puan}")
        
        elif olay == "tuzağa düşme":
            print("\nBir tuzağa düştünüz! Canınız azaldı.")
            zarar = random.randint(5, 20)
            oyuncu_can -= zarar
            print(f"{zarar} hasar aldınız. Canınız: {oyuncu_can}")
        
        elif olay == "çıkışa ulaşma":
            print("\nZindanın çıkışına ulaştınız! Macera sona erdi.")
            break
    
    if oyuncu_can <= 0:
        print(f"Öldünüz, {oyuncu_adi}. Zindan sizi yenecek kadar zorlayıcıydı!")
    else:
        print(f"\nTebrikler! Zindandan çıkmayı başardınız. Toplam Puanınız: {puan}")
    print("Oyun bitti.")

# Oyunu başlat
zindan()

