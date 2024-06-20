import tkinter as tk

WINDOW_MIN_WIDTH = 800
WINDOW_MIN_HEIGHT = 600
APP_TITLE = "Test app"

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.password_input_field_val = tk.StringVar()
        self.use_letters = tk.IntVar()
        self.use_digits = tk.IntVar()
        self.use_punctuation = tk.IntVar()
        self.createWidgets()
        self.arrange_widgets_in_grid()

    def createWidgets(self):
        self.password_input_field = tk.Entry(self, textvariable=self.password_input_field_val)
        self.use_letters_checkbox = tk.Checkbutton(self, text="Use Letters", )
        self.generate_password_button = tk.Button(self, text="Generate Password", command=self.quit)

    def arrange_widgets_in_grid(self):
        self.use_letters_checkbox.grid(padx=10, pady=10, row=1, column=2)
        self.generate_password_button.grid(padx=10, pady=15, row=2, columnspan=4)