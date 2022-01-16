from tkinter import Button, Frame, Label, Tk
from tkinter.font import Font

bio = [
    ['NIM', ':', 'xxxxxxx205'],
    ['Nama', ':', 'Zavier Ferodova Al Fitroh'],
    ['Kelamin', ':', 'Laki-Laki'],
    ['Agama', ':', 'Islam']
]

app = Tk(className='bio mahasiswa')
app.geometry('300x300')
app.resizable(False, False)


frame = Frame()
frame.pack(anchor='center')

for row_index, row_data in enumerate(bio):
    for column_index, column_data in enumerate(row_data):
        if (column_index == 0):
            lbl = Label(frame, text=column_data, font=Font(weight='bold', size=10))
            lbl.grid(row=row_index, column=column_index, sticky='w')
        else:
            lbl = Label(frame, text=column_data)
            lbl.grid(row=row_index, column=column_index, sticky='w')

button = Button(app, text='Tutup', command=app.quit, width=8)
button.pack(anchor='center', pady=10)

app.mainloop()