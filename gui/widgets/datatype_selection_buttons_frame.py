import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
import os
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
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=8)
        self.grid_rowconfigure(3, weight=1)
        self.configure(bg="white")

        ######################## Right Side with buttons ##################
        image_path = "./assets/datatype-select/"

        left_frame = tk.Frame(self)
        left_frame.grid(row=0,column=0, rowspan=4, padx=25, sticky="ns") # <------------
        left_frame.configure(bg="#D9D9D9")
        #left_frame.configure(bg="black")
        # Video Entry Image - button
        photo = ImageTk.PhotoImage(Image.open(image_path+"img_plyentry_sm.png"))
        img_videoentry= tk.Label(left_frame, image=photo )
        img_videoentry.image = photo
        img_videoentry.pack(side="top", expand=False, padx=10, pady=50, anchor="n")
        #img_videoentry.grid(row=1,column=2, padx=70, pady=20, sticky="nw")
        img_videoentry.configure(bg='#D9D9D9')
        img_videoentry.bind('<Button-1>', self.uploadPlyButton)
        # Image Entry Button
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_submit_sm.png"))
        btn_imageentry= tk.Label(left_frame, image=photo )
        btn_imageentry.image = photo
        btn_imageentry.pack(side="bottom", expand=False, padx=10, pady=50, anchor="s")
        btn_imageentry.configure(bg='#D9D9D9')

        btn_imageentry.bind('<Button-1>', self.uploadPlyButton)

        # Frame to place on top of GRAY background; packed() with images and a button
        right_frame = tk.Frame(self)
        right_frame.grid(row=0,column=1, rowspan=4, padx=25, sticky="ns") # <------------
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

        btn_imageentry.bind('<Button-1>', self.imageEntryButton)

      ###################################################################

    def uploadPlyButton(self, event):
        #self.controller.back_history.append("DataTypeSelectionScreen")
        #self.controller.show_frame("DataEntryScreen")
        self.__create_a_file()
        self.controller.mode = "height"
        self.controller.back_history.append("DataTypeSelectionScreen")
        self.controller.show_frame("ReviewListScreen")
        print("Upload .ply")

    def __create_a_file(self):
        ## Warning for a person who implements deletion of files:
        ## Remember that review_saved_data has files named {count_number}.txt
        ## So, if you delete any of the files in a list, remember that 
        ## names of certain files will be rewritten and because of
        ## count_number being equal "{name of folder}" 
        ## 
        ## Change filenames to hash maybe? To be random.
        file_path = filedialog.askopenfilename(
            title="Open .ply File",
            filetypes=[("PLY files", "*.ply"), ("All files", "*.*")]
        )
        if file_path:
            print(f"Selected file: {file_path[0:file_path.rfind('/')]}")
            save_path = "./review_saved_data/" + self.controller.crop + "/" 
            count_number_of_files = len(os.listdir(save_path))
            filename_and_path = save_path + str(count_number_of_files + 1)+ '.txt'
            #filename = "./review_saved_data/" + self.controller.crop + "/"  \
            #        + datetime.today().strftime('%d-%m-%Y') + ".txt"

            with open(filename_and_path, 'w') as file:
                file.write(datetime.today().strftime('%m-%d-%Y')  + "\n")
                file.write("Unknown" + "\n")
                file.write("Unknown" + "\n")
                file.write(file_path[0:file_path.rfind('/')] + "\n")
                file.write("Unknown" + "\n")
        else:
            print("No file selected")


    def imageEntryButton(self, event):
        self.controller.back_history.append("DataTypeSelectionScreen")
        self.controller.show_frame("DataEntryScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataEntryScreen")

    def exitButton(self, event):
        self.controller.destroy()

