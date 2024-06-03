import tkinter as tk
from tkinter import messagebox

class MenuApp:
    def __init__(self, root, username, password):
        self.root = root
        self.root.title("Login")
        self.username = username
        self.password = password
        bg_color = root.cget("bg")

        # Membuat frame dan menempatkannya di tengah jendela
        frame = tk.Frame(root, width=300, height=300, bg=bg_color)
        frame.place(relx=0.5, rely=0.4 , anchor=tk.CENTER)

        # Label "selamat datang"
        self.welcome_label = tk.Label(frame, text="Halo, selamat datang user", font=("Futura", 14))
        self.welcome_label.grid(row=0, column=0, columnspan=2, pady=(50, 20))  # Padding atas diatur ke 50px

        # Button "Quiz"
        self.login_button = tk.Button(frame, text="       Quiz       ", font=("Futura", 20), command=self.login)
        self.login_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Button "Lihat Peringkat"
        self.signup_button = tk.Button(frame, text="Lihat Peringkat", font=("Futura", 20), command=self.register)
        self.signup_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Button "Log Out"
        self.exit_button = tk.Button(frame, text="     Log Out    ", font=("Futura", 20), command=self.exit_program)
        self.exit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if username == "a" and password == "a":
            messagebox.showinfo("login","Berhasil Login")
        else:
            messagebox.showinfo("login","Gagal Login")
    
    def register(self):
        pass

    def exit_program(self):
        exit()

def start():
    # Inisialisasi Tkinter
    root = tk.Tk()
    root.title("Login")
    root.attributes("-fullscreen", True)  # Set fullscreen

    # Membuat instance dari LoginApp
    app = MenuApp(root, "", "")

    # Memulai loop utama Tkinter
    root.mainloop()

global root


