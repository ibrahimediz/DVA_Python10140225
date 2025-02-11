# Baklava dilimi yapma

n = 5  # Baklava diliminin boyutu (Yükseklik / genişlik)
    
# Artan kısmı yazdırma
#for i in range(1, n + 1):
#    print(" " * (n - i) + "*" * (2 * i - 1))  # Boşluk ve yıldızları yazdırma

# Azalan kısmı yazdırma
#for i in range(n - 1, 0, -1):
 #   print(" " * (n - i) + "*" * (2 * i - 1))  # Boşluk ve yıldızları yazdırma


a = 1
for i in range(50,0,-2):
    if i % 10 == 0:
        print(" " * (int(i / 2)-3) + "xx "+ "*"*a + " xx") 
    else:
        print(" " * int(i / 2) + "*"*a) 
    a += 2



a = 1
b = 1
for i in range(20,0,-2):
    print(" " * int(i / 2) + "*"*a) 
    a += 2
for j in range(20,0,-2):
    print(" "*b + "*"*j) 
    b += 1

