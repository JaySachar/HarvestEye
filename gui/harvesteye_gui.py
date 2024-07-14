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
from final_review_screen import FinalReviewScreen

class MainApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family = 'Helvetica',
                                      size = 18,
                                      weight = "bold",
                                      slant = "italic")

        # Default value is chili
        self.crop = 'chili'
        self.back_history = []

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
                  ReviewListScreen,
                  FinalReviewScreen):
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
        #self.frames['ReviewListScreen'].event_generate("<<ShowFrame>>")
        frame = self.frames[page_name]
        frame.event_generate("<<ShowFrame>>")
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

