try:
    import tkinter as tk
    from tkinter import font as tkfont
except ImportError:
    import Tkinter as tk
    import tkFont as tkfont

from PIL import Image, ImageTk

from splash_screen import SplashScreen
from cropselection_screen import CropSelectionScreen
from appselection_screen import AppSelectionScreen
from datatypeselection_screen import DataTypeSelectionScreen
from data_entry_screen import DataEntryScreen
from review_list_screen import ReviewListScreen

class MainApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family = 'Helvetica',
                                      size = 18,
                                      weight = "bold",
                                      slant = "italic")

        # Frameless/No title bar 
        #self.overrideredirect(True)

        # Define the program to be draggable
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)
 

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Pre-load every frame
        #for F in (SplashScreen, PageOne, PageTwo):
        for F in (SplashScreen,
                  CropSelectionScreen,
                  AppSelectionScreen,
                  DataTypeSelectionScreen,
                  DataEntryScreen,
                  ReviewListScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        # Start with the StartPage
        #self.show_frame("DataEntryScreen")
        self.show_frame("ReviewListScreen")

    # Because we RootWindow=controller has all the other classes as objects saved
    # we can reference and call any of those frames to show on top of the others
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


    def resize_image(event):
        new_width = event.width
        new_height = event.height
        # Resize the original image to fit the new dimensions
        resized_image = original_image.thumbnail((new_width, new_height))
        new_photo = ImageTk.PhotoImage(resized_image)
        background_label.config(image=new_photo)
        background_label.image = new_photo

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def stop_move(self, event):
        self.x = None
        self.y = None

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

## Create the main window
#root = tk.Tk()
#root.title("Responsive Background Image")
#root.minsize(940, 480)
#
## Load the original image using Pillow
#image_path = "./assets/splash/splash2.png"
## original_image = tk.PhotoImage(image_path)
#original_image = Image.open(image_path)
#photo = ImageTk.PhotoImage(original_image)
#
## Create a frame
#frame = tk.Frame(root)
#frame.pack(fill=tk.BOTH, expand=True)
#
## Create a Label widget to display the image
#background_label = tk.Label(frame, image=photo)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
#
## Bind the resize event to the resize_image function
#frame.bind("<Configure>", resize_image)
#
## Add other widgets on top of the background image
#label = tk.Label(frame, text="Hello, World!", bg="white")
#label.pack(pady=20)
#
#
## Start the Tkinter event loop
#root.mainloop()
## suck my dick - Kate
## i suck yours, you suck mine - Me
