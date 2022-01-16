times = ('pagi', 'siang', 'sore', 'petang', 'malam')

name = input('Siapa namamu : ')
time_now = float(input('Pukul berapa sekarang : '))

if time_now < 12:
    print(f'Selamat {times[0]} {name}.')
elif 12 >= time_now < 15 :
    print(f'Selamat {times[1]} {name}.')
elif 15 >= time_now < 17:
    print(f'Selamat {times[2]} {name}.')
elif 17 >= time_now < 19:
    print(f'Selamat {times[3]} {name}.')
else:
    print(f'Selamat {times[4]} {name}.')