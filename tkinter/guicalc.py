import tkinter as tk  # noqa: INP001
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("640x480")

        self.num1 = tk.StringVar(self)
        self.numone = tk.Entry(self, textvariable=self.num1)
        self.numone.grid(row=0, column=0, padx=10, pady=10)

        self.combobox = ttk.Combobox(self, values=["+", "-", "*", "/"],
                                     state="readonly")
        self.combobox.grid(row=0, column=1, padx=10, pady=10)

        self.num2 = tk.StringVar(self)
        self.numtwo = tk.Entry(self, textvariable=self.num2)
        self.numtwo.grid(row=0, column=2, padx=10, pady=10)

        self.equal = tk.Label(self, text="=")
        self.equal.grid(row=0, column=3, padx=10, pady=10)

        self.calculated = tk.Label(self)
        self.calculated.grid(row=0, column=4, padx=10, pady=10)

        self.calculateButton = tk.Button(self, text="Vypočítat",
                                         command=self.showcalculated)
        self.calculateButton.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.bind("<Return>", self.showcalculated)

    def calculate(self, lambdafunc):
        try:
            self.calculated.config(text=lambdafunc(float(self.num1.get()),
                                                   float(self.num2.get())))
        except ValueError:
            self.calculated.config(text="Chyba!")

    def showcalculated(self, _event=None):
        match self.combobox.get():
            case "+":
                self.calculate(lambda a, b: a + b)
            case "-":
                self.calculate(lambda a, b: a - b)
            case "*":
                self.calculate(lambda a, b: a * b)
            case "/":
                self.calculate(lambda a, b: a / b)


if __name__ == "__main__":
    app = App()
    app.mainloop()
