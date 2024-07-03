import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from widgets.data_information_entry_table_frame import DataInformationEntryTableFrame
from widgets.sidebar.sidebar_crop import SidebarCrop

class DataEntryScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.image_path = "./assets/datatype-select/"
        # ========================================/

        self.configure(bg="white")

        # Load button images
        color_of_the_gradient = '#8C953C'
        sidebar_frame = tk.Frame(self)
        #sidebar_frame.configure(bg='red')
        sidebar_frame.pack(side="left", fill='y')
        #.grid(row=0, column=0,columnspan=1, rowspan=4, sticky="nsew")

        ########################### Side bar ##############################

        sidebar = SidebarCrop(sidebar_frame, self.controller).pack(side="left", fill="y" )
        #.grid(col=0, row=0, sticky="nsew")
        #img_chili.pack(side="top", fill="both", expand=True, pady=50)


        #### Load all the images in ####
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
        # Step 5 ... Label
        txt_version = tk.Label(self, text = "STEP 3. Entry NEW DATA Information")
        #txt_version.grid(row=0,column=1,columnspan=2,  padx=50, pady=25, sticky="sw")
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
        img_logo.pack(side="top", expand=True)
        #img_logo.configure(bg='purple')

        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)


        # Write text for under the LOGO
        txt_underlogo= tk.Label(logo_frame,
                                 text = "Product of SkyHarvest Insights\n" + u"\N{COPYRIGHT SIGN}" + " All rights reserved",
                                 font = ("Montserrat", 10),
                                #wraplength=140,
                                 justify="right")
        #txt_underlogo.grid(row=3,column=2,padx=5, pady=5, sticky="se")
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
        ###### ENTER THE CUSTOM FRAME HERE!!!!!!!!!!!!
        buttons_frame = DataInformationEntryTableFrame(self, self.controller)
        buttons_frame.pack(side="top", expand=True, anchor='center')



    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()
