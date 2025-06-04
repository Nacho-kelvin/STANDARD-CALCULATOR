import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Standard Calculator")
        self.root.geometry("300x450")
        self.root.resizable(False, False)
        
        # Custom font
        self.custom_font = font.Font(size=14)
        
        # Variables
        self.current_input = ""
        self.total_calculation = ""
        
        # Display frame
        self.display_frame = self.create_display_frame()
        
        # Buttons frame
        self.buttons_frame = self.create_buttons_frame()
        
        # Create display labels
        self.total_label, self.label = self.create_display_labels()
        
        # Create buttons
        self.create_buttons()
        
        # Bind keyboard events
        self.root.bind("<Key>", self.key_press)
        
    def create_display_frame(self):
        frame = tk.Frame(self.root, height=100, bg="light gray")
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_calculation, 
                              anchor=tk.E, bg="light gray", fg="black",
                              padx=10, font=self.custom_font)
        total_label.pack(expand=True, fill="both")
        
        label = tk.Label(self.display_frame, text=self.current_input, 
                        anchor=tk.E, bg="light gray", fg="black",
                        padx=10, font=font.Font(size=24, weight="bold"))
        label.pack(expand=True, fill="both")
        
        return total_label, label
    
    def create_buttons(self):
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3), ('C', 0, 4),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3), ('(', 1, 4),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3), (')', 2, 4),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3), ('⌫', 3, 4)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.buttons_frame, text=text, font=self.custom_font,
                              command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)
            
        # Configure row and column weights
        for i in range(4):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(5):
            self.buttons_frame.columnconfigure(i, weight=1)
    
    def on_button_click(self, text):
        if text == "=":
            try:
                self.total_calculation = self.current_input
                self.current_input = str(eval(self.current_input))
                self.update_display()
            except Exception as e:
                self.current_input = "Error"
                self.update_display()
                self.current_input = ""
        elif text == "C":
            self.current_input = ""
            self.total_calculation = ""
            self.update_display()
        elif text == "⌫":
            self.current_input = self.current_input[:-1]
            self.update_display()
        else:
            self.current_input += str(text)
            self.update_display()
    
    def key_press(self, event):
        key = event.char
        if key in '0123456789+-*/.()':
            self.current_input += key
            self.update_display()
        elif key == '\r':  # Enter key
            self.on_button_click("=")
        elif key == '\x08':  # Backspace
            self.on_button_click("⌫")
        elif key == '\x1b':  # Escape
            self.on_button_click("C")
    
    def update_display(self):
        self.label.config(text=self.current_input[:20])
        self.total_label.config(text=self.total_calculation[:20])
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    calculator.run()