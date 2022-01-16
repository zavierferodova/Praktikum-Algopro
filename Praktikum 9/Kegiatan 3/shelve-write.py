import shelve

file = open('xxxxxxx205', 'r')
student_id = file.readline().strip()
birth_date = file.readline().strip()
name = file.readline().strip()

shelve_file = shelve.open('Zavier')
shelve_file["Bio"] = [student_id, name, birth_date]
shelve_file.close()
