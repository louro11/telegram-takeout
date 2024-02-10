import tkinter as tk
from tkinter import messagebox
from takeout import *

# Create main window
root = tk.Tk()
root.title("Telegram Takeout")

def submit_code():
	# Create a new window
	new_window = tk.Toplevel(root)
	new_window.title("Telegram Takeout")
	new_window.geometry(root.geometry())

	# Label in the new window
	label = tk.Label(new_window, text="New Window")
	label.pack()

	# Entry widget for text input
	entry = tk.Entry(new_window)
	entry.pack()

	# Button in the new window
	button = tk.Button(new_window, text="Submit")
	button.pack()
	
	root.wait_window(new_window)

def submit():
	api_id = api_id_entry.get()
	api_hash = api_hash_entry.get()
	phone_number = phone_number_entry.get()

	if api_id.strip() == "" or api_hash.strip() == "" or phone_number.strip() == "":
		messagebox.showerror("Error", "Please fill in all fields.")

	else:
		confirmation_code_label = tk.Label(root, text="Code:", font=label_font)
		confirmation_code_label.place(relx=0.15, rely=0.7, anchor=tk.CENTER)
		confirmation_code_entry = tk.Entry(root, width=30)
		confirmation_code_entry.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

		submit_code_button = tk.Button(root, text="Submit Confirmation Code", command=submit_code)
		submit_code_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the window width and height (25% of the screen)
window_width = int(screen_width * 0.25)
window_height = int(screen_height * 0.25)

# Calculate the x and y coordinates for the window to be centered
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2

# Set the geometry of the window
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.resizable(False, False)

# Create and place labels and entry fields
label_font = ("Arial", 10)  # Change the font size here

# Create and place labels and entry fields
padx=10
pady=5
api_id_label = tk.Label(root, text="api id:", font=label_font)
api_id_label.grid(row=0, column=0, padx=padx, pady=pady)
api_id_entry = tk.Entry(root, width=window_width)
api_id_entry.grid(row=0, column=1, padx=padx, pady=pady)

api_hash_label = tk.Label(root, text="api hash:", font=label_font)
api_hash_label.grid(row=1, column=0, padx=padx, pady=pady)
api_hash_entry = tk.Entry(root, width=window_width)
api_hash_entry.grid(row=1, column=1, padx=padx, pady=pady)

phone_number_label = tk.Label(root, text="phone number:", font=label_font)
phone_number_label.grid(row=2, column=0, padx=padx, pady=pady)
phone_number_entry = tk.Entry(root, width=window_width)
phone_number_entry.grid(row=2, column=1, padx=padx, pady=pady)

# Create submit button
submit_button = tk.Button(root, text="Submit API credentials", command=submit)
#submit_button.grid(row=3, column=0, columnspan=1, padx=padx, pady=10)
submit_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# Start the main loop
root.mainloop()