import tkinter as tk

root = tk.Tk()

# set frame
picture = tk.Frame(root)
buttons = tk.Frame(root)
picture.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
buttons.pack(side=tk.BOTTOM)

# create buttons
yes_button = tk.Button(root, text="Yes", width=10, height=2)
yes_button.pack(in_=buttons, side=tk.LEFT)

no_button = tk.Button(root, text="No", width=10, height=2)
no_button.pack(in_=buttons, side=tk.LEFT)

# set picture
text = tk.Label(root, text="Picture will go here")
text.pack(in_=picture, side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()
