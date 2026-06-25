import tkinter as tk
from tkinter import messagebox

# ---------------- LOGIN DETAILS ----------------
USERNAME = "admin"
PASSWORD = "bank123"

# ---------------- LOGIN FUNCTION ----------------
def login():
    if user_entry.get() == USERNAME and pass_entry.get() == PASSWORD:
        messagebox.showinfo("Success", "Secure Login Successful!")
        open_dashboard()
    else:
        messagebox.showerror("Error", "Invalid Username or Password")

# ---------------- DASHBOARD ----------------
def open_dashboard():
    dashboard = tk.Toplevel(root)
    dashboard.title("Cyber Security Banking Dashboard")
    dashboard.geometry("700x500")
    dashboard.configure(bg="#0B2447")

    heading = tk.Label(
        dashboard,
        text=" CYBER SECURITY IN BANKING SYSTEM",
        font=("Arial", 20, "bold"),
        bg="#0B2447",
        fg="cyan"
    )
    heading.pack(pady=15)

    tk.Label(
        dashboard,
        text="Enter Transaction Amount (₹)",
        font=("Arial", 14),
        bg="#0B2447",
        fg="white"
    ).pack()

    amount_entry = tk.Entry(
        dashboard,
        font=("Arial", 14),
        width=20
    )
    amount_entry.pack(pady=10)

    result = tk.Label(
        dashboard,
        text="",
        font=("Arial", 15, "bold"),
        bg="#0B2447"
    )
    result.pack(pady=20)

    def verify_transaction():
        try:
            amount = float(amount_entry.get())

            if amount > 100000:
                result.config(
                    text="⚠ HIGH-RISK TRANSACTION DETECTED",
                    fg="red"
                )
            elif amount > 50000:
                result.config(
                    text="Additional Verification Required",
                    fg="orange"
                )
            else:
                result.config(
                    text="Secure Transaction Approved",
                    fg="lime"
                )
        except:
            result.config(
                text="Invalid Amount",
                fg="yellow"
            )

    verify_btn = tk.Button(
        dashboard,
        text="VERIFY TRANSACTION",
        command=verify_transaction,
        font=("Arial", 12, "bold"),
        bg="#00C897",
        fg="white",
        width=25
    )
    verify_btn.pack(pady=10)

    # Security Features Section
    frame = tk.Frame(dashboard, bg="#19376D")
    frame.pack(pady=25, fill="x", padx=30)

    tk.Label(
        frame,
        text="BANKING SECURITY FEATURES",
        font=("Arial", 16, "bold"),
        bg="#19376D",
        fg="white"
    ).pack(pady=10)

    features = [
        "Multi-Factor Authentication",
        "Firewall Protection",
        "Intrusion Detection System",
        "Data Encryption",
        "AI Fraud Monitoring",
        "☁ Secure Cloud Banking"
    ]

    for item in features:
        tk.Label(
            frame,
            text=item,
            font=("Arial", 12),
            bg="#19376D",
            fg="lightgreen"
        ).pack(anchor="w", padx=20)

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Cyber Security Banking System")
root.geometry("500x400")
root.configure(bg="#1A1A40")

title = tk.Label(
    root,
    text=" Secure Banking Login",
    font=("Arial", 22, "bold"),
    bg="#1A1A40",
    fg="cyan"
)
title.pack(pady=20)

tk.Label(
    root,
    text="Username",
    font=("Arial", 12),
    bg="#1A1A40",
    fg="white"
).pack()

user_entry = tk.Entry(root, font=("Arial", 12))
user_entry.pack(pady=5)

tk.Label(
    root,
    text="Password",
    font=("Arial", 12),
    bg="#1A1A40",
    fg="white"
).pack()

pass_entry = tk.Entry(root, show="*", font=("Arial", 12))
pass_entry.pack(pady=5)

login_btn = tk.Button(
    root,
    text="SECURE LOGIN",
    command=login,
    font=("Arial", 12, "bold"),
    bg="#00C897",
    fg="white",
    width=20
)
login_btn.pack(pady=20)

tk.Label(
    root,
    text="Demo Login\nUsername: admin\nPassword: bank123",
    bg="#1A1A40",
    fg="lightgray",
    font=("Arial", 10)
).pack()

root.mainloop()
