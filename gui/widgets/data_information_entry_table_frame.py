import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
import re
from PIL import Image, ImageTk
import os
import sys
import time
import threading
# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate one folder up
parent_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))

# Navigate to the 'main' folder
target_dir = os.path.join(parent_dir, 'main')

# Add the 'main' folder to the Python path
sys.path.append(target_dir)

# Now you can import the target file
from classesCHANGE import PointCloudGenerator

class DataInformationEntryTableFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.file_path = ""

        self.configure(bg="#D9D9D9")

       # Table frame 
        color_of_the_gradient = '#8C953C'
        table_frame = tk.Frame(self)
        table_frame.configure(bg='#D9D9D9')
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
                                 height = 1,
                                 text = "Date of flight (MM-DD-YYYY): ",
                                 bg = "white")
        self.date_flight_entry= tk.Entry(table_frame,
                                 #height = 1,
                                 width = width_of_table,
                                 bg="white")
        weather_label = tk.Label(table_frame,
                                 height = 1,
                                 text = "Weather during flight: ",
                                 bg = "white")
        self.weather_entry = tk.Entry(table_frame,
                                 #height = 1,
                                 width = width_of_table,
                                 bg="white")
        dronetype_label = tk.Label(table_frame,
                                 height = 1,
                                 text = "Drone type: ",
                                 bg = "white")
        self.dronetype_entry = tk.Entry(table_frame,
                                 #height = 1,
                                 width = width_of_table,
                                 bg="white")
        folder_label = tk.Label(table_frame,
                                 height = 1,
                                 text = "Folder of Images ONLY: ",
                                 bg = "white")

        image_path = "./assets/data-entry/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_select_sm.png"))
        folder_btn= tk.Label(table_frame,
                             image=photo,
                             bg="white")
        folder_btn.bind('<Button-1>', self.openfile)
        folder_btn.image = photo



        lst = [[date_flight_label, self.date_flight_entry],
               [weather_label, self.weather_entry],
               [dronetype_label, self.dronetype_entry],
               [folder_label, folder_btn]]

        total_rows = len(lst)
        total_cols = len(lst[0])
        for i in range(total_rows):
            for j in range(total_cols):
                lst[i][j].grid(row= i, column = j, sticky="ew", pady=5) 

        notes_entry_frame= tk.Frame(table_frame)
        notes_entry_frame.configure(bg='#D9D9D9')
        notes_entry_frame.grid(row= i+1, column = j-1, columnspan=3, rowspan = 2, pady=5, sticky="nsew") 

        notes_entry = tk.Label(notes_entry_frame, text="Notes (500 words max): ", bg="white")
        notes_entry.pack(side="top", expand=True, anchor="w")

        self.notes_entry = tk.Text(notes_entry_frame, height = 10, bg="white")
        self.notes_entry.pack(side="bottom", expand=True, fill="x", anchor="w")


        # Image Entry Button
        image_path = "./assets/datatype-select/"
        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_submit_sm.png"))
        btn_imageentry= tk.Label(self, image=photo )
        btn_imageentry.image = photo
        btn_imageentry.pack(side="bottom", expand=False, padx=10, pady=20, anchor="s")
        btn_imageentry.configure(bg='#D9D9D9')

        btn_imageentry.bind('<Button-1>', self.submitButton)

      ###################################################################
    def openfile(self, event):
        # file_path = filedialog.askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        # The line above is a reference to add specific filetypes for selections
        self.file_path = filedialog.askdirectory()
        print("Selected file: ", self.file_path)

    def submitButton(self, event):

        def date_is_valid(date_to_validate):
            pattern = re.compile(r'^(?:(?:(?:0[13578]|1[02])-(?:0[1-9]|[12][0-9]|3[01])|(?:0[469]|11)-(?:0[1-9]|[12][0-9]|30)|02-(?:0[1-9]|1[0-9]|2[0-8]))-\d{4}|02-29-(?:\d{2}(?:0[48]|[2468][048]|[13579][26])|(?:[02468][048]00|[13579][26]00)))$')
            if pattern.match(date_to_validate):
                return True
            else:
                return False


        ## Validate Date Format
        save_path = "./review_saved_data/" + self.controller.crop + "/" 
        date_flight = self.date_flight_entry.get()
        if date_flight == "":
            messagebox.showerror("Select a Date", "Please select a Date of Flight to proceed.")
            return
        elif date_is_valid(date_flight):
            count_number_of_files = len(os.listdir(save_path))
            filename_and_path = save_path + str(count_number_of_files + 1)+ '.txt'
        else:
            messagebox.showerror("Wrong Date Format", "Please make sure to enter a correct date format: MM-DD-YYYY.")
            return

        ## Create a file
        try:
            if self.file_path == "":
                messagebox.showerror("Select a File", "Please select a correct folder with drone images to proceed.")
            else:
                with open(filename_and_path, 'w') as file:
                    file.write(self.date_flight_entry.get() + "\n")
                    file.write(self.weather_entry.get() + "\n")
                    file.write(self.dronetype_entry.get() + "\n")
                    file.write(self.file_path + "\n")
                    file.write(self.notes_entry.get("1.0", 'end-1c') + "\n")
 
                               
                # This is where LOADING SCREEN GOES!!!
                # Run PointCloudGeneration
                self.controller.show_frame("LoadingScreen")
                print(self.file_path)
                print("Point Cloud Generation in progress!")
                generated_pcd = PointCloudGenerator(self.file_path)

                def run_thread():
                    #time.sleep(5)  # Simulate a long-running task
                    generated_pcd.generatePointCloud()
                    self.controller.after(0, lambda: self.controller.show_frame("ReviewListScreen"))


                thread = threading.Thread(target=run_thread)
                thread.start()
                print("Point Cloud Generation complete!!!!!!!!!!!")

                # Clear current table upon submission
                self.date_flight_entry.delete(0, tk.END)
                self.weather_entry.delete(0, tk.END)
                self.dronetype_entry.delete(0, tk.END)
                self.file_path = ""
                self.notes_entry.delete('1.0', 'end-1c')



                ## Add current page into back button history and show another frame
                self.controller.back_history.append("DataEntryScreen")
                #self.controller.show_frame("ReviewListScreen")
                print("Successfuly added a file!")
             
        except NameError:
            messagebox.showerror("Select a File", "Please select a file to proceed.")


   
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()

