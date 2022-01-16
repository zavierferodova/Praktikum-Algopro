name = 'Zavier Ferodova Al Fitroh'
student_id = 'xxxxxxx205'
X = '1' + student_id[7:]
a = int(X)
# Konversi string ke integer
b = len(name)
# Menghitung panjang karakter pada variabel name

type(a)
# Mengambil informasi jenis tipe data pada variabel a yakni integer
type(b)
# Mengambil informasi jenis tipe data pada variabel b yakni integer
a / b
# Menghitung hasil pembagian dari a yakni 1205 dan b yakni 25 maka 1205 / 25 = 48.2

a // b
# Menghitung hasil pembagian dari 1205 / 25 = 48.2 dan membulatkannya menjadi 48
10 * (a - 999)
# Menghitung nilai dari 10 * (1205 - 999) = 2060
b ** 2
# Menghitung nilai perpangkatan dari 25^2 = 625
a % b
# Menghitung nilai sisa pembagian (modulus) dari 1205 / 25 maka hasilnya adalah 5

c = 12.5
# Menyimpan nilai 12.5 ke dalam variabel c
type(c)
# Mengambil informasi jenis tipe data pada variabel c yakni float
a / c
# Menghitung hasil pembagian dari 1205 / 12.5 = 96.4
a // c
# Menghitung hasil pembagian dari 1205 / 12.5 = 96.4 lalu membulatkannya menjadi 96
a % c
# Menghitung hasil sisa pembagian dari 1205 / 12.5 yakni 5.0

c > b
"""
Memeriksa apakah nilai dari variabel c lebih besar dari b maka 12.5 > 25 
akan menghasilkan nilai False
"""
type(c > b)
""" 
Mengambil informasi tipe data dari pemeriksaan kondisional, 
karena kondisi tersebut menghasilkan nilai False maka tipe datanya adalah boolean 
"""
a > b and b > c
""" 
- Memeriksa apakah a > b jadi 1205 > 25 maka akan menghasilkan nilai True, 
  lalu memeriksa apakah b > c jadi 25 > 12.5 maka akan menghasilkan nilai True.
- Karena ada keyword and maka kedua belah sisi harus menghasilkan nilai True 
  agar hasil bernilai benar.
- Karena (a > b) menghasilkan True dan (b > c) menghasilkan true, 
  maka (True and True) akan menghasilkan nilai True pula 
"""
a > 1100 or b < 10
"""
- Memeriksa apakah a > 1100 jadi 1205 > 1100 maka akan menghasilkan nilai True,
  lalu memeriksa apakah b < 10 jadi 25 < 10 maka akan menghasilkan nilai False.
- Karena ada keyword or maka apabila salah satu sisi menghasilkan nilai True 
  maka akan bernilai benar.
- Karena (a > 1100) menghasilkan True dan (b < 10) menghasilkan False, 
  maka (True or False) akan menghasilkan nilai True.
"""