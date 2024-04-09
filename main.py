import tkinter as tk


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error"
    return x / y


def power(x, y):
    return x ** y


def sqrtl(x):
    if x < 0:
        return "Error"
    return x ** 0.5


def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Error"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.master.geometry("270x335")
        self.master.resizable(False, False)

        self.background_color = "#242424"
        self.button_color = "#1C1C1C"
        self.operator_button_color = "#666666"
        self.equals_button_color = "#0052CC"
        self.master.configure(bg=self.background_color)

        self.default_font = ("Segoe UI", 16)
        self.operator_font = ("Segoe UI", 16, "bold")

        self.button_style = {"bg": self.button_color, "fg": "white", "font": self.default_font, "bd": 0, "height": 2,
                             "width": 4}
        self.operator_button_style = {"bg": self.operator_button_color, "fg": "white", "font": self.operator_font,
                                      "bd": 0, "height": 2, "width": 4}
        self.equals_button_style = {"bg": self.equals_button_color, "fg": "white", "font": self.default_font, "bd": 0,
                                    "height": 2, "width": 4}

        self.current_expression = tk.StringVar()
        self.current_expression.set("0")
        self.display = tk.Entry(master, textvariable=self.current_expression, justify='right', bd=0, state='readonly',
                                font=("Segoe UI", 24), bg="black", fg="black")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('×', 4, 3),
            ('C', 5, 0), ('0', 5, 1), ('.', 5, 2), ('÷', 5, 3),
            ('=', 6, 0), ('!', 6, 1), ('√', 6, 2), ('^', 6, 3),
        ]

        for (text, row, col) in self.buttons:
            self.add_button(text, row, col)

        self.master.grid_rowconfigure(1, weight=1)
        for i in range(2, 7):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i - 2, weight=1)

    def update_display(self, value):
        font_size = 24
        if len(value) > 10:
            font_size = max(24 - (len(value) - 10), 10)
        self.display.config(font=("Segoe UI", font_size))
        self.current_expression.set(value)

    def add_button(self, text, row, col):
        if text in {'+', '-', '×', '÷', '^', '√', '!'}:
            style = self.operator_button_style
        elif text == '=':
            style = self.equals_button_style
        else:
            style = self.button_style

        button = tk.Button(self.master, text=text, command=lambda: self.on_button_click(text), **style)
        if text == '=':
            button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)
        else:
            button.grid(row=row, column=col, sticky="nsew", padx=1, pady=1)

    def on_button_click(self, value):
        if value in {'+', '-', '×', '÷', '^', '√', '!', '='}:
            current = self.current_expression.get()
            if current.endswith(('+', '-', '×', '÷', '^')) and value in {'+', '-', '×', '÷', '^'}:
                current = current[:-1] + value
            elif value == '=':
                self.calculate_expression()
            else:
                if current == "0":
                    current = ""
                self.update_display(current + value)
        elif value == 'C':
            self.update_display("0")
        else:
            current = self.current_expression.get()
            if current == "0":
                current = ""
            self.update_display(current + value)

    def calculate_expression(self):
        expression = self.current_expression.get()
        operators = {'^': power, '√': sqrtl, '!': factorial, '×': multiply, '÷': divide, '+': add, '-': subtract}

        elements = []
        current_number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    elements.append(float(current_number))
                    current_number = ''
                elements.append(char)
        if current_number:
            elements.append(float(current_number))

        for op in ['!', '√']:
            if op == '√':
                indices = [i for i, x in enumerate(elements) if x == op]
                for op_index in reversed(indices):
                    result = operators[op](elements[op_index + 1])
                    elements[op_index:op_index + 2] = [result]
            elif op == '!':
                while op in elements:
                    op_index = elements.index(op)
                    result = operators[op](int(elements[op_index - 1]))
                    elements[op_index - 1:op_index + 1] = [result]

        for op in ['^', '×', '÷', '+', '-']:
            while op in elements:
                op_index = elements.index(op)
                result = operators[op](elements[op_index - 1], elements[op_index + 1])
                elements[op_index - 1:op_index + 2] = [result]

        self.update_display(str(sum(elements)))


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
