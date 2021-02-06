import tkinter as tk #Gui
from tkinter import filedialog, Text #App, and Text
import json

root = tk.Tk()

files = []

#Function definitions
def addFile():

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("JSON Files", "*.json"),("Executables", "*.exe"), ("All Files", "*.*")))

    files.append(filename)
    print(filename) #For debugging



def parseFile():
    wfile = open("output.txt", "w")
    for file in files:
        with open(file, 'r') as f:
            distros_dict = json.load(f)
            for distro in distros_dict:
                label = tk.Label(frame, text=distro['text'], bg="gray")
                label.pack() #working on scroll bar

                #Write to file
                wfile.write(''.join(distro['text']))
                wfile.write("\n")
        
    wfile.close()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#Buttons
openFile = tk.Button(root, text="Open JSON to parse", padx=10, pady=5, fg="white", bg="#263D42", command=addFile)

#Draw
openFile.pack()

#Parse button
parseButton = tk.Button(root, text="Parse", padx=10, pady=5, fg="white", bg="#263D42", command=parseFile)

parseButton.pack()

root.mainloop()