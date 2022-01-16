import shelve

shelve_file = shelve.open('Zavier')
bio = shelve_file.get('Bio')

print(f"Student Id : {bio[0]}")
print(f"Name       : {bio[1]}")
print(f"Birth Date : {bio[2]}")

shelve_file.close()
