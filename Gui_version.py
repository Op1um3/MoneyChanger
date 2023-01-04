"""TODO : Do better comments for the combobox section,
. Being able to import other curencies and cryptocurencies to exchange.
use fixer for api and not exchangerate. Put a graphic
FINIR LE PLACE HOLDER"""
import tkinter
import customtkinter
import requests

# available currencies list:
currencies = ["USD", "EUR", "CAD", "GBP","JPY"]

def convert():
  # get the amount to convert
  amount = entry.get()
  # check if the amount is a number
  if amount.isdigit():
    # get the starting and destination currencies
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    # check if the currency codes are valid
    if from_currency in currencies and to_currency in currencies:
      # send a request to the currency conversion API to get the conversion rate
      response = requests.get(f"https://v6.exchangerate-api.com/v6/40978df5c0d54eb0375143c7/latest/{from_currency}")
      data = response.json()
      rate = data["conversion_rates"][to_currency]

      # convert the amount and display the result
      # the following 3 lines delete all labels
      for widget in root.winfo_children():
        if isinstance(widget, customtkinter.CTkLabel):
          widget.destroy()
      result_label = customtkinter.CTkLabel(master=root, bg_color="#2A2728", fg_color="#1a1617",corner_radius=8)
      result_label.pack(padx=5, pady=5)
      result = round(float(amount) * rate)
      result_label.configure(text=f"{amount} {from_currency} = {result} {to_currency}")
      print("Your amount is " + str(result))
    # if the user enter a wrong curren it will display a text
    else:
      wrong_currency = customtkinter.CTkLabel(master=root, text="Please enter a valid currency",bg_color="#2A2728",fg_color="#a30016", width=120, height=25 ,corner_radius=8)
      wrong_currency.pack()
      root.after(1250, wrong_currency.destroy)
  # if the user enter a wrong amount it will display a text
  else:
    wrong_amount = customtkinter.CTkLabel(master=root, text='Please enter a valid amount',bg_color="#2A2728",fg_color="#a30016", width=120, height=25, corner_radius=8)
    wrong_amount.pack()
    root.after(1250, wrong_amount.destroy)
    
# create the main window
root = customtkinter.CTk()
root.title("Currency Converter")

# The root theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# main window size
root.geometry("600x500")

# create the widgets 
from_combo = customtkinter.CTkComboBox(master=root, values = currencies)

# complete explanation at end of script
to_combo = customtkinter.CTkComboBox(master=root, values = currencies)

# the conversion button (calls the conversion function when clicked)
entry = customtkinter.CTkEntry(master=root, placeholder_text="enter your amount of ", width=100, height=30, corner_radius=10)
convert_button = customtkinter.CTkButton(master=root, text="Convert", command=convert)

# add the widgets to the window
from_combo.pack(padx=20, pady=20)
to_combo.pack(padx=18, pady=18)
entry.place(relx=0.1, rely=0.5, anchor='n')
convert_button.pack(padx=10, pady=10)

# run the Tkinter main loop
root.mainloop()