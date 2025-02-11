
# Soru 1:
# input fonksiyonu ile kullanıcıdan ismini isteyiniz. 
# kullanıcının girmiş olduğu veririnin ilk 2 karakterini ekrana yazdıran python kodunu yazınız
#isim = input("Lütfen isminizi giriniz: ")
#print("İsminizin ilk iki harfi:", isim[:2])


# Piramit yüksekliğini kullanıcıdan alalım
#height = int(input("Piramit yüksekliğini giriniz: "))

# Üst piramidi yazdıralım
#for i in range(1, height + 1):
    #print(" " * (height - i), end="")
    #print("*" * (2 * i - 1))

# Alt ters piramidi yazdıralım
#for i in range(height - 1, 0, -1):
    #print(" " * (height - i), end="")
   # print("*" * (2 * i - 1))

import random
import curses

# Yılanın başlatılacağı ekran boyutları
screen = curses.initscr()
curses.curs_set(0)  # Fareyi gizle
sh, sw = screen.getmaxyx()  # Ekranın boyutlarını al
w = curses.newwin(sh, sw, 0, 0)  # Ekran penceresi
w.keypad(1)  # Klavye tuşlarını tanımak için
w.timeout(100)  # Yılanın hareket etme süresi

# Yılanın başlangıç noktası ve uzunluğu
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# İlk meyve yerini rastgele seç
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)  # Meyve olarak "π" sembolü çizilir

# Yılanın başlangıç yönü
key = curses.KEY_RIGHT

# Oyun döngüsü
while True:
    next_key = w.getch()  # Kullanıcıdan bir tuş al

    key = key if next_key == -1 else next_key  # Yeni tuş alınırsa yön değiştirilir

    # Yılanın yeni başı
    if key == curses.KEY_RIGHT:
        new_head = [snake[0][0], snake[0][1] + 1]
    elif key == curses.KEY_LEFT:
        new_head = [snake[0][0], snake[0][1] - 1]
    elif key == curses.KEY_UP:
        new_head = [snake[0][0] - 1, snake[0][1]]
    elif key == curses.KEY_DOWN:
        new_head = [snake[0][0] + 1, snake[0][1]]

    # Yılanın kendisine çarpması durumunda oyun biter
    if new_head in snake:
        curses.endwin()
        quit()

    # Yılanın başı ekrana sınır dışına çıkarsa oyun biter
    if new_head[0] == 0 or new_head[0] == sh or new_head[1] == 0 or new_head[1] == sw:
        curses.endwin()
        quit()

    # Yılanın yeni başı yılanın boyutunun içine eklenir
    snake.insert(0, new_head)

    # Yılanın yediği meyve varsa, yılan büyür
    if snake[0] == food:
        food = None
        while food is None:  # Yeni meyve rastgele yerleştirilir
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)  # Yeni meyve ekrana çizilir
    else:
        # Yılanın kuyruğunun sonu çıkarılır (hareket ederken yılanın kısalmasını sağlar)
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Yılanın başı ekrana çizilir
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
