import tkinter as tk
from tkinter import messagebox
import read_email_invoice  # Import the next module

def on_submit():
    email_user = email_entry.get()
    email_pass = password_entry.get()
    if not email_user or not email_pass:
        messagebox.showerror("Error", "Enter both email and app password.")
        return

    result = read_email_invoice.fetch_latest_invoice(email_user, email_pass)
    messagebox.showinfo("Status", result)

root = tk.Tk()
root.title("Gmail Login for Invoice Fetching")

tk.Label(root, text="Gmail ID:").grid(row=0, column=0, padx=10, pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=0, column=1)

tk.Label(root, text="App Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.grid(row=1, column=1)

tk.Button(root, text="Fetch Latest Invoice", command=on_submit).grid(row=2, column=0, columnspan=2, pady=20)
root.mainloop()
