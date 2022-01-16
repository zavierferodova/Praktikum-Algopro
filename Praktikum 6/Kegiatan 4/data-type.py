name = 'Zavier Ferodova Al Fitroh'
student_id = 205
body_height = 1.67
body_weight = 54
birth_year = 0000
me = (birth_year, body_weight, body_height, student_id, name)
data = [birth_year, body_weight, body_height, student_id, name]

type(me)
# Mengambil informasi tipe data dari variabel me yakni Tuple 
# karena diawali dan diakhiri tanda kurung ()
me[0]
# Mengambil index 0 dari variabel me yakni birth_year dengan value 0000
a = student_id % 4; me[a]
# Melakukan pembagian sisa dari student_id dengan 4 yang berarti 205 / 4 yakni 1
# Lalu mengambil index 1 dari variabel me yakni body_weight dengan value 54
type(me[a])
# Karena value dari me[a] adalah body_weight yang bernilai 54 maka tipe datanya
# adalah integer
me[a:4]
# Melakukan slicing index variabel me dari index ke - 1 sampai ke - 4
# Maka akan berisi (body_weight, body_height, student_id)
# Maka yang tampil di screen adalah (54, 1.67, 205)
type(me[4])
# Mengambil nilai dari index 4 variabel me yakni name
# Karena name berisi teks maka tipe datanya adalah string
me[0] = 'ok'
# Menghasilkan error karena tipe data dari variabel me adalah tuple
# yang mana tuple tidak bisa diubah value elemennya.

type(data)
# Mengambil informasi tipe data dari variabel data yakni list
type(data[4])
# Mengambil informasi tipe data dari value data index ke - 4
# yakni name yang bernilai teks maka tipe nya adalah string
data[4][5]
# Karena value data pada index ke - 4 berisi string Zavier Ferodova Al Fitroh
# Maka index ke - 5 dari teks tersebut adalah karakter 'r'

data[4][a:6]
# Karena value data pada index ke - 4 berisi string Zavier Ferodova Al Fitroh
# Karena nilai a adalah 1, maka slicing 1:6 akan bernilai avier
data[0] = 'ok'; data
# Mengubah index ke - 0 dari variabel data lalu menampilkannya ke layar
# Maka akan tampil ['ok', 54, 1.67, 205, 'Zavier Ferodova Al Fitroh']
data[-a]
# Karena a bernilai 1 maka index -1 dari data berisi variabel name
# Maka akan tampil di layar Zavier Ferodova Al Fitroh
range(a)
# Karena a bernilai 1 maka nilai range(a) akan menghasilkan range(0, 1)
# Karena nilai awalan dari range tidak ada dalam input maka default bernilai 0
# dan jika dirubah menjadi list dengan list(range(a)) akan menghasilkan nilai [0]
list(range(a))