import time

print('Menghitung waktu pulang : ')

while not time.localtime().tm_sec == 1:
    str_time = time.strftime('%H:%M:%S', time.localtime())
    print(str_time)
    time.sleep(1)

print('Jam praktikum sudah habis. Silahkan pulang :)')