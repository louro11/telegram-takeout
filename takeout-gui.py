import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Telegram Takeout")

def submit_code():
	print("Hello")

def submit():
	api_id = api_id_entry.get()
	api_hash = api_hash_entry.get()
	phone_number = phone_number_entry.get()

	if api_id.strip() == "" or api_hash.strip() == "" or phone_number.strip() == "":
		messagebox.showerror("Error", "Please fill in all fields.")

	else:
		#result_window = tk.Toplevel(root)
		confirmation_code_label = tk.Label(root, text="Code:", font=label_font)
		confirmation_code_label.grid(row=4, column=0, padx=10, pady=5)
		confirmation_code_entry = tk.Entry(root, width=30)
		confirmation_code_entry.grid(row=4, column=1, padx=15, pady=5)
		# Create submit button
		submit_button = tk.Button(root, text="Submit Confirmation Code", command=submit_code)
		submit_button.grid(row=5, column=0, columnspan=1, padx=10, pady=10, sticky="WE")



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
api_id_label = tk.Label(root, text="api id:", font=label_font)
api_id_label.grid(row=0, column=0, padx=10, pady=5)
api_id_entry = tk.Entry(root, width=55)
api_id_entry.grid(row=0, column=1, padx=15, pady=5)

api_hash_label = tk.Label(root, text="api hash:", font=label_font)
api_hash_label.grid(row=1, column=0, padx=10, pady=5)
api_hash_entry = tk.Entry(root, width=55)
api_hash_entry.grid(row=1, column=1, padx=15, pady=5)

phone_number_label = tk.Label(root, text="phone number:", font=label_font)
phone_number_label.grid(row=2, column=0, padx=10, pady=5)
phone_number_entry = tk.Entry(root, width=55)
phone_number_entry.grid(row=2, column=1, padx=15, pady=5)

# Create submit button
submit_button = tk.Button(root, text="Submit credentials", command=submit)
submit_button.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky="WE")

# Start the main loop
root.mainloop()