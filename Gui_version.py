"""TODO : Do better comments for the combobox section,
. Being able to import other curencies and cryptocurencies to exchange. Put a graphic api
Do a placeholder that react, replace the icon of the window, add polygon"""
import tkinter
import customtkinter
import requests

CURRENCIES = ["USD", "EUR", "CAD", "GBP","JPY"] # available currencies list

def is_number(s: str) -> bool:
  """
  Checks if a string is a number (for instance '69.01', '0.42' or '1').

  Args:
      s (str): the string to check
  """
  s_no_dot = s.replace(".", "", 1) # this is an integer iff s is a correct number
  return s_no_dot.isdigit()

def delete_labels(window: tkinter.Tk) -> None:
  """
  Remove all labels that are in a window.
  
  Args:
      window: a Tk instance associated with the window in wich the labels are.
  """
  for widget in window.winfo_children(): # delete all labels in the window
    if isinstance(widget, customtkinter.CTkLabel):
      widget.destroy()
      
def get_exchange_rate(from_currency: str, to_currency: str) -> float:
  """
  Gets the exchange rate between from_currency to to_currency from the https://www.exchangerate-api.com

  Args:
      from_currency (str): start currency
      to_currency (str): target currency

  Returns:
      float: x where 1 from_currency = x to_currency
  """
  response = requests.get(f"https://v6.exchangerate-api.com/v6/40978df5c0d54eb0375143c7/latest/{from_currency}")
  data = response.json()
  return data["conversion_rates"][to_currency]
def convert():
  """
  TODO: write docstring for this function
  """
  delete_labels(root)
  amount = entry.get()
  if is_number(amount):
    amount = float(amount)
    from_currency, to_currency = from_combo.get(), to_combo.get()
    if from_currency in CURRENCIES and to_currency in CURRENCIES:
      rate = get_exchange_rate(from_currency, to_currency)
      result = float(amount) * rate
      
      # Check if wrong_amount_displayed or wrong_currency_displayed exists and destroy it
      for widget in root.winfo_children():
        if widget.cget("text") == "Enter a valid currency" or widget.cget("text") == "Enter a valid amount":
            widget.destroy()
            
      # next three lines display the result using a new label instance
      result_label = customtkinter.CTkLabel(master=root, fg_color="#191919",
                                            width=140, height=30, corner_radius=7)
      result_label.place(relx=0.5, rely=0.90, anchor='s')
      result_label.configure(text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
    else: # case where a currency is invalid
      wrong_currency = customtkinter.CTkLabel(master=root, text="Enter a valid currency",
                                              bg_color="#2A2728", fg_color="#a30016",
                                              width=120, height=30 ,corner_radius=8)
      wrong_currency.place(relx=0.15, rely=0.90, anchor='w')
      root.after(3000, wrong_currency.destroy)
  else: # case where the amount is invalid
      wrong_amount = customtkinter.CTkLabel(master=root, text='Enter a valid amount',
                                            bg_color="#2A2728", fg_color="#a30016",
                                            width=140, height=30, corner_radius=8)
      wrong_amount.place(relx=0.15, rely=0.90, anchor='w')
      root.after(3000, wrong_amount.destroy)

# create the main window
root = customtkinter.CTk()
root.title("")

# The root theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# main window size
root.geometry("600x300")
root.minsize(200,300)
root.maxsize(200,300)

# create the widgets 
from_combo = customtkinter.CTkComboBox(master=root, values = CURRENCIES)

# complete explanation at end of script
to_combo = customtkinter.CTkComboBox(master=root, values = CURRENCIES)

# the conversion button (calls the conversion function when clicked)
from_currency = from_combo.get() 
print(from_currency)
entry = customtkinter.CTkEntry(master=root,
                               placeholder_text='Enter your amount', justify="center",
                               width=140, height=30, corner_radius=8)
convert_button = customtkinter.CTkButton(master=root, text="Convert", command=convert, 
                                         width=140, height=30, corner_radius=8)

# add the widgets to the window
rel_x = 0.15
from_combo.place(relx = rel_x, rely=0.10, anchor='w')
to_combo.place(relx = rel_x, rely=0.30, anchor='w')
entry.place(relx = rel_x, rely=0.50, anchor='w') 
convert_button.place(relx = rel_x, rely=0.70, anchor='w')

# run the Tkinter main loop
root.mainloop()