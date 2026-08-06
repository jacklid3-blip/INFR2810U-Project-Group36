# Author: Jack Lidster
# Date: 2026-08-03
# Description: 
# This program uses code to show how a vending machine works. 
# It will take in a user input of money and then allow the user to select a product. 
# The program will then calculate the change and display it to the user.
from tkinter import Tk, Label, Entry, Frame, Button, StringVar, BOTH, CENTER

WINDOW_WIDTH = 350
WINDOW_HEIGHT = 475
WINDOW_MIN_WIDTH = 350
WINDOW_MIN_HEIGHT = 475

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
    "A1": ("Soda", 1.50),
    "A2": ("Water", 0.75),
    "B1": ("Candy", 2.00),
    "B2": ("Pretzels", 1.25),
}
INITIAL_STOCK = 10
PRODUCT_ICONS = {
    "A1": "🥤",
    "A2": "💧",
    "B1": "🍬",
    "B2": "🥨",
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
balance = 0.0
inventory = {code: INITIAL_STOCK for code in PRODUCTS}
stock_labels = {}

def entry_purchase_item():
    global balance
    try:
        amount = float(entry_money.get())
    except ValueError:
        label_output.configure(text="Error: enter a valid amount.",
                               fg="#b30000", bg="#ffe6e6")
        return
    if amount <= 0:
        label_output.configure(text="Error: amount must be greater than $0.00.",
                               fg="#b30000", bg="#ffe6e6")
        return
    balance += amount
    label_balance.configure(text=f"Balance: ${balance:.2f}")
    entry_money.delete(0, 'end')
    label_output.configure(text=f"${amount:.2f} inserted. Balance: ${balance:.2f}.", fg=ACCENT, bg=OUTPUT_BG)

def format_stock_display(code):
    stock = inventory[code]
    icon = PRODUCT_ICONS[code]
    return f"{icon * stock} ({stock} left)"


def update_stock_display():
    for code, label in stock_labels.items():
        label.configure(text=f"{PRODUCTS[code][0]}: {format_stock_display(code)}")


def select_product(code, name, price):
    global balance
    if inventory[code] <= 0:
        label_output.configure(text=f"{code}: {name} is sold out.",
                               fg="#b30000", bg="#ffe6e6")
        label_code.configure(text="--")
        return
    if balance <= 0:
        label_output.configure(text=f"{code}: {name} - ${price:.2f}",
                               fg=ACCENT, bg=OUTPUT_BG)
        label_code.configure(text="--")
        return
    if balance < price:
        label_output.configure(text=f"Error: insufficient funds. {name} costs ${price:.2f}.",
                               fg="#b30000", bg="#ffe6e6")
        label_code.configure(text="--")
        return
    change = balance - price
    balance = 0.0
    inventory[code] -= 1
    update_stock_display()
    label_balance.configure(text="Balance: $0.00")
    change_var.set(f"${change:.2f}")
    label_output.configure(text="Dispensing product...", fg=ACCENT, bg=OUTPUT_BG)
    window.after(2000, lambda: (
        label_output.configure(text=f"Product dispensed! Enjoy your {name}!", fg=ACCENT, bg=OUTPUT_BG),
    ))
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

frame_insert = Frame(window, bg=COLOR_BG)
frame_insert.pack(pady=3)

button_confirm = Button(frame_insert, text="Insert Money", command=entry_purchase_item,
                        bg=BUTTON_CALC_BG, fg=BUTTON_FG)
button_confirm.grid(row=0, column=0, padx=5)

label_balance = Label(frame_insert, text="Balance: $0.00", bg=ENTRY_BG, fg=ACCENT,
                      font=("Arial", 11), relief="sunken", width=14)
label_balance.grid(row=0, column=1, padx=5)

stock_frame = Frame(window, bg=COLOR_BG)
stock_frame.pack(pady=5)
Label(stock_frame, text="Stock left", bg=COLOR_BG, fg=ACCENT,
      font=("Arial", 11, "bold")).pack()

for code, (name, price) in PRODUCTS.items():
    label_stock = Label(stock_frame, text=f"{name}: {format_stock_display(code)}",
                        bg=COLOR_BG, fg=ACCENT, justify=CENTER, wraplength=260)
    label_stock.pack(pady=2)
    stock_labels[code] = label_stock

button_frame = Frame(window, bg=COLOR_BG)
button_frame.pack(pady=5)

# Letter selection buttons
button_a = Button(button_frame, text="A", width=4, command=lambda: press_letter("A"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_a.grid(row=0, column=0, padx=5, pady=3)

button_b = Button(button_frame, text="B", width=4, command=lambda: press_letter("B"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_b.grid(row=0, column=1, padx=5, pady=3)

# Number selection buttons
button_1 = Button(button_frame, text="1", width=4, command=lambda: press_number("1"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_1.grid(row=1, column=0, padx=5, pady=3)

button_2 = Button(button_frame, text="2", width=4, command=lambda: press_number("2"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Arial", 12, "bold"))
button_2.grid(row=1, column=1, padx=5, pady=3)

# Displays current code being entered (e.g. "A_" then "A1")
label_code = Label(button_frame, text="--", bg=ENTRY_BG, fg=ACCENT,
                   font=("Arial", 14, "bold"), width=4, relief="sunken")
label_code.grid(row=2, column=0, columnspan=2, pady=5)

frame_change = Frame(window, bg=COLOR_BG)
frame_change.pack(pady=3)

Label(frame_change, text="Change:", bg=COLOR_BG, fg=ACCENT).grid(row=0, column=0, padx=5)
change_var = StringVar(value="$0.00")
entry_change = Entry(frame_change, textvariable=change_var, state="readonly",
                     bg=ENTRY_BG, fg=ACCENT, font=("Arial", 11), width=10)
entry_change.grid(row=0, column=1, padx=5)

label_output = Label(window, text="Please insert money to begin.", bg=OUTPUT_BG, fg=ACCENT,
                     wraplength=400, justify=CENTER)
label_output.pack(pady=10, fill=BOTH, expand=True)

window.mainloop()
