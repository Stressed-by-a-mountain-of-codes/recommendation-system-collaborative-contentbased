import tkinter as tk

def test_gui():
    root = tk.Tk()
    root.title("Test GUI")
    root.geometry("300x200")

    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=50)

    root.mainloop()

if __name__ == "__main__":
    test_gui()
