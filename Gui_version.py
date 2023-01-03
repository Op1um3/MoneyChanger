"""TODO : Do better comments for the combobox section, put everything in black and add a good interface and round widget
. Being able to import other curencies and cryptocurencies to exchange.
use fixer for api and not exchangerate."""
import tkinter as tk
import tkinter.ttk as ttk
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
      result_label.config(text=f"{amount} {from_currency} = {result} {to_currency}")
      print("Your amount is " + str(result))
    # if the user enter a wrong curren it will display a text
    else:
      wrong_currency = tk.Label(root,text="Please enter a valid currency")
      wrong_currency.pack()
      root.after(1500, wrong_currency.destroy)
  # if the user enter a wrong amount it will display a text
  else:
    wrong_amount = tk.Label(root, text='Please enter a valid amount')
    wrong_amount.pack()
    root.after(1500, wrong_amount.destroy)
# create the main window
root = tk.Tk()
root.title("Currency Converter")
# main window size
root.geometry("250x250")
# main window backroud
root.configure(bg="#2A2728")
# create the widgets 
from_combo = tk.ttk.Combobox(root)
from_combo["values"] = ("USD", "EUR", "CAD", "GBP")
from_combo.current(0)
# complete explication at end of script
to_combo = ttk.Combobox(root)
to_combo["values"] = ("USD", "EUR", "CAD", "GBP")
to_combo.current(1)
# the conversion button
entry = tk.Entry(root)
convert_button = tk.Button(root, text="Convert", command=convert)
result_label = tk.Label(root, bg="#2A2728", fg="white")
# add the widgets to the window
from_combo.pack()
to_combo.pack()
entry.pack()
convert_button.pack()
result_label.pack()

# run the Tkinter main loop
root.mainloop()  
"""A complete overview of the code : This code is written in Python and uses the tkinter library to create a simple graphical user interface (GUI) for a currency converter.
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