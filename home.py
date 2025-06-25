from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import cv2

# Main class for the application
class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1360x700+0+0")
        self.root.title("Home Page")

        # Load video
        self.video_path = "E:\\Billing Software\\video\\background1.mp4"  # Replace with your actual path
        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Unable to load video.")
            return

        # Label to show video frames
        self.video_label = tk.Label(self.root)
        self.video_label.place(relwidth=1, relheight=1)

        # Title label (on top of video)
        self.title_label = tk.Label(self.root, text="WELCOME TO KHODAL RETAILS", bg="#074463", fg="white",
                                    font=("times new roman", 24, "bold"), pady=20)
        self.title_label.pack(fill=tk.X)

        # Admin Button
        self.admin_button = tk.Button(self.root, text="Admin", width=10, height=1, font=("times new roman", 15, "bold"),
                                      command=self.admin_function, bd=5, relief="ridge")
        self.apply_gradient(self.admin_button, "#FF7F50", "#FF4500")
        self.admin_button.place(relx=0.06, rely=0.06, anchor="center")

        # User Button
        self.user_button = tk.Button(self.root, text="User", width=10, height=1, font=("times new roman", 15, "bold"),
                                     command=self.user_function, bd=5, relief="ridge")
        self.apply_gradient(self.user_button, "#32CD32", "#228B22")
        self.user_button.place(relx=0.94, rely=0.06, anchor="center")

        # Start video loop
        self.update_video_frame()

    def apply_gradient(self, button, color1, color2):
        button.config(
            bg=color1,
            activebackground=color2,
            fg="white"
        )

    def update_video_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (1355, 690))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(Image.fromarray(frame))
            self.video_label.configure(image=img)
            self.video_label.image = img
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

        self.root.after(30, self.update_video_frame)

    def admin_function(self):
        try:
            subprocess.run(["python", "admin_login.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error running the admin script: {e}")

    def user_function(self):
        try:
            subprocess.run(["python", "bill.py"])
        except Exception as e:
            messagebox.showerror("Error", f"Error running the user script: {e}")

# Main function
if __name__ == "__main__":
    root = tk.Tk()
    home_page = HomePage(root)
    root.mainloop()
