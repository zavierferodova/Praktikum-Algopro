file = open('xxxxxxx205', 'a+')
file.write('Indonesia')
file.seek(0)

student_id = file.readline().strip()
birth_date = file.readline().strip()
name = file.readline().strip()
birth_city = file.readline().strip()

birth_date_list = birth_date.split('-')

file.close()
print(name)
print(f"{birth_city}, {'/'.join(birth_date_list)}")
print(student_id)