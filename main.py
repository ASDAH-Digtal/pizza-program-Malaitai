import tkinter as tk
from tkinter import ttk

def show_price(pizza):
    if var_1.get() in regular_pizzas:
        price_1.config(text="$8.50")
    if var_2.get() in regular_pizzas:
        price_2.config(text="$8.50")
    if var_3.get() in regular_pizzas:
        price_3.config(text="$8.50")
    if var_4.get() in regular_pizzas:
        price_4.config(text="$8.50")
    if var_5.get() in regular_pizzas:
        price_5.config(text="$8.50")

    if var_1.get() in gourmet_pizzas:
        price_1.config(text="$13.50")
    if var_2.get() in gourmet_pizzas:
        price_2.config(text="$13.50")
    if var_3.get() in gourmet_pizzas:
        price_3.config(text="$13.50")
    if var_4.get() in gourmet_pizzas:
        price_4.config(text="$13.50")
    if var_5.get() in gourmet_pizzas:
        price_5.config(text="$13.50")

default = ["Select a doughnut"]
regular_pizzas = ["Glazed", "Cinamon", "Strawberry Sprinkles", "Strawberry Jam", "Chocolate Sprinkles", "Caramel", "Vanilla", "Chocolate Cheesecake"]
gourmet_pizzas = ["Ice Cream", "Tiramisu", "Fudge Brownie", "Cookies and Cream"]
all_pizzas = default + regular_pizzas + gourmet_pizzas

root = tk.Tk()

root.title("Doughnut Ordering System")

var_1 = tk.StringVar(root)
var_1.set("Select a doughnut")
var_2 = tk.StringVar(root)
var_2.set("Select a doughnut")
var_3 = tk.StringVar(root)
var_3.set("Select a doughnut")
var_4 = tk.StringVar(root)
var_4.set("Select a doughnut")
var_5 = tk.StringVar(root)
var_5.set("Select a doughnut")

title = ttk.Label(root, text="Doughnut Ordering System", font=("Arial", 25))
title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

regular_title = ttk.Label(root, text="Regular: $8.50", font=("Arial", 15))
regular_title.grid(row=1, column=0, padx=10, pady=10)

gourmet_title = ttk.Label(root, text="Gourmet $13.50", font=("Arial", 15))
gourmet_title.grid(row=1, column=1, padx=10, pady=10)

regular_menu = ttk.Label(root, text="Glazed\nCinnamon\nStrawyberry Sprinkles\nStrawberry Jam\nChocolate Sprinkles\nCaramel\nVanilla\nChocolate Cheesecake")
regular_menu.grid(row=2, column=0, sticky=tk.N, pady=20)

gourmet_menu = ttk.Label(root, text="Ice Cream\nTiramisu\nFudge Brownie\nCookies and Cream")
gourmet_menu.grid(row=2, column=1, sticky=tk.N, pady=20)

option_1 = ttk.OptionMenu(root, var_1, *all_pizzas, command=show_price)
option_1.grid(row=3, column=0, sticky=tk.E, pady=10)

price_1 = ttk.Label(root, text="$0.00")
price_1.grid(row=3, column=1)

option_2 = ttk.OptionMenu(root, var_2, *all_pizzas, command=show_price)
option_2.grid(row=4, column=0, sticky=tk.E, pady=10)

price_2 = ttk.Label(root, text="$0.00")
price_2.grid(row=4, column=1)

option_3 = ttk.OptionMenu(root, var_3, *all_pizzas, command=show_price)
option_3.grid(row=5, column=0, sticky=tk.E, pady=10)

price_3 = ttk.Label(root, text="$0.00")
price_3.grid(row=5, column=1)

option_4 = ttk.OptionMenu(root, var_4, *all_pizzas, command=show_price)
option_4.grid(row=6, column=0, sticky=tk.E, pady=10)

price_4 = ttk.Label(root, text="$0.00")
price_4.grid(row=6, column=1)

option_5 = ttk.OptionMenu(root, var_5, *all_pizzas, command=show_price)
option_5.grid(row=7, column=0, sticky=tk.E, pady=10)

price_5 = ttk.Label(root, text="$0.00")
price_5.grid(row=7, column=1)

root.mainloop()