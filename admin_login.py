import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

# List of credentials
stored_credentials = [
    {"username": "admin", "password": "123"},
    {"username": "smit", "password": "smit"},
    {"username": "dharmik", "password": "dharmik"},
    {"username": "yash", "password": "yash"}
]

def login_admin():
    entered_username = entry_login_username.get()
    entered_password = entry_login_password.get()

    # Check credentials
    for cred in stored_credentials:
        if entered_username == cred["username"] and entered_password == cred["password"]:
            messagebox.showinfo("Login Successful", f"Welcome, {entered_username}!")
            login_window.destroy()

            # Run admin.py using subprocess
            try:
                subprocess.run(["python", "admin.py"])  
            except Exception as e:
                messagebox.showerror("Error", f"Error running the admin script: {e}")
            return
    messagebox.showerror("Login Failed", "Invalid Details. Please try again.")

# Initialize Tkinter window
login_window = tk.Tk()
login_window.title("Admin Login")
login_window.geometry("1360x700+0+0")
login_window.resizable(False, False)

# Load Background Image
try:
    image = Image.open("E:\\Billing Software\\image\\background.jpg")  
    image = image.resize((1360, 700), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
except Exception as e:
    messagebox.showerror("Error", f"Error loading background image: {e}")
    bg_image = None

# Display Background Image
if bg_image:
    background_label = tk.Label(login_window, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame for Login
frame = tk.Frame(login_window, bg="white", bd=10, relief="flat")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

# Title Label
title = tk.Label(frame, text="ADMIN LOGIN", font=("Helvetica", 24, "bold"), fg="white", bg="#074463", padx=10, pady=10)
title.pack(pady=20, fill=tk.X)

# Username Label and Entry
label_login_username = tk.Label(frame, text="Username:", font=("Arial", 14, "bold"), bg="white")
label_login_username.pack(pady=10)
entry_login_username = tk.Entry(frame, font=("Arial", 14), width=22, bd=2, relief="solid")
entry_login_username.pack(pady=5)

# Password Label and Entry
label_login_password = tk.Label(frame, text="Password:", font=("Arial", 14, "bold"), bg="white")
label_login_password.pack(pady=10)
entry_login_password = tk.Entry(frame, font=("Arial", 14), width=22, bd=2, relief="solid", show="*")
entry_login_password.pack(pady=5)

# Login Button with Gradient Effect
def gradient_color(widget, color1, color2):
    widget.config(
        bg=color1,
        activebackground=color2,
        fg="white",
        font=("Arial", 14, "bold"),
        relief="flat",
        bd=5,
        width=15
    )

login_button = tk.Button(frame, text="Login", command=login_admin)
gradient_color(login_button, "#007bff", "#0056b3")
login_button.pack(pady=20)

# Run the main loop
login_window.mainloop()
