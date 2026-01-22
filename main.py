import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import winsound
import platform
import os
import socket
import json

class DemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Demo Application")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title Label - explicit positioning
        title_label = tk.Label(
            self.root, 
            text="Welcome to the Demo App", 
            font=("Arial", 18, "bold"),
            bg="#4A90E2",
            fg="white"
        )
        title_label.place(x=0, y=0, width=700, height=60)
        self.server_send("UI_show", "main.py_line15")
        
        # Text Input Section
        input_label = tk.Label(
            self.root,
            text="User Input",
            font=("Arial", 11, "bold"),
            bg="#E8E8E8"
        )
        input_label.place(x=20, y=80, width=660, height=30)
        self.server_send("UI_show", "main.py_line27")
        
        # Name Label
        name_label = tk.Label(self.root, text="Name:", anchor="w")
        name_label.place(x=30, y=120, width=80, height=25)
        self.server_send("UI_show", "main.py_line35")
        
        # Name Entry
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.place(x=120, y=120, width=250, height=25)
        self.server_send("UI_show", "main.py_line41")
        
        # Email Label
        email_label = tk.Label(self.root, text="Email:", anchor="w")
        email_label.place(x=30, y=155, width=80, height=25)
        self.server_send("UI_show", "main.py_line46")
        
        # Email Entry
        self.email_entry = ttk.Entry(self.root)
        self.email_entry.place(x=120, y=155, width=250, height=25)
        self.server_send("UI_show", "main.py_line52")
        
        # Dropdown Section
        dropdown_label = tk.Label(
            self.root,
            text="Selection Options",
            font=("Arial", 11, "bold"),
            bg="#E8E8E8"
        )
        dropdown_label.place(x=20, y=200, width=660, height=30)
        self.server_send("UI_show", "main.py_line59")
        
        # Category Label
        category_label = tk.Label(self.root, text="Choose Category:", anchor="w")
        category_label.place(x=30, y=240, width=150, height=25)
        self.server_send("UI_show", "main.py_line67")
        
        # Category Dropdown
        self.category_var = tk.StringVar()
        category_dropdown = ttk.Combobox(
            self.root, 
            textvariable=self.category_var,
            values=["Technology", "Business", "Education", "Entertainment", "Other"],
            state="readonly"
        )
        category_dropdown.place(x=190, y=240, width=200, height=25)
        category_dropdown.current(0)
        self.server_send("UI_show", "main.py_line77")
        
        # Checkboxes Section
        checkbox_label = tk.Label(
            self.root,
            text="Preferences",
            font=("Arial", 11, "bold"),
            bg="#E8E8E8"
        )
        checkbox_label.place(x=20, y=285, width=660, height=30)
        self.server_send("UI_show", "main.py_line87")
        
        # Newsletter Checkbox
        self.newsletter_var = tk.BooleanVar()
        newsletter_check = ttk.Checkbutton(
            self.root, 
            text="Subscribe to Newsletter", 
            variable=self.newsletter_var
        )
        newsletter_check.place(x=30, y=325, width=250, height=25)
        self.server_send("UI_show", "main.py_line97")
        
        # Notifications Checkbox
        self.notifications_var = tk.BooleanVar()
        notifications_check = ttk.Checkbutton(
            self.root, 
            text="Enable Notifications", 
            variable=self.notifications_var
        )
        notifications_check.place(x=30, y=355, width=250, height=25)
        self.server_send("UI_show", "main.py_line105")
        
        # Radio Buttons Section
        radio_label = tk.Label(
            self.root,
            text="Experience Level",
            font=("Arial", 11, "bold"),
            bg="#E8E8E8"
        )
        radio_label.place(x=20, y=395, width=660, height=30)
        self.server_send("UI_show", "main.py_line115")
        
        # Experience Radio Buttons
        self.experience_var = tk.StringVar(value="intermediate")
        
        beginner_radio = ttk.Radiobutton(
            self.root, 
            text="Beginner", 
            variable=self.experience_var, 
            value="beginner"
        )
        beginner_radio.place(x=30, y=435, width=150, height=25)
        self.server_send("UI_show", "main.py_line125")
        
        intermediate_radio = ttk.Radiobutton(
            self.root, 
            text="Intermediate", 
            variable=self.experience_var, 
            value="intermediate"
        )
        intermediate_radio.place(x=200, y=435, width=150, height=25)
        self.server_send("UI_show", "main.py_line133")
        
        advanced_radio = ttk.Radiobutton(
            self.root, 
            text="Advanced", 
            variable=self.experience_var, 
            value="advanced"
        )
        advanced_radio.place(x=370, y=435, width=150, height=25)
        self.server_send("UI_show", "main.py_line141")
        
        # Button Section
        submit_button = ttk.Button(
            self.root, 
            text="Submit Form", 
            command=self.submit_form
        )
        submit_button.place(x=30, y=480, width=130, height=35)
        self.server_send("UI_show", "main.py_line149")
        
        info_button = ttk.Button(
            self.root, 
            text="Show Info Dialog", 
            command=self.show_info
        )
        info_button.place(x=175, y=480, width=130, height=35)
        self.server_send("UI_show", "main.py_line155")
        
        sound_button = ttk.Button(
            self.root, 
            text="Play Sound", 
            command=self.play_sound
        )
        sound_button.place(x=320, y=480, width=130, height=35)
        self.server_send("UI_show", "main.py_line161")
        
        file_button = ttk.Button(
            self.root, 
            text="Open File Dialog", 
            command=self.open_file
        )
        file_button.place(x=465, y=480, width=130, height=35)
        self.server_send("UI_show", "main.py_line167")
        
        # Progress Bar Label
        progress_label = tk.Label(self.root, text="Progress Demonstration:", anchor="w")
        progress_label.place(x=30, y=535, width=200, height=25)
        self.server_send("UI_show", "main.py_line174")
        
        # Progress Bar
        self.progress = ttk.Progressbar(
            self.root, 
            length=300, 
            mode='determinate'
        )
        self.progress.place(x=200, y=570, width=400, height=25)
        self.server_send("UI_show", "main.py_line182")
        
        # Start Progress Button
        progress_button = ttk.Button(
            self.root, 
            text="Start Progress", 
            command=self.start_progress
        )
        progress_button.place(x=250, y=605, width=200, height=35)
        self.server_send("UI_show", "main.py_line190")
        
        # Aperture Runner Button
        aperture_button = ttk.Button(
            self.root,
            text="Run Aperture",
            command=self.aperture_runner
        )
        aperture_button.place(x=30, y=605, width=130, height=35)
        
    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        category = self.category_var.get()
        newsletter = "Yes" if self.newsletter_var.get() else "No"
        notifications = "Yes" if self.notifications_var.get() else "No"
        experience = self.experience_var.get()
        
        if not name or not email:
            messagebox.showwarning("Warning", "Please fill in all required fields!")
            self.play_sound()
            self.server_send("add_popup", "Please fill in all required fields!")
            return
        
        message = f"""Form Submitted Successfully!
        
Name: {name}
Email: {email}
Category: {category}
Newsletter: {newsletter}
Notifications: {notifications}
Experience: {experience.capitalize()}"""
        
        messagebox.showinfo("Success", message)
        self.play_sound()
        
    def show_info(self):
        result = messagebox.askyesno(
            "Confirmation", 
            "Do you want to see application information?"
        )
        if result:
            info = f"""Demo Application v1.0
            
Platform: {platform.system()}
Python Version: {platform.python_version()}
            
This is a demonstration of tkinter UI elements including:
• Text entries
• Dropdowns
• Checkboxes
• Radio buttons
• Progress bars
• Popups and dialogs
• Sound feedback"""
            messagebox.showinfo("Application Info", info)
    
    def play_sound(self):
        try:
            if platform.system() == "Windows":
                winsound.Beep(1000, 200)  # Frequency: 1000Hz, Duration: 200ms
            else:
                # For macOS/Linux, print a message (or use other audio libraries)
                print("\a")  # Terminal bell
                messagebox.showinfo("Sound", "Sound played (system bell)")
        except Exception as e:
            messagebox.showerror("Error", f"Could not play sound: {e}")
    
    def open_file(self):
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            messagebox.showinfo("File Selected", f"You selected:\n{filename}")
    
    def start_progress(self):
        self.progress['value'] = 0
        self.animate_progress()
    
    def animate_progress(self):
        if self.progress['value'] < 100:
            self.progress['value'] += 10
            self.root.after(200, self.animate_progress)
        else:
            messagebox.showinfo("Complete", "Progress complete!")
            self.play_sound()

    def aperture_runner(self):
        system = platform.system()
        if system == "Windows":
            aperture_path = "./Aperture.exe"
        elif system == "Darwin":  # macOS
            aperture_path = "./Aperture.app"
        else:  # Linux and others
            aperture_path = "./Aperture"
        
        if os.path.exists(aperture_path):
            try:
                os.startfile(aperture_path) if system == "Windows" else os.system(f"open {aperture_path}" if system == "Darwin" else f"chmod +x {aperture_path} && {aperture_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not run aperture: {e}")
        else:
            messagebox.showerror("Error", "Aperture file not found!")

    def server_send(self, content_type, content):
        data = {"type": content_type, "content": content}
        json_string = json.dumps(data)
        byte_data = json_string.encode('utf-8')
        length = len(byte_data)
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(('localhost', 8080))
            sock.send(f"{length}\n".encode('utf-8') + byte_data)
            sock.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send data: {e}")

def main():
    root = tk.Tk()
    app = DemoApp(root)
    root.mainloop()
    app.server_send("UI_show", "EOF")

if __name__ == "__main__":