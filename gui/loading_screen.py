import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
#from widgets.sidebar.sidebar_crop import SidebarCrop
from widgets.logo_frame import LogoFrame

class LoadingScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='white')

        # ========================================/
        #### Load all the images in ####
        self.image_path = "./assets/app-select/"


        print(f"Right after assigning a variable crop: {self.controller.crop}")
        ########################### Side bar ##############################

        self.center_frame()
        self.bottomPage()

        #self.bind("<<ShowFrame>>", self.onShowFrame)


    def bottomPage(self):
        #BottomBar

        bottom_bar_frame = tk.Frame(self)
        bottom_bar_frame.pack(side="left", fill='x', expand=True)
        bottom_bar_frame.configure(bg='white')

        # ------------------------------
        #Logo frame that  goes to the bottom right
        logo_frame = LogoFrame(bottom_bar_frame)
        logo_frame.pack(side="right", anchor="s")
        logo_frame.configure(bg='green')

        # Actual bottom_bar_frame stuff
        # Write text for Version number
        txt_version = tk.Label(bottom_bar_frame, text = "Version 1.00")
        txt_version.pack(side="bottom")
        #txt_version.grid(row=3,column=1,columnspan=2, padx=5, pady=5, sticky="s")
        txt_version.configure(bg='white')


    def center_frame(self):
        ###################################################################
        ######################## Right Side with buttons ##################

        foreground_frame = tk.Frame(self)
        foreground_frame.pack(side="top", expand=True, anchor='center')
        foreground_frame.configure(bg="gray")

        loading_font = ('Montserrat', 42, "bold")
        txt_loading = tk.Label(foreground_frame, text="Loading...")
        txt_loading.configure(font = loading_font, pady=50, bg="white")


        #txt_loading.tag_configure("center", justify='center')
        #txt_loading.tag_add("center", "1.0", "end")

        txt_loading.pack(side="top",  anchor="center")


        ###################################################################

#    def onShowFrame(self, event):
#        self.sidebar.renderSidebarContent()

    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def exitButton(self, event):
        self.controller.destroy()

#    def volumeAnalysisButton(self, event):
#        self.controller.mode = "volume"
#        self.controller.back_history.append("AppSelectionScreen")
#        self.controller.show_frame("ReviewListScreen")
