
# Soru 7:
class Araba():
     tip = "Binek Otomobil"
     def __init__(self,plaka,marka,model,saseno):
         self.plaka = plaka
         self.marka = marka
         self.model = model
         self.__saseno = saseno
         self.__gizli = "Gizli Bilgi"

     def bilgiVer(self):
         print(self.marka,self.model)
         print("Plaka:",self.plaka)
    




