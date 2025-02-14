import pywhatkit
import time
import os

NUMARA = "+905495000000"
FOTO_KLASOR = "/home/syn-ack/Downloads/deneme23"

# Fotoğrafları sırayla gönder
for i, foto in enumerate(os.listdir(FOTO_KLASOR)):
    if i >= 100:  
        break

    foto_yolu = os.path.join(FOTO_KLASOR, foto)
    pywhatkit.sendwhats_image(NUMARA, foto_yolu, f"Fotoğraf {i+1}")
    time.sleep(5)  

print("100 fotoğraf başarıyla gönderildi!")
