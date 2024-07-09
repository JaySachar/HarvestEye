import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DataTypeSelectionButtonsFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # ========================================/
        #### Load all the images in ####

        # Configure grid for the entire SplashScreen frame
        self.grid_rowconfigure(0, weight = 1 )
        self.grid_columnconfigure(0, weight = 1)

        # Create a foreground frame on top of the background
        #foreground_frame = tk.Frame(self)
        #foreground_frame.configure(bg='white')
        #foreground_frame.grid(row=0, column=0, sticky="nsew")

        ## Configure grid for the foreground frame
        #foreground_frame.grid_columnconfigure(0, weight=1)
        #foreground_frame.grid_columnconfigure(1, weight=2)
        #foreground_frame.grid_columnconfigure(2, weight=2)
        #foreground_frame.grid_rowconfigure(0, weight=1)
        #foreground_frame.grid_rowconfigure(1, weight=3)
        #foreground_frame.grid_rowconfigure(2, weight=3)
        #foreground_frame.grid_rowconfigure(3, weight=3)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=8)
        self.grid_rowconfigure(3, weight=1)
        self.configure(bg="white")

        # Placed in .grid() on top of gray background (check BELOW img_graybtnbackground)
        #left_frame = tk.Frame(self)
        #right_frame = tk.Frame(self)
        #right_frame.pack(side="right", expand=False, padx=10, pady=10, anchor="w")
        #img_greengradient.place(relx=0.5, rely=0.5, anchor="center")

        ######################## Right Side with buttons ##################
        image_path = "./assets/datatype-select/"

        # Video Entry - GRAY background
        #photo = ImageTk.PhotoImage(Image.open(image_path+"img_background_sm.png"))
        #img_graybtnbackground= tk.Label(self, image=photo )
        #img_graybtnbackground.image = photo
        #img_graybtnbackground.grid(row=0,column=0, rowspan=2, padx=25, sticky="sw")
        #img_graybtnbackground.pack(side="top", expand=False, padx=10, pady=10, anchor="n")
        #img_graybtnbackground.configure(bg='white')
        left_frame = tk.Frame(self)
        left_frame.grid(row=0,column=0, rowspan=4, padx=25, sticky="ns") # <------------
        left_frame.configure(bg="#D9D9D9")
        #left_frame.configure(bg="black")
        # Video Entry Image - button
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_videoentry_sm.png"))
        img_videoentry= tk.Label(left_frame, image=photo )
        img_videoentry.image = photo
        img_videoentry.pack(side="top", expand=False, padx=10, pady=50, anchor="n")
        #img_videoentry.grid(row=1,column=2, padx=70, pady=20, sticky="nw")
        img_videoentry.configure(bg='#D9D9D9')
        img_videoentry.bind('<Button-1>', self.chiliButton)
        # Image Entry Button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_submit_sm.png"))
        btn_imageentry= tk.Label(left_frame, image=photo )
        btn_imageentry.image = photo
        btn_imageentry.pack(side="bottom", expand=False, padx=10, pady=50, anchor="s")
        btn_imageentry.configure(bg='#D9D9D9')

        btn_imageentry.bind('<Button-1>', self.chiliButton)


        # Image Entry - GRAY background
        #photo = ImageTk.PhotoImage(Image.open(image_path+"img_background_sm.png"))
        #img_graybtnbackground= tk.Label(self, image=photo )
        #img_graybtnbackground.image = photo
        #img_graybtnbackground.grid(row=0,column=1, rowspan=4, padx=25, sticky="ns")
        #img_graybtnbackground.configure(bg='white')
        # Frame to place on top of GRAY background; packed() with images and a button
        right_frame = tk.Frame(self)
        right_frame.grid(row=1,column=1, rowspan=4, padx=25, sticky="ns") # <------------
        right_frame.configure(bg="#D9D9D9")
        # Image Entry Image
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_imageentry_sm.png"))
        img_imageentry= tk.Label(right_frame, image=photo )
        img_imageentry.image = photo
        img_imageentry.pack(side="top", expand=False, padx=10, pady=50, anchor="n")
        img_imageentry.configure(bg='#D9D9D9')
        # Image Entry Button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_submit_sm.png"))
        btn_imageentry= tk.Label(right_frame, image=photo )
        btn_imageentry.image = photo
        btn_imageentry.pack(side="bottom", expand=False, padx=10, pady=50, anchor="s")
        btn_imageentry.configure(bg='#D9D9D9')

        btn_imageentry.bind('<Button-1>', self.chiliButton)

      ###################################################################


    def chiliButton(self, event):
        self.controller.back_history.append("DataTypeSelectionScreen")
        self.controller.show_frame("DataEntryScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataEntryScreen")

    def exitButton(self, event):
        self.controller.destroy()

