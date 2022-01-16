# profile-info.py

import identity as userData

menu = """
Daftar Pilihan :
[n] Tampilkan NIM
[N] Tampilkan Nama
[T] Tampilkan Tanggal Lahir
[K] Tampilkan Kelamin
[A] Tampilkan Agama
[a] Tampilkan Alamat
[B] Tampilkan Bahasa Keseharian
[b] Tampilkan daftar pilihan
[k] Keluar program"""

print(menu + "\n")

useropt = ''
while (useropt != 'k'):
    useropt = input("Input Menu -> ")

    if (useropt == 'n'):
        userData.printStudentId()
    elif (useropt == 'N'):
        userData.printName()
    elif (useropt == 'T'):
        userData.printBirthDay()
    elif (useropt == 'K'):
        userData.printGender()
    elif (useropt == 'A'):
        userData.printReligion()
    elif (useropt == 'a'):
        userData.printAddress()
    elif (useropt == 'B'):
        userData.printDailyLaguage()
    elif (useropt == 'b'):
        print(menu)
    elif (useropt == 'k'):
        print('Terimakasih')
    else:
        print('Perintah tidak dikenal')
    
    print()