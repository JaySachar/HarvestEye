import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from widgets.review_list_frame import ReviewListFrame
from widgets.sidebar.sidebar_crop import SidebarCrop
from widgets.logo_frame import LogoFrame

class ReviewListScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.image_path = "./assets/datatype-select/"
        # ========================================/
        self.configure(bg="white")

        ########################### Side bar ##############################
        color_of_the_gradient = '#8C953C'
        sidebar_frame = tk.Frame(self)
        sidebar_frame.pack(side="left", fill='y')

        sidebar = SidebarCrop(sidebar_frame, self.controller).pack(side="left", fill="y" )

        ###################################################################


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
        # Step 4 ... Label
        txt_version = tk.Label(self, text = "STEP 4. select data entry to start crop height analysis")
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
        image_path = "./assets/review-list/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_bottomdrone_sm.png"))
        img_graybtnbackground= tk.Label(bottom_bar_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.pack(side="bottom", fill='x')
        #img_graybtnbackground.grid(row=3,column=1, columnspan=2, padx=25, pady=20,  sticky="nwe")
        img_graybtnbackground.configure(bg='white')



    def center_frame(self):
        folder_path = "./review_saved_data/" + self.controller.crop + "/"  # Set this to the path of your folder
        # REMEMBER TO IMPLEMENT A CHECK IF THE FOLDER EXISTS
        ## -> CREATE A NEW ONE IF IT DOESN'T!!!
        review_list_frame = ReviewListFrame(self, self.controller, folder_path)
        review_list_frame.pack(side="top", fill="both", expand=True, anchor='center')


    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()
