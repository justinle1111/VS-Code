import tkinter

def create_empty_window() -> None:
    window = tkinter.Tk()
    window.title("ICS32 Example Gui")
    message = tkinter.Label(master=window, text = "this is example label")
    button = tkinter.Button(master=window, text='Press me', command=run_method)

    message.pack()
    button.pack()
    window.mainloop()

def run_method() -> None:
    print("Hey")

if __name__ == "__main__":
    create_empty_window()
