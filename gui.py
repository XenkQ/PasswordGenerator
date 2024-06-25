# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer
# And then edited and refectored by xenkq
import tkinter
import pyperclip
from pathlib import Path
from password import CHARACTERS_BAD_FOR_PASSWORD, Password

# Explicit imports to satisfy Flake8
from tkinter import *
from value_operations import ValueOperations

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("img")

APP_NAME = "Password Generator"

COUNT_ENTRY_MIN_VALUE_LIMIT = 0
COUNT_ENTRY_MAX_VALUE_LIMIT = 64
COUNT_ENTRY_START_VALUE = 3

DEFAULT_ENTRY_STYLE_KWARGS = {
    'bd': 0,
    'fg': '#FFFFFF',
    'highlightthickness': 0,
    'font': ('Arial', 14),
    'insertbackground': "white"
}


class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        self.window.configure(bg="#B8E994")
        self.window.resizable(False, False)
        self.window.title(APP_NAME)

        self.entry_vars = {}
        self.var_associated_with_entry = {}

        canvas = Canvas(
            self.window,
            bg="#B8E994",
            height=600,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        increase_button_image = PhotoImage(file=self.relative_to_images("arrow_up_button.png"))
        decrease_button_image = PhotoImage(file=self.relative_to_images("arrow_down_button.png"))

        # ==============================Password entry widget with reset and copy buttons==============================#

        self.password_entry_var = StringVar()

        canvas.place(x=0, y=0)
        entry_image_1 = PhotoImage(
            file=self.relative_to_images("password_entry.png"))

        canvas.create_image(
            351.0,
            60.0,
            image=entry_image_1,
        )

        self.password_entry = Entry(
            **DEFAULT_ENTRY_STYLE_KWARGS,
            bg="#78E08F",
            textvariable=self.password_entry_var
        )

        self.password_entry.place(
            x=62.0,
            y=44.0,
            width=578.0,
            height=30.0
        )

        button_image_1 = PhotoImage(
            file=self.relative_to_images("regenerate_button.png"))

        generate_password_button = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_password_entry_value_to_new_generated_password(),
            relief="flat"
        )

        generate_password_button.place(
            x=663.0,
            y=40.0,
            width=40.0,
            height=40.0
        )

        button_image_2 = PhotoImage(
            file=self.relative_to_images("copy_button.png"))

        copy_password_button = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: pyperclip.copy(self.password_entry_var.get()),
            relief="flat"
        )

        copy_password_button.place(
            x=712.0,
            y=40.0,
            width=40.0,
            height=40.0
        )

        # ============================================================================================================#

        image_image_1 = PhotoImage(
            file=self.relative_to_images("app_background.png"))

        canvas.create_image(
            399.0,
            329.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=self.relative_to_images("section_background.png"))

        canvas.create_image(
            399.0,
            343.0,
            image=image_image_2
        )

        button_image_3 = PhotoImage(
            file=self.relative_to_images("exit_button.png"))

        exit_button = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: exit(0),
            relief="flat"
        )

        exit_button.place(
            x=67.0,
            y=498.0,
            width=99.0,
            height=40.0
        )

        canvas.create_text(
            67.0,
            125.0,
            anchor="nw",
            text="Password strength: no input",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        entry_image_2 = PhotoImage(
            file=self.relative_to_images("exclude_entry.png"))

        canvas.create_image(
            425.5,
            395.0,
            image=entry_image_2
        )

        canvas.create_text(
            67.0,
            185.0,
            anchor="nw",
            text="Char options",
            fill="#3C6382",
            font=("Inter", 20 * -1)
        )

        canvas.create_text(
            99.0,
            384.0,
            anchor="nw",
            text="Exclude",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        canvas.create_text(
            115.0,
            308.0,
            anchor="nw",
            text="Count",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        image_image_7 = PhotoImage(
            file=self.relative_to_images("label_background_2.png"))

        canvas.create_image(
            223.0,
            287.0,
            image=image_image_7
        )

        canvas.create_text(
            208.0,
            276.0,
            anchor="nw",
            text="A-Z",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        canvas.create_image(
            336.0,
            287.0,
            image=image_image_7
        )

        canvas.create_text(
            325.0,
            276.0,
            anchor="nw",
            text="a-z",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        canvas.create_image(
            451.0,
            287.0,
            image=image_image_7
        )

        canvas.create_text(
            439.0,
            276.0,
            anchor="nw",
            text="0-9",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        # ==========================================Exclude entry widget=============================================#

        self.exclude_entry = Entry(
            **DEFAULT_ENTRY_STYLE_KWARGS,
            bg="#38ADA9"
        )

        self.exclude_entry.place(
            x=178.0,
            y=380.0,
            width=495.0,
            height=28.0
        )

        entry_image_3 = PhotoImage(
            file=self.relative_to_images("count_entry.png"))

        canvas.create_image(
            217.5,
            321.0,
            image=entry_image_3
        )

        self.exclude_entry.insert(0, CHARACTERS_BAD_FOR_PASSWORD)

        # ============================================================================================================#

        #===================================Upper az count entry widget with buttons==================================#

        self.upper_az_count_entry_var = IntVar(value=COUNT_ENTRY_START_VALUE)
        self.upper_az_count_entry_var.trace_add('write', self.on_count_entry_value_change)

        self.upper_az_count_entry = Entry(
            **DEFAULT_ENTRY_STYLE_KWARGS,
            bg="#38ADA9",
            justify="right",
            textvariable=self.upper_az_count_entry_var
        )

        var_name = str(self.upper_az_count_entry_var)
        self.entry_vars[var_name] = self.upper_az_count_entry_var
        self.var_associated_with_entry[var_name] = self.upper_az_count_entry

        self.upper_az_count_entry.place(
            x=178.0,
            y=311.0,
            width=79.0,
            height=18.0
        )

        image_image_3 = PhotoImage(
            file=self.relative_to_images("entry_background_1.png"))

        canvas.create_image(
            215.0,
            321.0,
            image=image_image_3
        )

        upper_az_count_increment_button = Button(
            image=increase_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.upper_az_count_entry_var, 1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        upper_az_count_increment_button.place(
            x=257.0,
            y=306.0,
            width=16.0,
            height=15.0
        )

        upper_az_count_decrement_button = Button(
            image=decrease_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.upper_az_count_entry_var, -1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        upper_az_count_decrement_button.place(
            x=257.0,
            y=321.0,
            width=16.0,
            height=15.0
        )

        entry_image_4 = PhotoImage(
            file=self.relative_to_images("count_entry.png"))

        canvas.create_image(
            330.5,
            321.0,
            image=entry_image_4
        )

        # ============================================================================================================#

        # ==================================Lower az count entry widget with buttons==================================#

        self.lower_az_count_entry_var = IntVar(value=COUNT_ENTRY_START_VALUE)
        self.lower_az_count_entry_var.trace_add('write', self.on_count_entry_value_change)

        self.lower_az_count_entry = Entry(
            **DEFAULT_ENTRY_STYLE_KWARGS,
            bg="#38ADA9",
            justify="right",
            textvariable=self.lower_az_count_entry_var
        )

        var_name = str(self.lower_az_count_entry_var)
        self.entry_vars[var_name] = self.lower_az_count_entry_var
        self.var_associated_with_entry[var_name] = self.lower_az_count_entry

        self.lower_az_count_entry.place(
            x=291.0,
            y=311.0,
            width=79.0,
            height=18.0
        )

        image_image_4 = PhotoImage(
            file=self.relative_to_images("entry_background_1.png"))

        canvas.create_image(
            328.0,
            321.0,
            image=image_image_4
        )

        lower_az_count_increment_button = Button(
            image=increase_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.lower_az_count_entry_var, 1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        lower_az_count_increment_button.place(
            x=370.0,
            y=306.0,
            width=16.0,
            height=15.0
        )

        lower_az_count_decrement_button = Button(
            image=decrease_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.lower_az_count_entry_var, -1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        lower_az_count_decrement_button.place(
            x=370.0,
            y=321.0,
            width=16.0,
            height=15.0
        )

        entry_image_5 = PhotoImage(
            file=self.relative_to_images("count_entry.png"))

        canvas.create_image(
            445.5,
            321.0,
            image=entry_image_5
        )

        # ============================================================================================================#

        # ===================================Digits count entry widget with buttons===================================#

        self.digits_count_entry_var = IntVar(value=COUNT_ENTRY_START_VALUE)
        self.digits_count_entry_var.trace_add('write', self.on_count_entry_value_change)

        self.digits_count_entry = Entry(
            **DEFAULT_ENTRY_STYLE_KWARGS,
            bg="#38ADA9",
            justify="right",
            textvariable=self.digits_count_entry_var
        )

        var_name = str(self.digits_count_entry_var)
        self.entry_vars[var_name] = self.digits_count_entry_var
        self.var_associated_with_entry[var_name] = self.digits_count_entry

        self.digits_count_entry.place(
            x=406.0,
            y=311.0,
            width=79.0,
            height=18.0
        )

        image_image_5 = PhotoImage(
            file=self.relative_to_images("entry_background_1.png"))

        canvas.create_image(
            443.0,
            321.0,
            image=image_image_5
        )

        digits_count_increase_button = Button(
            image=increase_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.digits_count_entry_var, 1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        digits_count_increase_button.place(
            x=485.0,
            y=306.0,
            width=16.0,
            height=15.0
        )

        digits_count_decrease_button = Button(
            image=decrease_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.digits_count_entry_var, -1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        digits_count_decrease_button.place(
            x=485.0,
            y=321.0,
            width=16.0,
            height=15.0
        )

        # ============================================================================================================#

        # =============================Special characters count entry widget with buttons=============================#

        self.special_characters_count_entry_var = IntVar(value=COUNT_ENTRY_START_VALUE)
        self.special_characters_count_entry_var.trace_add('write', self.on_count_entry_value_change)

        self.special_characters_count_entry = Entry(
            **DEFAULT_ENTRY_STYLE_KWARGS,
            bg="#38ADA9",
            justify="right",
            textvariable=self.special_characters_count_entry_var
        )

        var_name = str(self.digits_count_entry_var)
        self.entry_vars[var_name] = self.special_characters_count_entry_var
        self.var_associated_with_entry[var_name] = self.special_characters_count_entry

        self.special_characters_count_entry.place(
            x=520.0,
            y=311.0,
            width=142.0,
            height=18.0
        )

        image_image_6 = PhotoImage(
            file=self.relative_to_images("entry_background_2.png"))

        canvas.create_image(
            588.0,
            321.0,
            image=image_image_6
        )

        special_character_count_increase_button = Button(
            image=increase_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.special_characters_count_entry_var, 1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        special_character_count_increase_button.place(
            x=662.0,
            y=306.0,
            width=16.0,
            height=15.0
        )

        special_character_count_decrease_button = Button(
            image=decrease_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: ValueOperations.add_value_to_entry_var_if_new_val_in_range(
                self.special_characters_count_entry_var, -1, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT
            ),
            relief="flat"
        )

        special_character_count_decrease_button.place(
            x=662.0,
            y=321.0,
            width=16.0,
            height=15.0
        )

        image_image_10 = PhotoImage(
            file=self.relative_to_images("label_background_1.png"))

        canvas.create_image(
            596.0,
            287.0,
            image=image_image_10
        )

        canvas.create_text(
            523.0,
            276.0,
            anchor="nw",
            text="Special characters",
            fill="#3C6382",
            font=("Inter", 18 * -1)
        )

        # ============================================================================================================#

        self.set_password_entry_value_to_new_generated_password()
        self.window.mainloop()

    def relative_to_images(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def on_count_entry_value_change(self, *args):
        if args[0] in self.entry_vars and args[0] in self.var_associated_with_entry:
            var = self.entry_vars[args[0]]

            try:
                value = var.get()

                if not ValueOperations.value_in_range(value, COUNT_ENTRY_MIN_VALUE_LIMIT, COUNT_ENTRY_MAX_VALUE_LIMIT):
                    if value > COUNT_ENTRY_MAX_VALUE_LIMIT:
                        var.set(COUNT_ENTRY_MAX_VALUE_LIMIT)

                    if value < COUNT_ENTRY_MIN_VALUE_LIMIT:
                        var.set(COUNT_ENTRY_MIN_VALUE_LIMIT)

                    self.var_associated_with_entry[args[0]].icursor(END)
                    self.set_password_entry_value_to_new_generated_password()

            except tkinter.TclError:
                self.var_associated_with_entry[args[0]].delete(0, END)


            value = var.get()
            print(var.get())
            if value != 0:
                var.set(var.get())


    def set_password_entry_value_to_new_generated_password(self):
        pwd = Password.generate_password(
            self.lower_az_count_entry_var.get(),
            self.upper_az_count_entry_var.get(),
            self.digits_count_entry_var.get(),
            self.special_characters_count_entry_var.get(),
            self.exclude_entry.get()
        )

        self.password_entry_var.set(pwd)
