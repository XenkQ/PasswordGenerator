# Password Generator
## Idea
When searching for gui builder that is using tkinter I found this repo https://github.com/ParthJadhav/Tkinter-Designer so I wanted to test it with simple app. Tkinter Designer is great tool for making simple apps design in figma and then convert it to tk inter app.
## How it looks
![passgen](https://github.com/XenkQ/PasswordGenerator/assets/77151114/08b540ca-2fb8-43a6-b64b-8e57a70d6d71)
## Stack
- python
- tkinter
- figma (for app design)
- https://github.com/ParthJadhav/Tkinter-Designer (It seems to me that it is a good tool for small projects, but for medium and larger projects you can feel its limits for example, a limited number of widgets compatible with tkinter)
- PyInstaller (for making exe file with following command: *python -m PyInstaller --onefile --name="Password Generator" --windowed --hidden-import=pyperclip --icon=img/key.ico main.py*)
