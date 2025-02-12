
# Soru 7:
# class Araba():
#     tip = "Binek Otomobil"
#     def __init__(self,plaka,marka,model,saseno):
#         self.plaka = plaka
#         self.marka = marka
#         self.model = model
#         self.__saseno = saseno

#     def bilgiVer(self):
#         print(self.marka,self.model)
#         print("Plaka:",self.plaka)

# class Araba():
#     tip = "Binek Otomobil"
#     def __init__(self,plaka,marka,model):
#           self.plaka = plaka
#           self.marka = marka
#           self.model = model
#           self.__saseno = saseno
#      # getter
#     @property
#     def saseno(self):
#         if self.yetki == 1:
#             return self.__saseno
#         else:
#             raise Exception("Yetki Hatası")

#     @saseno.setter
#     def saseno (self,param):
#         if type(param) == int:
#             if param in range(1,20):
#                 self.__gizli = param
#             else:
#                 raise Exception("Limit Hatası")
#         else:
#             raise ValueError("Değer Hatası")

#     @gizli.deleter
#     def gizli(self):
#         self.__gizli*=-1
#      def bilgiVer(self):
#          print(self.marka,self.model)
#          print("Plaka:",self.plaka)


class Araba():
    tip = "Binek Otomobil"

    def __init__(self, plaka, marka, model, yetki, saseno):
        self.plaka = plaka
        self.marka = marka
        self.model = model
        self.yetki = yetki
        self.__saseno = saseno

    # getter
    @property
    def saseno(self):
        if self.yetki == 1:  # Yetki kontrolü
            return self.__saseno
        else:
            raise Exception("Yetki Hatası")

    def bilgiVer(self):
        print(self.marka, self.model)
        print("Plaka:", self.plaka)