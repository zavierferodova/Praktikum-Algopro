formulas = {
    'Segitiga'        : 'L = 0.5 * a * t',
    'Persegi'         : 'L = s ** 2',
    'Persegi Panjang' : 'L = p * l',
    'Lingkaran'       : 'L = phi * r ** 2',
    'Jajar Genjang'   : 'L = a * t'
}

print('No | Nama Bangun     | Rumus Luas')
print('---|-----------------|-------------------')
for index, key in enumerate(formulas.keys()):
    print(' {} | {:15} | {}'.format(index+1, key, formulas[key]))
    