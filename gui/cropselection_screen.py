import tkinter as tk

class CropSelectionScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, 
                         text = "This is crop selection screen",
                         font = controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self,
                           text = "Go to SplashScreen",
                           command = lambda: controller.show_frame("SplashScreen"))
        button.pack()

