from tkinter import Button, Entry, Frame, Label, Tk

class Calculator:
    def __init__(self):
        self.__init_components()

    def __init_components(self):
        self.app = Tk(className='calculator')

        app = self.app
        self.lbl1 = Label(app, text='Angka 1', anchor='w')
        self.entry1 = Entry(app)
        self.lbl2 = Label(app, text='Angka 2', anchor='w')
        self.entry2 = Entry(app)

        frame_btn = Frame(app)
        self.frame_btn = frame_btn
        self.btn_plus = Button(frame_btn, text='+', width=5, command=lambda: self.__calculate('+'))
        self.btn_minus = Button(frame_btn, text='-', width=5, command=lambda: self.__calculate('-'))
        self.btn_power = Button(frame_btn, text='*', width=5, command=lambda: self.__calculate('*'))
        self.btn_divide = Button(frame_btn, text='/', width=5, command=lambda: self.__calculate('/'))

        frame_result = Frame(app)
        self.frame_result = frame_result
        self.lbl3 = Label(frame_result, text='Hasil')
        self.lbl_result = Label(frame_result, text='0')

    def render(self):
        self.app.geometry('300x300')
        self.app.resizable(False, False)
        self.lbl1.pack(fill='x', padx=10)
        self.entry1.pack(fill='x', padx=10)
        self.lbl2.pack(fill='x', padx=10)
        self.entry2.pack(fill='x', padx=10)

        self.frame_btn.pack(pady=10, anchor='center')
        self.btn_plus.grid(row=0, column=0)
        self.btn_minus.grid(row=0, column=1)
        self.btn_power.grid(row=0, column=3)
        self.btn_divide.grid(row=0, column=4)

        self.frame_result.pack(fill='x', padx=10)
        self.lbl3.grid(row=0, column=0)
        self.lbl_result.grid(row=0, column=1)

        self.app.mainloop()

    def __calculate(self, operator):
        val1 = self.entry1.get() or 0
        val2 = self.entry2.get() or 0
        result = 0
        lbl_result = self.lbl_result

        if (operator == '+'):
            result = float(val1) + float(val2)
        elif (operator == '-'):
            result = float(val1) - float(val2)
        elif (operator == '*'):
            result = float(val1) * float(val2)
        elif (operator == '/'):
            result = float(val1) / float(val2)
        lbl_result.config(text=result)

def main():
    calculator = Calculator()
    calculator.render()

main()