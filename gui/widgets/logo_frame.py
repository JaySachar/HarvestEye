import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class LogoFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)


        # ========================================/
        self.image_path = "./assets/datatype-select/"

        self.configure(bg="white")


        # ------------------------------
        #Logo frame that  goes to the bottom right

        logo_frame = tk.Frame(self)
        logo_frame.pack(side="right")
        logo_frame.configure(bg='white')
        # Load the LOGO img
        photo = ImageTk.PhotoImage(Image.open(self.image_path+"Logo_sm.png"))
        img_logo = tk.Label(logo_frame, image=photo, borderwidth=0)
        img_logo.image = photo
        img_logo.pack(side="top", expand=True, anchor="se")


        # Write text for under the LOGO
        txt_underlogo= tk.Label(logo_frame,
                                 text = "Product of SkyHarvest Insights\n" + u"\N{COPYRIGHT SIGN}" + " All rights reserved",
                                 font = ("Montserrat", 10),
                                #wraplength=140,
                                 justify="right")
        #txt_underlogo.grid(row=3,column=2,padx=5, pady=5, sticky="se")
        txt_underlogo.pack(side="bottom")
        txt_underlogo.configure(bg='white')
        # ------------------------------

