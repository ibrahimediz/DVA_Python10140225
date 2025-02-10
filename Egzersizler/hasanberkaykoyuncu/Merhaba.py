
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 
# kullanıcının girmiş olduğu veririnin ilk 2 karakterini ekrana yazdıran python kodunu yazınız

isim = input("İsminizi yazınız:")
print("Merhaba", isim, "memnun oldum.")
print(isim[0:2])


l1 = [1,2,3]
l2 = l1.copy()
l2.append(500)
print(l1,l2)
