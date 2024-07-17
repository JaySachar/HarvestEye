import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from widgets.sidebar.sidebar_crop import SidebarCrop
from widgets.logo_frame import LogoFrame

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

        self.sidebar = SidebarCrop(sidebar_frame, self.controller)
        self.sidebar.pack(side="left", fill="y" )

        self.topPage()
        self.center_frame()
        self.bottomPage()

        self.bind("<<ShowFrame>>", self.onShowFrame)

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
        logo_frame = LogoFrame(self)
        logo_frame.pack(side="right", anchor="s")

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

        top_buttons_frame = tk.Frame(foreground_frame)
        top_buttons_frame.pack(side="top", fill="both", expand=True, pady=20)
        top_buttons_frame.configure(bg="white")
       # NEW DATA - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_newdata_sm.png"))
        btn_newdata= tk.Label(top_buttons_frame, image=photo )
        btn_newdata.image = photo
        btn_newdata.pack(side="left", fill="x", expand=True)
        #btn_newdata.grid(row=1,column=1, padx=80, pady=20, sticky="se")
        btn_newdata.configure(bg='white')
        btn_newdata.bind('<Button-1>', self.dataTypeButton)

       # HEIGHT ANALYSIS - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_heightanal_sm.png"))
        btn_heightanalysis= tk.Label(top_buttons_frame, image=photo )
        btn_heightanalysis.image = photo
        btn_heightanalysis.pack(side="left", fill="x", expand=True)
        #btn_heightanalysis.pack(side="left", expand=True, anchor='n')
        #btn_heightanalysis.grid(row=1,column=2, padx=70, pady=20, sticky="sw")
        btn_heightanalysis.configure(bg='white')
        btn_heightanalysis.bind('<Button-1>', self.heightAnalysisButton)

       # VOLUME ANALYSIS - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_volumeanal_sm.png"))
        btn_volumeanalysis= tk.Label(top_buttons_frame, image=photo )
        btn_volumeanalysis.image = photo
        btn_volumeanalysis.pack(side="left", fill="x", expand=True)
        #btn_volumeanalysis.pack(side="left", expand=True, anchor='ne')
        #btn_volumeanalysis.grid(row=1,column=2, padx=70, pady=20, sticky="sw")
        btn_volumeanalysis.configure(bg='white')
        btn_volumeanalysis.bind('<Button-1>', self.volumeAnalysisButton)



       # DRONE NAVIGATION GUIDE - button
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"img_droneflight_sm.png"))
        btn_dronenavguide= tk.Label(foreground_frame, image=photo )
        btn_dronenavguide.image = photo
        btn_dronenavguide.pack(side="bottom", expand=True, anchor='center')
        #btn_dronenavguide.grid(row=2,column=1, columnspan=2, padx=70, pady=40, sticky="n")
        btn_dronenavguide.configure(bg='white')
        btn_dronenavguide.bind('<Button-1>', self.chiliButton)
        ###################################################################

    def onShowFrame(self, event):
        self.sidebar.renderSidebarContent()

    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def exitButton(self, event):
        self.controller.destroy()

    def dataTypeButton(self, event):
        self.controller.back_history.append("AppSelectionScreen")
        self.controller.show_frame("DataTypeSelectionScreen")

    def heightAnalysisButton(self, event):
        self.controller.back_history.append("AppSelectionScreen")
        self.controller.show_frame("ReviewListScreen")
        self.controller.mode = "height"
    def volumeAnalysisButton(self, event):
        self.controller.mode = "volume"
        self.controller.back_history.append("AppSelectionScreen")
        self.controller.show_frame("ReviewListScreen")
