import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

class FinalReviewTableFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.file_path = ""
        # Table background color
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
        image_path = "./assets/final-review/"

        # Date of flight
        date_of_flight = tk.Label(table_frame,
                                  height = 1,
                                  text = "Date of flight (MM-DD-YYYY): ",
                                  bg = "white")

        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_review_sm.png"))
        date_of_flight_btn= tk.Label(table_frame,
                                     image=photo,
                                     bg="white")
        date_of_flight_btn.bind('<Button-1>', self.openfile)
        date_of_flight_btn.image = photo

        # Height & Location CSV
        height_and_location = tk.Label(table_frame,
                                       height = 1,
                                       text = "Height & Location (XYZ) CSV: ",
                                       bg = "white")

        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_review_sm.png"))
        height_and_location_btn= tk.Label(table_frame,
                                          image=photo,
                                          bg="white")
        height_and_location_btn.bind('<Button-1>', self.openfile)
        height_and_location_btn.image = photo

        # Volume & Location (XYZ) CSV
        volume_and_location = tk.Label(table_frame,
                                       height = 1,
                                       text = "Volume & Location (XYZ) CSV: ",
                                       bg = "white")

        photo = ImageTk.PhotoImage(Image.open(image_path+"btn_review_sm.png"))
        volume_and_location_btn= tk.Label(table_frame,
                                          image=photo,
                                          bg="white")
        volume_and_location_btn.bind('<Button-1>', self.openfile)
        volume_and_location_btn.image = photo




        # Go over ALL elements to fill the grid
        lst = [
                [date_of_flight, date_of_flight_btn],
                [height_and_location, height_and_location_btn],
                [volume_and_location, volume_and_location_btn],

               ]

        total_rows = len(lst)
        total_cols = len(lst[0])
        for i in range(total_rows):
            for j in range(total_cols):
                lst[i][j].grid(row= i, column = j, sticky="ew", pady=5) 

        notes_entry_frame= tk.Frame(table_frame)
        notes_entry_frame.configure(bg='#D9D9D9')
        notes_entry_frame.grid(row= i+1, column = j-1, columnspan=3, rowspan = 2, pady=5, sticky="nsew") 

        notes_entry = tk.Label(notes_entry_frame, text="Notes (500 words max): ", bg="white")
        #notes_entry.insert(0, "Notes (500 words max): ")
        notes_entry.pack(side="top", expand=True, anchor="w")

        #notes_entry.grid(row= i+1, column = j-1, sticky="nsew") 
        #notes_entry = tk.Label(notes_entry_frame, text="", bg="white")
        #notes_entry.pack(side="right", expand=False, anchor="s")
        #notes_entry.grid(row= i+1, column = j,  sticky="nsew") 

        self.notes_entry = tk.Text(notes_entry_frame, height = 10, bg="white")
        #notes_entry.grid(row= i+2, column = j-1, columnspan=2, sticky="ew") 
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
        print("Submit button is pressed! You can uncomment the code!!")
        # Need to improve the code to handle same filenames,
        # in case there are 2 readings or more on the same day
#        self.date_flight_entry.get("1.0", 'end-1c')
#        self.weather_entry.get("1.0", 'end-1c')
#        self.dronetype_entry.get("1.0", 'end-1c')
#        # File path skipped to have a check if empty
#        self.notes_entry.get("1.0", 'end-1c')
#        
#        try:
#            filename = "./review_saved_data/" + self.date_flight_entry.get("1.0", 'end-1c') + ".txt"
#            if self.date_flight_entry.get("1.0", 'end-1c') == "":
#                messagebox.showerror("Select a Date", "Please select a Date of Flight to proceed.")
#            elif self.file_path == "":
#                messagebox.showerror("Select a File", "Please select a correct folder with drone images to proceed.")
#            else:
#                with open(filename, 'w') as file:
#                    file.write(self.date_flight_entry.get("1.0", 'end-1c') + "\n")
#                    file.write(self.weather_entry.get("1.0", 'end-1c') + "\n")
#                    file.write(self.dronetype_entry.get("1.0", 'end-1c') + "\n")
#                    file.write(self.file_path + "\n")
#                    file.write(self.notes_entry.get("1.0", 'end-1c') + "\n")
#     
#        except NameError:
#            messagebox.showerror("Select a File", "Please select a file to proceed.")
#
#
#        filename = "./review_saved_data/" + self.date_flight_entry.get("1.0", 'end-1c')
#        with open(filename, 'w') as file:
#            file.write(self.date_flight_entry.get("1.0", 'end-1c') + "\n")
#            file.write(self.weather_entry.get("1.0", 'end-1c') + "\n")
#            file.write(self.dronetype_entry.get("1.0", 'end-1c') + "\n")
#            file.write(self.file_path + "\n")
#            file.write(self.notes_entry.get("1.0", 'end-1c') + "\n")
#
#        print("Successfuly added a file!")
#        #self.controller.show_frame("DataTypeSelectionScreen")
    
    def backButton(self, event):
        self.controller.show_frame("SplashScreen")

    def exitButton(self, event):
        self.controller.destroy()

