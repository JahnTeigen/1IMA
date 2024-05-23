import tkinter as tk
from tkinter import messagebox

class SignInApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign In")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(root, show="*")  # Show * for password
        self.password_entry.pack()

        self.sign_in_button = tk.Button(root, text="Sign In", command=self.sign_in)
        self.sign_in_button.pack()

    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Add your authentication logic here
        # For simplicity, let's assume a hardcoded username and password
        if username == "user" and password == "password":
            messagebox.showinfo("Success", "Sign In Successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")

if __name__ == "__main__":
    root = tk.Tk()
    app = SignInApp(root)
    root.mainloop()
