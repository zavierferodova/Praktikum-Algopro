from math import sqrt
from tkinter import Button, Entry, Label, Tk
from tkinter.font import Font
from tkinter import messagebox as mb

class PyramidCalculator:
    def __init__(self, window: Tk):
        self.app = window
        self.__init_components()

    def __init_components(self):
        app = self.app
        self.label_s = Label(app, text='Panjang alas :', anchor='w')
        self.entry_s = Entry(app)
        self.label_t = Label(app, text='Tinggi bangun :', anchor='w')
        self.entry_t = Entry(app)
        self.btn_calc = Button(app, text='Hitung', command=self.__calculate)
        self.label_rs = Label(app, text='Hasil', font=Font(weight='bold', size=11))
        self.label_res = Label(app, text='0')

    def render(self):
        self.label_s.pack(fill='x', padx=10)
        self.entry_s.pack(fill='x', padx=10)
        self.label_t.pack(fill='x', padx=10)
        self.entry_t.pack(fill='x', padx=10)
        self.btn_calc.pack(anchor='center', pady=20)
        self.label_rs.pack(anchor='center')
        self.label_res.pack(anchor='center')
        self.app.mainloop()

    def __calculate(self):
        base_w = float(self.entry_s.get() or 0)
        height = float(self.entry_t.get() or 0)
        tr_height = sqrt(((base_w/2)**2) + (height**2))

        if base_w == 0:
            mb.showerror('Alert', 'Panjang alas tidak boleh kosong')
        elif height == 0:
            mb.showerror('Alert', 'Tinggi bangun tidak boleh kosong')
        else:
            area = (base_w**2) + (4 * (0.5 * base_w * tr_height))
            self.label_res.config(text=area)

def main():
    window = Tk(className='pyramid area calculator')
    window.geometry('300x300')
    app = PyramidCalculator(window)
    app.render()

main()
