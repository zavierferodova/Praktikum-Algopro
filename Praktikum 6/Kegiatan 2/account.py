import random as rand

name = 'Zavier Ferodova Al Fitroh'
birth_date = 'dd mm yyyy'
short_name = f"{name[:6]} {name[7]}.{name[16]}.{name[19]}"
username = name[0] + birth_date[:2] + birth_date[-1:-5:-1]
password = name[:3] + ''.join([str(rand.randint(0, 9)) for i in range(3)])

print(f"Name       : {name}")
print(f"Short Name : {short_name}")
print(f"Birth Date : {birth_date}")
print(f"Username   : {username}")
print(f"Password   : {password}")