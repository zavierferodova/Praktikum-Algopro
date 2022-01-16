from getpass import getpass

password = 'zavierferodova'

for i in range(0, 3):
    input_password = getpass('Masukkan Password : ')
    if i == 2:
        print('Akses ditolak !')
        break
    elif input_password == password:
        print('Login berhasil :)')
        break
    else:
        print('Maaf, password salah !')
