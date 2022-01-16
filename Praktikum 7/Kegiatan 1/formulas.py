formulas = {
    'Triangle'     : 'L = 0.5 * a * t',
    'Square'       : 'L = s ** 2',
    'Rectangle'    : 'L = p * l',
    'Circle'       : 'L = phi * r ** 2',
    'Parallelogram': 'L = a * t'
}

print(f'''
No | Nama Bangun     | Rumus Luas
---|-----------------|-------------------
 1 | Segitiga        | {formulas['Triangle']}
 2 | Persegi         | {formulas['Square']}
 3 | Persegi Panjang | {formulas['Rectangle']}
 4 | Lingkaran       | {formulas['Circle']}
 5 | Jajar Genjang   | {formulas['Parallelogram']}
''')