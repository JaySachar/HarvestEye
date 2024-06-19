import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class DataInformationEntryTableFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        #self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=8)
        #self.grid_rowconfigure(2, weight=8)
        #self.grid_rowconfigure(3, weight=1)
        self.configure(bg="#D9D9D9")


        # ========================================/
        #### Load all the images in ####
        # Create a foreground frame on top of the background
        #foreground_frame = tk.Frame(self)
        #foreground_frame.configure(bg='white')
        #foreground_frame.grid(row=0, column=0, sticky="nsew")

        ## Configure grid for the foreground frame
        #foreground_frame.grid_columnconfigure(0, weight=2)
        #foreground_frame.grid_columnconfigure(1, weight=2)
        #foreground_frame.grid_columnconfigure(2, weight=2)
        #foreground_frame.grid_rowconfigure(0, weight=5)
        #foreground_frame.grid_rowconfigure(1, weight=1)

       # Table frame 
        color_of_the_gradient = '#8C953C'
        table_frame = tk.Frame(self)
        table_frame.configure(bg=color_of_the_gradient)
        #table_frame.grid(row=0, column=0,columnspan=3, rowspan=4, sticky="nsew")
        table_frame.pack(side="top", expand=True, padx=10, pady=20,  anchor="center")
        table_frame.grid_columnconfigure(0, weight = 1)
        table_frame.grid_columnconfigure(1, weight = 1)
        table_frame.grid_rowconfigure(0, weight = 1)
        table_frame.grid_rowconfigure(1, weight = 1)
        table_frame.grid_rowconfigure(2, weight = 1)
        table_frame.grid_rowconfigure(3, weight = 1)
        table_frame.grid_rowconfigure(4, weight = 1)
        table_frame.grid_rowconfigure(5, weight = 2)

        width_of_table = 50
        date_flight_label= tk.Label(table_frame,
                                 height = 2,
                                 text = "Date of flight (MM-DD-YYYY): ",
                                 bg = "green")
        date_flight_enty= tk.Text(table_frame,
                                 height = 2,
                                 width = width_of_table,
                                 bg="red")
        weather_label = tk.Label(table_frame,
                                 height = 2,
                                 text = "Weather during flight: ",
                                 bg = "green")
        weather_entry = tk.Text(table_frame,
                                 height = 2,
                                 width = width_of_table,
                                 bg="red")
        dronetype_label = tk.Label(table_frame,
                                 height = 2,
                                 text = "Drone type: ",
                                 bg = "green")
        dronetype_entry = tk.Text(table_frame,
                                 height = 2,
                                 width = width_of_table,
                                 bg="red")
        folder_label = tk.Label(table_frame,
                                 height = 2,
                                 text = "Folder of Images ONLY: ",
                                 bg = "green")
        folder_btn = tk.Button(table_frame,
                                 height = 2,
                                 text = "Select",
                                 bg = "green")


#        inputtxt.pack(side="right", fill=tk.BOTH, expand=tk.TRUE, anchor="n")
#        inputlabel.pack(side="left", expand=False,  anchor="n")
        lst = [[date_flight_label, date_flight_enty],
               [weather_label, weather_entry],
               [dronetype_label, dronetype_entry],
               [folder_label, folder_btn]]

        total_rows = len(lst)
        total_cols = len(lst[0])
        for i in range(total_rows):
            for j in range(total_cols):
                lst[i][j].grid(row= i, column = j, sticky="ew") 

        notes_entry = tk.Label(table_frame, text="Notes (500 words max): ", bg="red")
        #notes_entry.insert(0, "Notes (500 words max): ")
        notes_entry.grid(row= i+1, column = j-1, sticky="nsew") 
        notes_entry = tk.Label(table_frame, text="", bg="red")
        notes_entry.grid(row= i+1, column = j,  sticky="nsew") 

        notes_entry = tk.Text(table_frame, height = 10, bg="red")
        notes_entry.grid(row= i+2, column = j-1, columnspan=2, sticky="ew") 


        # Image Entry Button
        image_path = "./assets/datatype-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_submit_sm.png"))


       # Frame to place on top of GRAY background; packed() with images and a button
#        right_frame = tk.Frame(self)
#        right_frame.grid(row=1,column=1, rowspan=4, padx=25, sticky="nsew") # <------------
#        right_frame.configure(bg="#D9D9D9")
        # Image Entry Button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_submit_sm.png"))
        btn_imageentry= tk.Label(self, image=photo )
        btn_imageentry.image = photo
        btn_imageentry.pack(side="bottom", expand=False, padx=10, pady=20, anchor="s")
        btn_imageentry.configure(bg='#D9D9D9')

        btn_imageentry.bind('<Button-1>', self.chiliButton)

      ###################################################################


    def chiliButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()

