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
        self.canvas.configure(bg="blue")
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.configure(bg="#D9D9D9")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        print(self.canvas.winfo_width())
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame,
                                  anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        ###########
        self.scrollbar.pack(side="right", fill="y")

        self.canvas.bind("<Configure>", self.on_canvas_resized)
        self.update_list()
        #self.add_labels()

    def add_labels(self):
        # Add some content to the scrollable frame for demonstration
        for i in range(50):
            tk.Label(self.scrollable_frame, text=f"Label {i}", bg="lightgrey").pack(fill="x")


    def on_canvas_resized(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas_frame, width=canvas_width)
        self.scrollable_frame.config(width=canvas_width)

    def update_list(self):
        # Clear previous contents
        print(self.scrollable_frame.winfo_children())
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Get list of files
        print(os.listdir(self.folder_path))
        files = os.listdir(self.folder_path)
        if not files:
            no_data_label = ttk.Label(self.scrollable_frame, text="No Data Found")
            no_data_label.pack(fill="x", pady=10)
        else:
            for file in files:
                file_path = os.path.join(self.folder_path, file)
                if os.path.isfile(file_path):
                    file_date = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
                    #tk.Label(self.scrollable_frame, text=f"Label {file_date}", bg="lightgrey").pack(fill="x")
                    self.add_file_row(file_date)

    def add_file_row(self, file_date):
        #tk.Label(self.scrollable_frame, text=f"Label {file_date}", bg="lightgrey").pack(fill="x")
        frame = tk.Frame(self.scrollable_frame, bg="#EFEFEF")
        #frame = tk.Frame(self.scrollable_frame, bg="purple").pack(fill="x")

        date_label = ttk.Label(frame, text=file_date)
        date_label.pack(side=tk.LEFT, padx=10)

        review_button = ttk.Button(frame, text="Review", command=lambda: self.review_file(file_date))
        review_button.pack(side=tk.RIGHT, padx=10)

        frame.pack(fill='x', expand=True, pady=5)

    def review_file(self, file_date):
        print(f"Reviewing file from date: {file_date}")


