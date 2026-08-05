# Author: Jack Lidster
# Date: 2026-08-03
# Description: 
# This program uses code to show how a vending machine works. 
# It will take in a user input of money and then allow the user to select a product. 
# The program will then calculate the change and display it to the user.
from tkinter import Tk, Label, Entry, Frame, Button, BOTH, CENTER

WINDOW_WIDTH = 425
WINDOW_HEIGHT = 450
WINDOW_MIN_WIDTH = 425
WINDOW_MIN_HEIGHT = 450

# Color palette
COLOR_BG = "#e6f7ff"       # light blue background
ACCENT = "#003366"         # dark blue for text
ENTRY_BG = "#fffde6"       # light yellow for entries
ENTRY_BORDER = "#99ccff"   # entry border highlight
BUTTON_CALC_BG = "#28a745" # green
BUTTON_RESET_BG = "#dc3545"# red
BUTTON_FG = "#ffffff"      # white text on buttons
OUTPUT_BG = "#f0fbff"      # very light blue for output area

# Category background colors for output
OUT_BG_SEVERE = "#cce5ff"  # light blue
OUT_BG_UNDER = "#fff3cd"   # light yellow/orange
OUT_BG_HEALTHY = "#d4edda" # light green
OUT_BG_OVER = "#ffe5b4"    # peach/light orange
OUT_BG_OBESE = "#f8d7da"   # light red/pink

PRODUCTS = {
    "A1": ("Coke", 1.50),
    "A2": ("Water", 0.75),
    "B1": ("Chocolate bar", 2.00),
    "B2": ("Chips", 1.25),
}

window = Tk()

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
window.minsize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)

window.title("Vending Machine")
window.configure(bg=COLOR_BG)

# Create GUI elements
label_money = Label(window, text="Insert money ($):", bg=COLOR_BG, fg=ACCENT)
label_money.pack(pady=5)

entry_money = Entry(window, bg=ENTRY_BG, fg=ACCENT, font=("Arial", 12))
entry_money.pack(pady=5)

selected_letter = ""

def entry_purchase_item():
    try:
        money = float(entry_money.get())
        label_output.configure(text=f"Money inserted: ${money:.2f}. Please select a product.", fg=ACCENT, bg=OUTPUT_BG)
    except ValueError:
        label_output.configure(text="Error: please insert money first.",
                               fg="#b30000", bg="#ffe6e6")

def select_product(code, name, price):
    try:
        money = float(entry_money.get())
        if money < price:
            label_output.configure(text=f"Error: insufficient funds. {name} costs ${price:.2f}.",
                                   fg="#b30000", bg="#ffe6e6")
            return
        change = money - price
        label_output.configure(text="Dispensing product...", fg=ACCENT, bg=OUTPUT_BG)
        window.after(2000, lambda: (
            label_output.configure(text=f"Product dispensed! Enjoy your {name}! Your change is ${change:.2f}", fg=ACCENT, bg=OUTPUT_BG),
        ))
        entry_money.delete(0, 'end')
        entry_money.insert(0, f"{change:.2f}")
        label_code.configure(text="--")
    except ValueError:
        label_output.configure(text="Error: please insert money first.",
                               fg="#b30000", bg="#ffe6e6")
        label_code.configure(text="--")

def press_letter(letter):
    global selected_letter
    selected_letter = letter
    label_code.configure(text=f"{letter}_")

def press_number(number):
    global selected_letter
    if not selected_letter:
        label_output.configure(text="Select a letter first (A or B).",
                               fg="#b30000", bg="#ffe6e6")
        return
    code = selected_letter + number
    label_code.configure(text=code)
    selected_letter = ""
    if code in PRODUCTS:
        name, price = PRODUCTS[code]
        select_product(code, name, price)
    else:
        label_output.configure(text=f"Invalid selection: {code}",
                               fg="#b30000", bg="#ffe6e6")

button_frame = Frame(window, bg=COLOR_BG)
button_frame.pack(pady=5)

# Product listing
Label(button_frame, text="A1: Coke              $1.50", bg=COLOR_BG, fg=ACCENT, anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", padx=10)
Label(button_frame, text="A2: Water             $0.75", bg=COLOR_BG, fg=ACCENT, anchor="w").grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
Label(button_frame, text="B1: Chocolate bar     $2.00", bg=COLOR_BG, fg=ACCENT, anchor="w").grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
Label(button_frame, text="B2: Chips             $1.25", bg=COLOR_BG, fg=ACCENT, anchor="w").grid(row=3, column=0, columnspan=2, sticky="w", padx=10)

Label(button_frame, text="", bg=COLOR_BG).grid(row=4, column=0)

# Letter selection buttons
button_a = Button(button_frame, text="A", width=4, command=lambda: press_letter("A"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_a.grid(row=5, column=0, padx=5, pady=3)

button_b = Button(button_frame, text="B", width=4, command=lambda: press_letter("B"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_b.grid(row=5, column=1, padx=5, pady=3)

# Number selection buttons
button_1 = Button(button_frame, text="1", width=4, command=lambda: press_number("1"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_1.grid(row=6, column=0, padx=5, pady=3)

button_2 = Button(button_frame, text="2", width=4, command=lambda: press_number("2"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_2.grid(row=6, column=1, padx=5, pady=3)

button_confirm = Button(button_frame, text="Insert Money", command=entry_purchase_item,
                        bg=BUTTON_CALC_BG, fg=BUTTON_FG)
button_confirm.grid(row=7, column=0, padx=5, pady=5)

# Displays current code being entered (e.g. "A_" then "A1")
label_code = Label(button_frame, text="--", bg=ENTRY_BG, fg=ACCENT,
                   font=("Arial", 14, "bold"), width=4, relief="sunken")
label_code.grid(row=7, column=1, padx=5, pady=5)

label_output = Label(window, text="Please insert money to begin.", bg=OUTPUT_BG, fg=ACCENT,
                     wraplength=400, justify=CENTER)
label_output.pack(pady=10, fill=BOTH, expand=True)

window.mainloop()
