import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        calculated_km = float(miles_entry.get()) * 1.60934
        
        km_value.set("{:.2f}".format(calculated_km))
    except ValueError:
        error_value.set("Bitte einen gültigen Zahlenwert eingeben!")

root = tk.Tk()
root.geometry("500x250")
root.title("Einheiten-Umrechner")

km_value = tk.StringVar(value="Hier erscheint gleich das Ergebnis...")
error_value = tk.StringVar()

miles_label = ttk.Label(root, text="Meilen:", font=("Arial", 18))
miles_label.pack(side="top", fill="x", padx=5, pady=2)

miles_entry = ttk.Entry(root, font=("Arial", 18))
miles_entry.pack(side="top", fill="x", padx=5, pady=2)

km_label = ttk.Label(root, text="Kilometer:", font=("Arial", 18))
km_label.pack(side="top", fill="x", padx=5, pady=2)

km_display = ttk.Label(root, textvariable=km_value, font=("Arial", 18))
km_display.pack(side="top", fill="x", padx=5, pady=2)

error_display = ttk.Label(root, textvariable=error_value, foreground="red", font=("Arial", 18))
error_display.pack(side="top", fill="x", padx=5, pady=2)

calc_button = ttk.Button(root, text="Umrechnung starten", command=calculate)
calc_button.pack(side="bottom", fill="x", padx=10, pady=10 )


root.mainloop()