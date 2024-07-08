import os
import tkinter as tk
from tkinter import ttk
from datetime import datetime

class ReviewListFrame(tk.Frame):
    def __init__(self, parent, controller, folder_path):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.folder_path = folder_path

        self.frame = ttk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.frame)
        self.canvas.configure(bg="white")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.configure(bg="#FFFFFF")
        self.scrollable_frame.bind(
                "<Configure>",
                self.on_frame_configure
        )
 
 
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.on_canvas_resized)
        self.update_list()
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame,
                                  anchor="nw")
 

    def on_canvas_resized(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
        self.scrollable_frame.config(width=canvas_width)

        
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        # Run the update scroll after all the elements loaded in
        self.after(100, self.update_scroll_region)


    def update_scroll_region(self):
        # Adjust the scrollregion dynamically
        content_height = self.scrollable_frame.winfo_height() 
        canvas_height = self.canvas.winfo_height()
        if content_height < canvas_height:
            #print(f" self.scrollable_frame.winfo_height()  + self.canvas.winfo_height() ")
            #print(f"{self.scrollable_frame.winfo_height()}  + {self.canvas.winfo_height()} ")
            #print("Adjusting scrollable_frame dynamically")
            self.canvas.configure(scrollregion=(0, 0, self.canvas.winfo_width(), canvas_height))
            #print(f"0, 0, {self.canvas.winfo_width()}, {canvas_height}")
        else:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))



    def update_list(self, *args):
        # Clear previous contents
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Get list of files
        files = os.listdir(self.folder_path)
        if not files:
            no_data_label = ttk.Label(self.scrollable_frame, text="No Data Found")
            no_data_label.pack(fill="x", pady=10)
        else:
            for file in files:
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    self.add_file_row(file_date)

    def add_file_row(self, file_date):
        frame = tk.Frame(self.scrollable_frame, bg="#EFEFEF")

        date_label = ttk.Label(frame, text=file_date)
        date_label.pack(side=tk.LEFT, padx=10)

        review_button = ttk.Button(frame, text="Review", command=lambda: self.review_file(file_date))
        review_button.pack(side=tk.RIGHT, padx=10)

        frame.pack(fill='x', expand=True, pady=5)

    def review_file(self, file_date):
        print(f"Reviewing file from date: {file_date}")
        # UPDATE WHEN I KNOW IT WILL LEAD TO THE FINAL REVIEW SCREEN
        #self.controller.back_history.append("DataEntryScreen")
        #self.update_list()


