import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from widgets.sidebar.sidebar_crop import SidebarCrop

class AppSelectionScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg='white')

        # ========================================/
        #### Load all the images in ####
        self.image_path = "./assets/app-select/"


        print(f"Right after assigning a variable crop: {self.controller.crop}")
        ########################### Side bar ##############################
        sidebar_frame = tk.Frame(self)
        sidebar_frame.configure(bg="white")
        sidebar_frame.pack(side="left", fill='y')
        sidebar = SidebarCrop(sidebar_frame, self.controller).pack(side="left", fill="y" )

        self.topPage()
        self.center_frame()
        self.bottomPage()

    def topPage(self):
        # Load the EXIT button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"btn-exit_sm.png"))
        btn_exit = tk.Label(self, image=photo )
        btn_exit.image = photo
        btn_exit.bind('<Button-1>', self.exitButton)
        btn_exit.pack(side="top", expand=False, padx=10, pady=10, anchor="ne")
        btn_exit.configure(bg='white')
        # Step 2 ... Label
        txt_version = tk.Label(self, text = "STEP 2. select the HarvestEye application")
        txt_version.pack(side="top",  anchor="w", padx=30 )
        txt_version.configure(bg='white')

    def bottomPage(self):
        #BottomBar

        bottom_bar_frame = tk.Frame(self)
        bottom_bar_frame.pack(side="left", fill='x', expand=True)
        bottom_bar_frame.configure(bg='white')

        # ------------------------------
        #Logo frame that  goes to the bottom right

        logo_frame = tk.Frame(self)
        logo_frame.pack(side="right")
        logo_frame.configure(bg='white')
        # Load the LOGO img
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"Logo_sm.png"))
        img_logo = tk.Label(logo_frame, image=photo, borderwidth=0)
        img_logo.image = photo
        #img_logo.grid(row=3,column=2,padx=5, pady=35, sticky="se")
        img_logo.pack(side="top", anchor="e", expand=True)
        #img_logo.configure(bg='purple')

        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)


        # Write text for under the LOGO
        txt_underlogo= tk.Label(logo_frame,
                                 text = "Product of SkyHarvest Insights\n" +
                                        u"\N{COPYRIGHT SIGN}" +
                                        " All rights reserved",
                                 font = ("Montserrat", 10),
                                 #wraplength=140,
                                 justify="right")
        txt_underlogo.pack(side="bottom")
        txt_underlogo.configure(bg='white')
        # ------------------------------


        # Actual bottom_bar_frame stuff
        # Write text for Version number
        txt_version = tk.Label(bottom_bar_frame, text = "Version 1.00")
        txt_version.pack(side="bottom", fill='x')
        #txt_version.grid(row=3,column=1,columnspan=2, padx=5, pady=5, sticky="s")
        txt_version.configure(bg='white')

        # Drone progress bar
        # Image of Drone Progress Bar
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_bottomdrone_sm.png"))
        img_graybtnbackground= tk.Label(bottom_bar_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.pack(side="bottom", fill='x')
        #img_graybtnbackground.grid(row=3,column=1, columnspan=2, padx=25, pady=20,  sticky="nwe")
        img_graybtnbackground.configure(bg='white')


    def center_frame(self):
        ###################################################################
        ######################## Right Side with buttons ##################

        foreground_frame = tk.Frame(self)
        foreground_frame.pack(side="top", expand=True, anchor='center')
        foreground_frame.configure(bg="white")

        # NEW DATA - GRAY background
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_background_sm.png"))
        img_graybtnbackground= tk.Label(foreground_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.grid(row=1,column=1, padx=25, sticky="se")
        img_graybtnbackground.configure(bg='white')
        # NEW DATA - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_newdata_sm.png"))
        btn_newdata= tk.Label(foreground_frame, image=photo )
        btn_newdata.image = photo
        btn_newdata.grid(row=1,column=1, padx=80, pady=20, sticky="se")
        btn_newdata.configure(bg='#D9D9D9')
        btn_newdata.bind('<Button-1>', self.dataTypeButton)


        # HEIGHT ANALYSIS - GRAY background
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_background_sm.png"))
        img_graybtnbackground= tk.Label(foreground_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.grid(row=1,column=2, padx=25, sticky="sw")
        img_graybtnbackground.configure(bg='white')
        # HEIGHT ANALYSIS - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_heightanal_sm.png"))
        btn_heightanalysis= tk.Label(foreground_frame, image=photo )
        btn_heightanalysis.image = photo
        btn_heightanalysis.grid(row=1,column=2, padx=70, pady=20, sticky="sw")
        btn_heightanalysis.configure(bg='#D9D9D9')
        btn_heightanalysis.bind('<Button-1>', self.heightAnalysisButton)

        # DRONE NAVIGATION GUIDE - GRAY background
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_backgroundlong_sm.png"))
        img_graybtnbackground= tk.Label(foreground_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.grid(row=2,column=1, columnspan=2,  pady=20,  sticky="n")
        img_graybtnbackground.configure(bg='white')
        # DRONE NAVIGATION GUIDE - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_droneflight_sm.png"))
        btn_dronenavguide= tk.Label(foreground_frame, image=photo )
        btn_dronenavguide.image = photo
        btn_dronenavguide.grid(row=2,column=1, columnspan=2, padx=70, pady=40, sticky="n")
        btn_dronenavguide.configure(bg='#D9D9D9')
        btn_dronenavguide.bind('<Button-1>', self.chiliButton)
        ###################################################################




    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def backButton(self, event):
        self.controller.show_frame("CropSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()

    def dataTypeButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def heightAnalysisButton(self, event):
        self.controller.show_frame("ReviewListScreen")
