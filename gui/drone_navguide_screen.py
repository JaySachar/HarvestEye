import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from widgets.logo_frame import LogoFrame

class DroneNavGuideScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Reference to the MainApp() and it's __init__ variables
        self.controller = controller

        #self.image_path = "./assets/datatype-select/"
        self.configure(bg="white")
        self.image_path = "./assets/drone-navguide/"

        self.topPage()
        self.centerPage()
        self.bottomPage()

    def topPage(self):
        # Load the EXIT button
        top_page_frame = tk.Frame(self)
        top_page_frame.pack(side="top", fill='x', expand=False)
        top_page_frame.configure(bg="white")


        photo = ImageTk.PhotoImage(Image.open(self.image_path+"btn-back_sm.png"))
        btn_back = tk.Label(top_page_frame, image=photo )
        btn_back.image = photo
        btn_back.bind('<Button-1>', self.backButton)
        btn_back.pack(side="left", expand=False, padx=10, pady=10, anchor="nw")
        btn_back.configure(bg='white')


        photo = ImageTk.PhotoImage(Image.open(self.image_path+"btn-exit_sm.png"))
        btn_exit = tk.Label(top_page_frame, image=photo )
        btn_exit.image = photo
        btn_exit.bind('<Button-1>', self.exitButton)
        btn_exit.pack(side="right", expand=False, padx=10, pady=10, anchor="ne")
        btn_exit.configure(bg='white')

        # Step # label
        txt_version = tk.Label(top_page_frame, text = "STEP 2.5 drone navigation guide")
        txt_version.pack(side="bottom",  anchor="sw", padx=30 )
        txt_version.configure(bg='white')

    def centerPage(self):
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_drone_navguide_sm.png"))
        drone_navguide = tk.Label(self, image=photo )
        drone_navguide.image = photo
        drone_navguide.pack(side="top", expand=True, anchor="center")
        drone_navguide.configure(bg='white')


    def bottomPage(self):
        #BottomBar

        bottom_bar_frame = tk.Frame(self)
        bottom_bar_frame.pack(side="left", fill='x', expand=True)
        bottom_bar_frame.configure(bg='white')

        # ------------------------------
        #Logo frame that  goes to the bottom right

        #logo_frame = LogoFrame(self)
        #logo_frame.pack(side="right", anchor="s")


        # Write text for Version number
        txt_version = tk.Label(bottom_bar_frame, text = "Version 1.00")
        txt_version.pack(side="bottom", fill='x')
        txt_version.configure(bg='white')

        # Drone progress bar
        # Image of Drone Progress Bar
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_bottomdrone_sm.png"))
        img_graybtnbackground= tk.Label(bottom_bar_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.pack(side="bottom", fill='x')
        img_graybtnbackground.configure(bg='white')



        ## ========================================/
        #self.image_path = "./assets/datatype-select/"


    def backButton(self, event):
        try:
            self.controller.show_frame(self.controller.back_history.pop())
        except:
            print("Nowhere to go. Back button stack is empty")
            self.controller.show_frame("SplashScreen")


    def openButton(self, event):
        self.controller.back_history.append("SplashScreen")
        self.controller.show_frame("CropSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()



