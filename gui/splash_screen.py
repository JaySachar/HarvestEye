import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SplashScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Reference to the MainApp() and it's __init__ variables
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


        # Load the SPLASH image
        image_path = "./assets/splash/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"splash3_downsampled.jpg"))
        background_label = tk.Label(foreground_frame, image=photo, borderwidth=0)
        background_label.image = photo
        #background_label.place(relx=0.5, rely=0.5, anchor="center")
        background_label.grid(row=1, column=1, rowspan=3, sticky="nsew")
        background_label.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Configure grid for the foreground frame
        foreground_frame.grid_columnconfigure(0, weight=1)
        foreground_frame.grid_columnconfigure(1, weight=5)
        foreground_frame.grid_columnconfigure(2, weight=1)
        foreground_frame.grid_rowconfigure(0, weight=1)
        foreground_frame.grid_rowconfigure(1, weight=1)
        foreground_frame.grid_rowconfigure(2, weight=1)
        foreground_frame.grid_rowconfigure(3, weight=1)
        foreground_frame.grid_rowconfigure(4, weight=1)

        # Load the Top Right Corner image
        photo = ImageTk.PhotoImage(Image.open(image_path+"top_right_sm.png"))
        img_corner_topright = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_corner_topright.image = photo
        img_corner_topright.place(x=0, y=0, relwidth=1, relheight=1)
        img_corner_topright.grid(row=0,column=2,rowspan=3, padx=5, pady=5, sticky="ne")
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load the Bottom Left Corner image
        photo = ImageTk.PhotoImage(Image.open(image_path+"bottom_left_sm.png"))
        img_corner_bottomleft = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_corner_bottomleft.image = photo
        img_corner_bottomleft.place(x=0, y=0, relwidth=1, relheight=1)
        img_corner_bottomleft.grid(row=2,column=0, rowspan=3, padx=5, pady=5, sticky="sw")
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load the custom OPEN button 
        photo = ImageTk.PhotoImage(Image.open(image_path+"Open button w text_sm.png"))
        btn_open = tk.Label(foreground_frame, image=photo )
        btn_open.image = photo
        #btn_open.place(x=0, y=0, relwidth=1, relheight=1)
        btn_open.bind('<Button-1>', self.openButton)
        btn_open.grid(row=4,column=1,padx=5, pady=5)
        btn_open.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load the LOGO img
        photo = ImageTk.PhotoImage(Image.open(image_path+"Logo_sm.png"))
        img_logo = tk.Label(foreground_frame, image=photo, borderwidth=0)
        img_logo.image = photo
        img_logo.grid(row=4,column=2,padx=5, pady=35, sticky="se")
        img_logo.configure(bg='white')
        # Bind the resize event to the resize_image function
        #self.bind("<Configure>", resize_image)

        # Load the EXIT button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn-exit_sm.png"))
        btn_exit = tk.Label(foreground_frame, image=photo )
        btn_exit.image = photo
        #btn_exit.place(x=0, y=0, relwidth=1, relheight=1)
        btn_exit.bind('<Button-1>', self.exitButton)
        btn_exit.grid(row=0,column=2,padx=50, pady=50, sticky="ne")
        btn_exit.configure(bg='white')
 

        # Write text for under the LOGO
        txt_underlogo= tk.Label(foreground_frame,
                                 text = "Product of SkyHarvest Insights",
                                 font = ("Montserrat", 10),
                                 wraplength=140,
                                 justify="right")
        txt_underlogo.grid(row=4,column=2,padx=5, pady=5, sticky="se")
        txt_underlogo.configure(bg='white')

        # Write text for Version number
        txt_version = tk.Label(foreground_frame, text = "Version 1.00")
        txt_version.grid(row=4,column=1,padx=5, pady=5, sticky="s")
        txt_version.configure(bg='white')



        # ========================================/
        #### Define a grid for all the elements ####


#        btn_open = tk.Button(self,
#                           text = "Open",
#                           command = lambda: controller.show_frame("CropSelectionScreen"))
#        btn_open.pack()
        # ========================================/

    def openButton(self, event):
        self.controller.show_frame("CropSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()



