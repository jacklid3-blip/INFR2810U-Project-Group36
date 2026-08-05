# Author: Jack Lidster
# Date: 2026-08-03
# Description: 
# This program uses code to show how a vending machine works. 
# It will take in a user input of money and then allow the user to select a product. 
# The program will then calculate the change and display it to the user.
from tkinter import Tk, Label, Entry, Frame, Button, BOTH, CENTER

WINDOW_WIDTH = 425
WINDOW_HEIGHT = 225
WINDOW_MIN_WIDTH = 425
WINDOW_MIN_HEIGHT = 225

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

def entry_money_func():
    try:
        money = float(entry_money.get())
        if money < 0.25 or money > 20.00:
            label_output.configure(text="Error: money must be between $0.25 and $20.00.",
                                   fg="#b30000", bg="#ffe6e6")
            entry_money.focus()
            return
        else:
            label_output.configure(text=f"You have inserted ${money:.2f}. Please select a product.",
                                   fg=ACCENT, bg=OUTPUT_BG)
    except ValueError:
        label_output.configure(text="Error: please enter a valid amount of money.",
                               fg="#b30000", bg="#ffe6e6")
        entry_money.focus()

def select_product(product_price):
    try:
        money = float(entry_money.get())
        if money < product_price:
            label_output.configure(text=f"Error: insufficient funds. Product costs ${product_price:.2f}.",
                                   fg="#b30000", bg="#ffe6e6")
            return
        change = money - product_price
        label_output.configure(text="Dispensing product...", fg=ACCENT, bg=OUTPUT_BG)
        window.after(2000, lambda: (
            label_output.configure(text=f"Product dispensed! Enjoy! Your change is ${change:.2f}", fg=ACCENT, bg=OUTPUT_BG),
        ))
        entry_money.delete(0, 'end')
        entry_money.insert(0, f"{change:.2f}")
    except ValueError:
        label_output.configure(text="Error: please insert money first.",
                               fg="#b30000", bg="#ffe6e6")

button_frame = Frame(window, bg=COLOR_BG)
button_frame.pack(pady=10)

button_confirm = Button(button_frame, text="Confirm Money", command=entry_money_func, 
                        bg=BUTTON_CALC_BG, fg=BUTTON_FG)
button_confirm.grid(row=0, column=0, padx=5)

button_coke = Button(button_frame, text="Coke ($1.50)", command=lambda: select_product(1.50),
                     bg=ACCENT, fg=BUTTON_FG)
button_coke.grid(row=0, column=1, padx=5)

button_water = Button(button_frame, text="Water ($0.75)", command=lambda: select_product(0.75),
                      bg=ACCENT, fg=BUTTON_FG)
button_water.grid(row=0, column=2, padx=5)

button_snack = Button(button_frame, text="Chocolate bar($2.00)", command=lambda: select_product(2.00),
                      bg=ACCENT, fg=BUTTON_FG)
button_snack.grid(row=0, column=3, padx=5)

button_chips = Button(button_frame, text="Chips ($1.25)", command=lambda: select_product(1.25),
                      bg=ACCENT, fg=BUTTON_FG)
button_chips.grid(row=0, column=3, padx=5)

label_output = Label(window, text="Please insert money to begin.", bg=OUTPUT_BG, fg=ACCENT,
                     wraplength=400, justify=CENTER)
label_output.pack(pady=10, fill=BOTH, expand=True)

window.mainloop()
