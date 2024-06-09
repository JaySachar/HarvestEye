import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class CropSelectionScreen(tk.Frame):

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
        foreground_frame.grid_columnconfigure(1, weight=1)
        foreground_frame.grid_columnconfigure(2, weight=1)
        foreground_frame.grid_rowconfigure(0, weight=1)
        foreground_frame.grid_rowconfigure(1, weight=1)
        foreground_frame.grid_rowconfigure(2, weight=1)
        foreground_frame.grid_rowconfigure(3, weight=5)
        foreground_frame.grid_rowconfigure(4, weight=2)
        foreground_frame.grid_rowconfigure(5, weight=1)

        button_frame = tk.Frame(foreground_frame)
        button_frame.configure(bg='white')
        button_frame.grid(row=3, column=1, sticky="nsew")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)

        # Load button images
        # Button background rounded square
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"background-btn_sm.png"))
        background_for_buttons = tk.Label(button_frame, image=photo, borderwidth=0)
        background_for_buttons.image = photo
        #background_for_buttons.place(relx=0.5, rely=0.5, anchor="center")
        background_for_buttons.grid(row=0, column=0, columnspan=2, rowspan=2, sticky="nsew")
        background_for_buttons.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Chili button
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-chili-text_sm.png"))
        btn_chili = tk.Label(button_frame, image=photo, borderwidth=0)
        btn_chili.image = photo
        #btn_chili.place(relx=0.5, rely=0.5, anchor="center")
        btn_chili.bind('<Button-1>', self.chiliButton)
        btn_chili.grid(row=0, column=0, sticky="nsew")
        btn_chili.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load button images
        # Orange button
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-orange-text_sm.png"))
        btn_orange = tk.Label(button_frame, image=photo, borderwidth=0)
        btn_orange.image = photo
        #btn_orange.place(relx=0.5, rely=0.5, anchor="center")
        btn_orange.bind('<Button-1>', self.orangeButton)
        btn_orange.grid(row=0, column=1, sticky="nsew")
        btn_orange.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load button images
        # Avocado button
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-avocado-text_sm.png"))
        btn_avocado = tk.Label(button_frame, image=photo, borderwidth=0)
        btn_avocado.image = photo
        #btn_avocado.place(relx=0.5, rely=0.5, anchor="center")
        btn_avocado.bind('<Button-1>', self.avocadoButton)
        btn_avocado.grid(row=1, column=0,  sticky="nsew")
        btn_avocado.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load button images
        # Add/More button
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-more-text_sm.png"))
        btn_more = tk.Label(button_frame, image=photo, borderwidth=0)
        btn_more.image = photo
        #btn_more.place(relx=0.5, rely=0.5, anchor="center")
        btn_more.bind('<Button-1>', self.moreButton)
        btn_more.grid(row=1, column=1, sticky="nsew")
        btn_more.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load the EXIT button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-exit_sm.png"))
        btn_exit = tk.Label(foreground_frame, image=photo )
        btn_exit.image = photo
        #btn_exit.place(x=0, y=0, relwidth=1, relheight=1)
        btn_exit.bind('<Button-1>', self.exitButton)
        btn_exit.grid(row=0,column=2,padx=10, pady=10, sticky="ne")
        btn_exit.configure(bg='white')

        # Load the BACK button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-back_sm.png"))
        btn_back = tk.Label(foreground_frame, image=photo )
        btn_back.image = photo
        #btn_back.place(x=0, y=0, relwidth=1, relheight=1)
        btn_back.bind('<Button-1>', self.backButton)
        btn_back.grid(row=0,column=0,padx=10, pady=10, sticky="nw")
        btn_back.configure(bg='white')
 

        # Title
        txt_title= tk.Label(foreground_frame,
                                 text = "Crop Dashboard",
                                 font = ("Montserrat", 22, "bold"),
                                 justify="center")
        txt_title.grid(row=0,column=1,padx=5, pady=50, sticky="nsew")
        txt_title.configure(bg='white')


        # Step 1 ... Label
        txt_version = tk.Label(foreground_frame, text = "STEP 1. select the crop you plan to analyze today")
        txt_version.grid(row=2,column=0,columnspan=2, padx=5, pady=5, sticky="w")
        txt_version.configure(bg='white')

        # Left side image of progress visual
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"load-left_sm.png"))
        img_left_progress = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_left_progress.image = photo
        #img_left_progress.place(relx=0.5, rely=0.5, anchor="center")
        img_left_progress.grid(row=3, column=0, sticky="ew")
        img_left_progress.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Left side image of progress visual
        image_path = "./assets/crop-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"load-right_sm.png"))
        img_right_progress = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_right_progress.image = photo
        #img_right_progress.place(relx=0.5, rely=0.5, anchor="center")
        img_right_progress.grid(row=3, column=2, sticky="ew")
        img_right_progress.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load the LOGO img
        photo = ImageTk.PhotoImage(Image.open(image_path+"Logo_sm.png"))
        img_logo = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_logo.image = photo
        img_logo.grid(row=5,column=2,padx=5, pady=35, sticky="se")
        img_logo.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)


        # Write text for under the LOGO
        txt_underlogo= tk.Label(foreground_frame,
                                 text = "Product of SkyHarvest Insights",
                                 font = ("Montserrat", 10),
                                 wraplength=140,
                                 justify="right")
        txt_underlogo.grid(row=5,column=2,padx=5, pady=5, sticky="se")
        txt_underlogo.configure(bg='white')

        # Write text for Version number
        txt_version = tk.Label(foreground_frame, text = "Version 1.00")
        txt_version.grid(row=5,column=1,padx=5, pady=5, sticky="s")
        txt_version.configure(bg='white')




        label = tk.Label(self, 
                         text = "This is crop selection screen",
                         font = controller.title_font)
        button = tk.Button(self,
                           text = "Go to SplashScreen",
                           command = lambda: controller.show_frame("SplashScreen"))

    def chiliButton(self, event):
        self.controller.show_frame("AppSelectionScreen")

    def orangeButton(self, event):
        self.controller.show_frame("AppSelectScreen")
    
    def avocadoButton(self, event):
        self.controller.show_frame("AppSelectScreen")

    def moreButton(self, event):
        self.controller.show_frame("AppSelectScreen")

    
    
    
    def backButton(self, event):
        self.controller.show_frame("SplashScreen")

    def exitButton(self, event):
        self.controller.destroy()
