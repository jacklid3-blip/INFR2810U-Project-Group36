# Author: Jack Lidster
# Date: 2026-08-03
# Description: 
# This program uses code to show how a vending machine works. 
# It will take in a user input of money and then allow the user to select a product. 
# The program will then calculate the change and display it to the user.
from tkinter import Tk, Label, Entry, Frame, Button, StringVar, BOTH, CENTER

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 680
WINDOW_MIN_WIDTH = 420
WINDOW_MIN_HEIGHT = 680

# Color palette
COLOR_BG = "#eef2f7"       # window background
PANEL_BG = "#ffffff"       # card-like panel background
ACCENT = "#1f3a5f"         # primary text color
MUTED = "#5b6d85"          # secondary text color
ENTRY_BG = "#f8fafc"       # input background
ENTRY_BORDER = "#c9d5e5"   # input border highlight
BUTTON_CALC_BG = "#2f7d32" # green for insert action
BUTTON_RESET_BG = "#dc3545"# red
BUTTON_FG = "#ffffff"      # white text on buttons
OUTPUT_BG = "#f8fbff"      # output area background

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_HEADING = ("Segoe UI", 11, "bold")
FONT_BODY = ("Segoe UI", 10)
FONT_BUTTON = ("Segoe UI", 10, "bold")

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
window.resizable(False, False)

window.title("Vending Machine")
window.configure(bg=COLOR_BG)

Label(window, text="Vending Machine", bg=COLOR_BG, fg=ACCENT,
    font=FONT_TITLE).pack(pady=(14, 4))
Label(window, text="Insert money, choose a code, and collect change.",
    bg=COLOR_BG, fg=MUTED, font=FONT_BODY).pack(pady=(0, 10))

# Create GUI elements
label_money = Label(window, text="Insert money ($):", bg=COLOR_BG, fg=ACCENT,
                    font=FONT_HEADING)
label_money.pack(pady=(4, 4))

entry_money = Entry(window, bg=ENTRY_BG, fg=ACCENT, font=("Segoe UI", 12),
                    relief="solid", bd=1, highlightthickness=1,
                    highlightbackground=ENTRY_BORDER, highlightcolor=ACCENT,
                    justify="center")
entry_money.pack(pady=(0, 8), ipadx=6, ipady=4)

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

frame_insert = Frame(window, bg=PANEL_BG, bd=1, relief="solid")
frame_insert.pack(pady=4, padx=18, fill="x")

button_confirm = Button(frame_insert, text="Insert Money", command=entry_purchase_item,
                bg=BUTTON_CALC_BG, fg=BUTTON_FG, font=FONT_BUTTON,
                activebackground="#256628", activeforeground=BUTTON_FG,
                relief="flat", cursor="hand2", padx=10, pady=6)
button_confirm.grid(row=0, column=0, padx=8, pady=8)

label_balance = Label(frame_insert, text="Balance: $0.00", bg=ENTRY_BG, fg=ACCENT,
                font=("Segoe UI", 11, "bold"), relief="solid", bd=1,
                width=14, padx=6, pady=4)
label_balance.grid(row=0, column=1, padx=8, pady=8)

stock_frame = Frame(window, bg=PANEL_BG, bd=1, relief="solid")
stock_frame.pack(pady=6, padx=18, fill="x")
Label(stock_frame, text="Stock", bg=PANEL_BG, fg=ACCENT,
    font=FONT_HEADING).pack(pady=(8, 2))

for code, (name, price) in PRODUCTS.items():
    label_stock = Label(stock_frame, text=f"{name}: {format_stock_display(code)}",
                bg=PANEL_BG, fg=ACCENT, justify=CENTER,
                wraplength=320, font=FONT_BODY)
    label_stock.pack(pady=2)
    stock_labels[code] = label_stock

button_frame = Frame(window, bg=PANEL_BG, bd=1, relief="solid")
button_frame.pack(pady=6, padx=18, fill="x")

Label(button_frame, text="Select Product", bg=PANEL_BG, fg=ACCENT,
    font=FONT_HEADING).grid(row=0, column=0, columnspan=2, pady=(8, 2))

# Letter selection buttons
button_a = Button(button_frame, text="A", width=5, command=lambda: press_letter("A"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Segoe UI", 12, "bold"),
                  activebackground="#2b4b77", activeforeground=BUTTON_FG,
                  relief="flat", cursor="hand2")
button_a.grid(row=1, column=0, padx=8, pady=4)

button_b = Button(button_frame, text="B", width=5, command=lambda: press_letter("B"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Segoe UI", 12, "bold"),
                  activebackground="#2b4b77", activeforeground=BUTTON_FG,
                  relief="flat", cursor="hand2")
button_b.grid(row=1, column=1, padx=8, pady=4)

# Number selection buttons
button_1 = Button(button_frame, text="1", width=5, command=lambda: press_number("1"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Segoe UI", 12, "bold"),
                  activebackground="#2b4b77", activeforeground=BUTTON_FG,
                  relief="flat", cursor="hand2")
button_1.grid(row=2, column=0, padx=8, pady=4)

button_2 = Button(button_frame, text="2", width=5, command=lambda: press_number("2"),
                  bg=ACCENT, fg=BUTTON_FG, font=("Segoe UI", 12, "bold"),
                  activebackground="#2b4b77", activeforeground=BUTTON_FG,
                  relief="flat", cursor="hand2")
button_2.grid(row=2, column=1, padx=8, pady=4)

# Displays current code being entered (e.g. "A_" then "A1")
label_code = Label(button_frame, text="--", bg=ENTRY_BG, fg=ACCENT,
             font=("Segoe UI", 14, "bold"), width=6,
             relief="solid", bd=1, pady=2)
label_code.grid(row=3, column=0, columnspan=2, pady=(6, 10))

frame_change = Frame(window, bg=PANEL_BG, bd=1, relief="solid")
frame_change.pack(pady=6, padx=18, fill="x")

Label(frame_change, text="Change:", bg=PANEL_BG, fg=ACCENT,
    font=FONT_HEADING).grid(row=0, column=0, padx=8, pady=8)
change_var = StringVar(value="$0.00")
entry_change = Entry(frame_change, textvariable=change_var, state="readonly",
               bg=ENTRY_BG, fg=ACCENT, font=("Segoe UI", 11, "bold"),
               width=10, relief="solid", bd=1, readonlybackground=ENTRY_BG,
               justify="center")
entry_change.grid(row=0, column=1, padx=8, pady=8)

label_output = Label(window, text="Please insert money to begin.", bg=OUTPUT_BG, fg=ACCENT,
               wraplength=360, justify=CENTER, font=FONT_BODY,
               relief="solid", bd=1, padx=12, pady=12)
label_output.pack(pady=(8, 14), padx=18, fill=BOTH, expand=True)

window.mainloop()
