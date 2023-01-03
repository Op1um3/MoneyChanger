"""TODO : Do better comments for the combobox section, put everything in black and add a good interface and round widget
. Being able to import other curencies and cryptocurencies to exchange.
use fixer for api and not exchangerate.
FINISH THE THEME"""
import tkinter
import customtkinter
import requests

def convert():
  # get the amount to convert
  amount = entry.get()
  # check if the amount is a number
  if amount.isdigit():
    # get the starting and destination currencies
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    # check if the currency codes are valid
    if from_currency in ["USD", "EUR", "CAD", "GBP"] and to_currency in ["USD", "EUR", "CAD", "GBP"]:
      # send a request to the currency conversion API to get the conversion rate
      response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
      data = response.json()
      rate = data["rates"][to_currency]

      # convert the amount and display the result
      result = round(float(amount) * rate)
      result_label.configure(text=f"{amount} {from_currency} = {result} {to_currency}")
      print("Your amount is " + str(result))
    # if the user enter a wrong curren it will display a text
    else:
      wrong_currency = customtkinter.CTkLabel(master=root, text="Please enter a valid currency",bg_color="#2A2728",fg_color="white", width=120, height=25
    , corner_radius=8)
      wrong_currency.pack()
      root.after(1250, wrong_currency.destroy)
  # if the user enter a wrong amount it will display a text
  else:
    wrong_amount = customtkinter.CTkLabel(master=root, text='Please enter a valid amount',bg_color="#2A2728",fg_color="white", width=120, height=25
    , corner_radius=8)
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
# main window backroud
# create the widgets 
from_combo = customtkinter.CTkComboBox(master=root, values = ["USD", "EUR", "CAD", "GBP"])

# complete explication at end of script
to_combo = customtkinter.CTkComboBox(master=root, values = ["USD", "EUR", "CAD", "GBP"])

# the conversion button
entry = customtkinter.CTkEntry(master=root)
convert_button = customtkinter.CTkButton(master=root, text="Convert", command=convert)
result_label = customtkinter.CTkLabel(master=root, bg_color="#2A2728", fg_color="white",corner_radius=8)
# add the widgets to the window
from_combo.pack(padx=20, pady=20)
to_combo.pack(padx=18, pady=18)
entry.pack(padx=15, pady=15)
convert_button.pack(padx=10, pady=10)
result_label.pack(padx=5, pady=5)

# run the Tkinter main loop
root.mainloop()  
"""A complete overview of the code : This code is written in Python and uses the tkinter library to create a simple graphical user interface (GUI) for a currency converter.Also have
The GUI has two dropdown menus (using the ttk.Combobox widget) to select the currency to convert from and the currency to convert to, and an Entry widget to enter the amount to convert.
There is also a Button widget with the text "Convert" and a Label widget to display the result of the conversion.
When the user clicks the "Convertir" button, the convert function is called.
This function gets the amount to convert from the Entry widget, and the selected currencies from the two Combobox widgets.
It then sends a request to the "Exchange Rate API" (using the requests library) to get the exchange rate between the two currencies.
The function then calculates the result of the conversion and updates the text of the Label widget with the result.
Finally, the mainloop function is called, which waits for events (such as button clicks) and processes them until the user closes the window.

 Other specification : from_currency and to_currency are variables that store the selected currency codes from the from_combo and to_combo comboboxes, respectively. 
 The get method is a method of the Combobox widget that returns the currently selected value in the combobox.
In this script, the from_combo and to_combo comboboxes allow the user to select the currency they want to convert from and the currency they want to convert to, respectively. 
The selected currency codes are stored in the from_currency and to_currency variables, and are used in the API request to get the conversion rate.
For example, if the user selects "USD" in the from_combo combobox and "EUR" in the to_combo combobox, 
the from_currency variable will be set to "USD" and the to_currency variable will be set to "EUR".
The isdigit() method is a built-in method in Python that returns True if a string contains only digits (0-9) and False if it contains any other characters."""