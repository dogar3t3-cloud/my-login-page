import pyjokes
import tkinter as tk

def show_joke():
    joke = pyjokes.get_joke()
    label.config(text=joke)

root = tk.Tk()
root.title("Joke Generator")
root.geometry("400x200")

label = tk.Label(root, text="Click button for joke", wraplength=350)
label.pack(pady=20)

button = tk.Button(root, text="Get Joke", command=show_joke)
button.pack()

root.mainloop()