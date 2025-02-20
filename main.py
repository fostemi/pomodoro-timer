import tkinter
from tkinter import ttk

root = tkinter.Tk()

def main():
    frame = ttk.Frame(root, padding=10)
    frame.grid()
    ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()

if __name__ == "__main__":
    main()
