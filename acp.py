import tkinter as tk

def calculate_interest():
    try:
        p = float(principal_entry.get())
        r = float(rate_entry.get())
        t = float(time_entry.get())

        si = (p * r * t) / 100
        ci = p * ((1 + r / 100) ** t) - p

        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}")
    except:
        result_label.config(text="Please enter valid numbers.")

root = tk.Tk()
root.title("Interest Calculator")
root.geometry("300x280")
root.resizable(False, False)

tk.Label(root, text="Interest Calculator", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Principal:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
principal_entry = tk.Entry(root, width=20)
principal_entry.grid(row=1, column=1, pady=5)

tk.Label(root, text="Rate (%):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
rate_entry = tk.Entry(root, width=20)
rate_entry.grid(row=2, column=1, pady=5)

tk.Label(root, text="Time (years):").grid(row=3, column=0, padx=10, pady=5, sticky="e")
time_entry = tk.Entry(root, width=20)
time_entry.grid(row=3, column=1, pady=5)

tk.Button(root, text="Calculate", command=calculate_interest, bg="#4CAF50", fg="white", width=15).grid(row=4, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 11))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
