import tkinter as tk

root = tk.Tk()

root.geometry("500x500")

root.title("My First GUI")

label = tk.Label(root, text="Hello World")
label.pack(padx=10)

textbox = tk.Text(root, height=3)
textbox.pack()

button = tk.Button(root, text="Click me")
button.pack()


root.mainloop()