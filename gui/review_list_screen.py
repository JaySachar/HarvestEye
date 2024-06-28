import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# keep it for now as a placeholder for the frame you will make
#from widgets.data_information_entry_table_frame import DataInformationEntryTableFrame
from widgets.review_list_frame import ReviewListFrame

class ReviewListScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # ========================================/
        #### Load all the images in ####

        # Configure grid for the entire SplashScreen frame
        self.grid_rowconfigure(0, weight = 1 )
        self.grid_columnconfigure(0, weight = 1)

        # Create a foreground frame on top of the background
        foreground_frame = tk.Frame(self)
        foreground_frame.configure(bg='white')
        foreground_frame.grid(row=0, column=0, sticky="nsew")

        # Configure grid for the foreground frame
        foreground_frame.grid_columnconfigure(0, weight=1)
        foreground_frame.grid_columnconfigure(1, weight=2)
        foreground_frame.grid_columnconfigure(2, weight=2)
        foreground_frame.grid_rowconfigure(0, weight=1)
        foreground_frame.grid_rowconfigure(1, weight=3)
        foreground_frame.grid_rowconfigure(2, weight=3)
        foreground_frame.grid_rowconfigure(3, weight=3)

        # Load button images
        color_of_the_gradient = '#8C953C'
        gradient_frame = tk.Frame(foreground_frame)
        gradient_frame.configure(bg=color_of_the_gradient)
        gradient_frame.grid(row=0, column=0,columnspan=1, rowspan=4, sticky="nsew")

        ## Green Background
        image_path = "./assets/datatype-select/"


        ########################### Side bar ##############################
        # Load the BACK button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-back_sm.png"))
        btn_back = tk.Label(gradient_frame, image=photo )
        btn_back.image = photo
        btn_back.pack(side="top", expand=False, padx=10, pady=10, anchor="nw")
        btn_back.bind('<Button-1>', self.backButton)
        btn_back.configure(bg=color_of_the_gradient)


        # Load CHILI TEXT for the side gradient_frame
        photo = ImageTk.PhotoImage(Image.open(image_path+"txt_chili_sm.png"))
        txt_chilititle = tk.Label(gradient_frame, image=photo )
        txt_chilititle.image = photo
        txt_chilititle.pack(side="top", fill="x", expand=False, pady=50)
        txt_chilititle.configure(bg=color_of_the_gradient)
        image_path = "./assets/datatype-select/"

        # Load CHILI image for the side gradient_frame
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_chili_sm.png"))
        img_chili = tk.Label(gradient_frame, image=photo )
        img_chili.image = photo
        img_chili.pack(side="top", fill="x", expand=False, pady=50)
        img_chili.configure(bg=color_of_the_gradient)

        # Load CHILI TXT INFO for the side gradient_frame
        photo = ImageTk.PhotoImage(Image.open(image_path+"txt_info_sm.png"))
        txt_chiliinfo = tk.Label(gradient_frame, image=photo )
        txt_chiliinfo.image = photo
        txt_chiliinfo.pack(side="bottom", fill="y",  expand=True)
        txt_chiliinfo.configure(bg=color_of_the_gradient)

        ###################################################################

        # Load the EXIT button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-exit_sm.png"))
        btn_exit = tk.Label(foreground_frame, image=photo )
        btn_exit.image = photo
        #btn_exit.place(x=0, y=0, relwidth=1, relheight=1)
        btn_exit.bind('<Button-1>', self.exitButton)
        btn_exit.grid(row=0,column=2,padx=10, pady=10, sticky="ne")
        btn_exit.configure(bg='white')


###### ENTER THE CUSTOM FRAME HERE!!!!!!!!!!!!
        #buttons_frame = DataInformationEntryTableFrame(foreground_frame, self.controller)
        #buttons_frame.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, sticky="nsew")

        folder_path = "./review_saved_data/"  # Set this to the path of your folder
        review_list_frame = ReviewListFrame(foreground_frame, self.controller, folder_path)
        review_list_frame.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, sticky="nsew")

        ######################## Right Side with buttons ##################
        # Step 2 ... Label
        txt_version = tk.Label(foreground_frame, text = "STEP 4. select data entry to start crop height analysis")
        txt_version.grid(row=0,column=1,columnspan=2,  padx=50, pady=25, sticky="sw")
        txt_version.configure(bg='white')
#
        image_path_bottomdroneimg = "./assets/review-list/"

        # Image of Drone Progress Bar
        photo = ImageTk.PhotoImage(Image.open(image_path_bottomdroneimg + "img_bottomdrone_sm.png"))
        img_graybtnbackground= tk.Label(foreground_frame, image=photo )
        img_graybtnbackground.image = photo
        img_graybtnbackground.grid(row=3,column=1, columnspan=2, padx=25, pady=20,  sticky="nwe")
        img_graybtnbackground.configure(bg='white')
       


        # Load the LOGO img
        photo = ImageTk.PhotoImage(Image.open(image_path+"Logo_sm.png"))
        img_logo = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_logo.image = photo
        img_logo.grid(row=3,column=2,padx=5, pady=35, sticky="se")
        img_logo.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)


        # Write text for under the LOGO
        txt_underlogo= tk.Label(foreground_frame,
                                 text = "Product of SkyHarvest Insights",
                                 font = ("Montserrat", 10),
                                 wraplength=140,
                                 justify="right")
        txt_underlogo.grid(row=3,column=2,padx=5, pady=5, sticky="se")
        txt_underlogo.configure(bg='white')

        # Write text for Version number
        txt_version = tk.Label(foreground_frame, text = "Version 1.00")
        txt_version.grid(row=3,column=1,columnspan=2, padx=5, pady=5, sticky="s")
        txt_version.configure(bg='white')



    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()
