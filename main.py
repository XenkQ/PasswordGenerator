import random
import string
import application
from password import Password

if __name__ == "__main__":
    app = application.Application()
    app.master.title(application.APP_TITLE)
    app.master.minsize(application.WINDOW_MIN_WIDTH, application.WINDOW_MIN_HEIGHT)
    app.master.grid_size()
    app.mainloop()