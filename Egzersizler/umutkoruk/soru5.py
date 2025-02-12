
def find_number():
    # 11 haneli sayıyı 10000000001 ile 99999999999 arasında arıyoruz
    for num in range(10000000001, 100000000000):  # 11 haneli sayılar
        str_num = str(num)
        
        # 1, 3, 5, 7, 9 hanelerinin toplamını hesapla
        sum_odd_positions = int(str_num[0]) + int(str_num[2]) + int(str_num[4]) + int(str_num[6]) + int(str_num[8])
        
        # 2, 4, 6, 8 hanelerinin toplamını hesapla
        sum_even_positions = int(str_num[1]) + int(str_num[3]) + int(str_num[5]) + int(str_num[7])
        
        # 10. haneyi, 1, 3, 5, 7, 9 hanelerinin toplamının 7 katının, 2, 4, 6, 8 hanelerinin toplamına farkının mod 10'u verecek
        if (sum_odd_positions * 7 - sum_even_positions) % 10 != int(str_num[9]):
            continue
        
        # 1, 2, 3, 4, 5, 6, 7, 8, 9 hanelerinin toplamının mod 11'i, 11. haneyi verecek
        if sum(int(str_num[i]) for i in range(9)) % 11 != int(str_num[10]):
            continue
        
        # Eğer tüm şartlar sağlanıyorsa, sayıyı döndür
        return num

# Sayıyı bulma
result = find_number()
print(f"Bulunan sayı: {result}")