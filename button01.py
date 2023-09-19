import tkinter as tk
from tkinter import messagebox

print("HELLO")

def printName():
    result = messagebox.askyesnocancel("TITLE", "Choose yes or no.")
    print(result)
    if result == True:
        print("Check")
        messagebox.showinfo("Info", "User clicked Yes")
    elif result == False:
        messagebox.showinfo("Info 2", "User clicked No")
    else:
        messagebox.showinfo("Info 3", "User did not click yes or no")
    return

#canvas setup
root = tk.Tk()
root.geometry("500x500")
root.title("Jack's Canvas")

#label setup
jpsLabel = tk.Label(root, text="Jack's Label", font=("Arial", 12))
jpsLabel.pack()

#button setup
jpsButton = tk.Button(root, text="Press Me, I Dare You", font=("Arial", 10), command=printName)
jpsButton.pack()




root.mainloop()
