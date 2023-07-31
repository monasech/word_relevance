#This file contains the utility functions associated with the word relevancy project. 

import tkinter as tk
from tkinter import filedialog,messagebox


def ask_directory(title, message):
  root = tk.Tk()
  # Hide the main window
  root.withdraw()

  # Show a message to the user
  messagebox.showinfo(title,message)

  # Raise the file dialog prompting the user to select a directory
  directory = filedialog.askdirectory()

  # Print the selected directory to the console
  print(f"You selected the directory {directory}")

  
# Call the function with specific title and message
#ask_directory("Directory Selection","Please select a directory for your purpose.")




    
  