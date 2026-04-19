import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, x, y):
        self.result = x + y
        return self.result
    
    def subtract(self, x, y):
        self.result = x - y
        return self.result
    
    def multiply(self, x, y):
        self.result = x * y
        return self.result
    
    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        self.result = x / y
        return self.result


class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x200")

        self.display = tk.Entry(root, font=("Arial", 20), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="nsew")
        
        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]
        
        for (text, row, col) in buttons:
            btn = tk.Button(root, text=text, font=("Arial", 18), 
                           command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, f"{expression} = {result}")
            except:
                messagebox.showerror("Error", "Invalid expression")
        else:
            self.display.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.lift()
    root.attributes('-topmost', True)
    root.mainloop()