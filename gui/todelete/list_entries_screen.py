import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from widgets.data_information_entry_table_frame import DataInformationEntryTableFrame

class ListEntriesScreen(tk.Frame):

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
        #photo = ImageTk.PhotoImage(Image.open(image_path+"img_gradient_sm.png"))
        #img_greengradient = tk.Label(foreground_frame, image=photo, borderwidth=0)
        #img_greengradient.image = photo
        ##img_greengradient.place(relx=0.5, rely=0.5, anchor="center")
        #img_greengradient.grid(row=0, column=0, sticky="nsew")
        #img_greengradient.configure(bg='white')



#        # Chili button
#        image_path = "./assets/crop-select/"
#        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-chili-text_sm.png"))
#        btn_chili = tk.Label(foreground_frame, image=photo, borderwidth=0)
#        btn_chili.image = photo
#        #btn_chili.place(relx=0.5, rely=0.5, anchor="center")
#        btn_chili.bind('<Button-1>', self.chiliButton)
#        btn_chili.grid(row=0, column=0, sticky="nsew")
#        btn_chili.configure(bg='white')
#        # Bind the resize event to the resize_image function
#        #self.bind("<Configure>", resize_image)


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
        buttons_frame = DataInformationEntryTableFrame(foreground_frame, self.controller)
        buttons_frame.grid(row = 1, column = 1, columnspan = 2, rowspan = 2, sticky="nsew")
        ######################## Right Side with buttons ##################
        # Step 2 ... Label
        txt_version = tk.Label(foreground_frame, text = "STEP 3. Entry NEW DATA Information")
        txt_version.grid(row=0,column=1,columnspan=2,  padx=50, pady=25, sticky="sw")
        txt_version.configure(bg='white')
#
#        # NEW DATA - GRAY background
#        photo = ImageTk.PhotoImage(Image.open(image_path+"img_background_sm.png"))
#        img_graybtnbackground= tk.Label(foreground_frame, image=photo )
#        img_graybtnbackground.image = photo
#        img_graybtnbackground.grid(row=1,column=1, padx=25, sticky="se")
#        img_graybtnbackground.configure(bg='white')
#        # NEW DATA - button
#        photo = ImageTk.PhotoImage(Image.open(image_path+"img_imageentry_sm.png"))
#        btn_newdata= tk.Label(foreground_frame, image=photo )
#        btn_newdata.image = photo
#        btn_newdata.grid(row=1,column=1, padx=80, pady=20, sticky="ne")
#        btn_newdata.configure(bg='#D9D9D9')
#        btn_newdata.bind('<Button-1>', self.chiliButton)
#
#
#        # HEIGHT ANALYSIS - GRAY background
#        photo = ImageTk.PhotoImage(Image.open(image_path+"img_background_sm.png"))
#        img_graybtnbackground= tk.Label(foreground_frame, image=photo )
#        img_graybtnbackground.image = photo
#        img_graybtnbackground.grid(row=1,column=2, padx=25, sticky="sw")
#        img_graybtnbackground.configure(bg='white')
#        # HEIGHT ANALYSIS - button
#        photo = ImageTk.PhotoImage(Image.open(image_path+"img_videoentry_sm.png"))
#        btn_heightanalysis= tk.Label(foreground_frame, image=photo )
#        btn_heightanalysis.image = photo
#        btn_heightanalysis.grid(row=1,column=2, padx=70, pady=20, sticky="nw")
#        btn_heightanalysis.configure(bg='#D9D9D9')
#        btn_heightanalysis.bind('<Button-1>', self.chiliButton)
#       ###################################################################

        # Image of Drone Progress Bar
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_bottomdrone_sm.png"))
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
                                 text = "Product of SkyHarvest Insights\n" + u"\N{COPYRIGHT SIGN}" + " All rights reserved",
                                 font = ("Montserrat", 10),
                                 #wraplength=140,
                                 justify="right")
        txt_underlogo.grid(row=3,column=2,padx=5, pady=5, sticky="se")
        txt_underlogo.configure(bg='white')

        # Write text for Version number
        txt_version = tk.Label(foreground_frame, text = "Version 1.00")
        txt_version.grid(row=3,column=1,columnspan=2, padx=5, pady=5, sticky="s")
        txt_version.configure(bg='white')




        label = tk.Label(self, 
                         text = "This is crop selection screen",
                         font = controller.title_font)
        button = tk.Button(self,
                           text = "Go to SplashScreen",
                           command = lambda: controller.show_frame("SplashScreen"))

    def chiliButton(self, event):
        self.controller.show_frame("SplashScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()
