import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk

class DataInformationEntryTableFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.file_path = ""

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
        self.date_flight_entry= tk.Text(table_frame,
                                 height = 1,
                                 width = width_of_table,
                                 bg="white")
        weather_label = tk.Label(table_frame,
                                 height = 1,
                                 text = "Weather during flight: ",
                                 bg = "white")
        self.weather_entry = tk.Text(table_frame,
                                 height = 1,
                                 width = width_of_table,
                                 bg="white")
        dronetype_label = tk.Label(table_frame,
                                 height = 1,
                                 text = "Drone type: ",
                                 bg = "white")
        self.dronetype_entry = tk.Text(table_frame,
                                 height = 1,
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
       # folder_btn = tk.Button(table_frame,
       #                          height = 2,
       #                          text = "Select",
       #                          bg = "white")


#        inputtxt.pack(side="right", fill=tk.BOTH, expand=tk.TRUE, anchor="n")
#        inputlabel.pack(side="left", expand=False,  anchor="n")
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
        # Need to improve the code to handle same filenames,
        # in case there are 2 readings or more on the same day
        self.date_flight_entry.get("1.0", 'end-1c')
        self.weather_entry.get("1.0", 'end-1c')
        self.dronetype_entry.get("1.0", 'end-1c')
        # File path skipped to have a check if empty
        self.notes_entry.get("1.0", 'end-1c')
        
        try:
            filename = "./review_saved_data/" + self.date_flight_entry.get("1.0", 'end-1c') + ".txt"
            if self.date_flight_entry.get("1.0", 'end-1c') == "":
                messagebox.showerror("Select a Date", "Please select a Date of Flight to proceed.")
            elif self.file_path == "":
                messagebox.showerror("Select a File", "Please select a correct folder with drone images to proceed.")
            else:
                with open(filename, 'w') as file:
                    file.write(self.date_flight_entry.get("1.0", 'end-1c') + "\n")
                    file.write(self.weather_entry.get("1.0", 'end-1c') + "\n")
                    file.write(self.dronetype_entry.get("1.0", 'end-1c') + "\n")
                    file.write(self.file_path + "\n")
                    file.write(self.notes_entry.get("1.0", 'end-1c') + "\n")
     
        except NameError:
            messagebox.showerror("Select a File", "Please select a file to proceed.")


        filename = "./review_saved_data/" + self.date_flight_entry.get("1.0", 'end-1c')
        with open(filename, 'w') as file:
            file.write(self.date_flight_entry.get("1.0", 'end-1c') + "\n")
            file.write(self.weather_entry.get("1.0", 'end-1c') + "\n")
            file.write(self.dronetype_entry.get("1.0", 'end-1c') + "\n")
            file.write(self.file_path + "\n")
            file.write(self.notes_entry.get("1.0", 'end-1c') + "\n")

        print("Successfuly added a file!")
        #self.controller.show_frame("DataTypeSelectionScreen")
    
    def backButton(self, event):
        self.controller.show_frame("DataTypeSelectionScreen")

    def exitButton(self, event):
        self.controller.destroy()

