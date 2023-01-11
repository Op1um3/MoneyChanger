"""TODO : Do better comments for the combobox section,
. Being able to import other curencies and cryptocurencies to exchange. Put a graphic api
Do a placeholder that react, replace the icon of the window, add polygon"""
import tkinter
import customtkinter
import requests

# global declaration for the wrong_amount_after_id and wrong_currency_after_id variables to make them accessible inside the convert function:
wrong_amount_displayed = False
wrong_currency_displayed = False

# available currencies list:
currencies = ["USD", "EUR", "CAD", "GBP","JPY",""]

wrong_amount_displayed = False
wrong_currency_displayed = False

def convert():
  global wrong_amount_displayed
  global wrong_currency_displayed
  wrong_amount_displayed = False
  wrong_currency_displayed = False
  
  # delete all labels
  for widget in root.winfo_children():
    if isinstance(widget, customtkinter.CTkLabel):
      widget.destroy()
  
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
      result = round(float(amount) * rate, 2)
      result_label = customtkinter.CTkLabel(master=root,fg_color="#191919", width=140, height=30, corner_radius=7)
      result_label.place(relx=0.03, rely=0.90, anchor='w')
      result_label.configure(text=f"{amount} {from_currency} = {result} {to_currency}")
    else:
      if not wrong_currency_displayed:
        wrong_currency = customtkinter.CTkLabel(master=root, text="Enter a valid currency",
                                                bg_color="#2A2728",fg_color="#a30016", width=120, height=30 ,corner_radius=8)
        wrong_currency.place(relx=0.03, rely=0.90, anchor='w')
        wrong_currency_displayed = True
        try:
          root.after_cancel(wrong_currency_after_id)
        except NameError:
          pass
        wrong_currency_after_id = root.after(3000, wrong_currency.destroy)
  else:
    if not wrong_amount_displayed:
      wrong_amount = customtkinter.CTkLabel(master=root, text='Enter a valid amount',
                                            bg_color="#2A2728",fg_color="#a30016", width=140, height=30, corner_radius=8)
      wrong_amount.place(relx=0.03, rely=0.90, anchor='w')
      wrong_amount_displayed = True
      try:
        root.after_cancel(wrong_amount_after_id)
      except NameError:
        pass
      wrong_amount_after_id = root.after(3000, wrong_amount.destroy)

# create the main window
root = customtkinter.CTk()
root.title("Currency Converter")

# The root theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# main window size
root.geometry("600x300")
root.minsize(600,300)
root.maxsize(600,300)

# create the widgets 
from_combo = customtkinter.CTkComboBox(master=root, values = currencies)

# complete explanation at end of script
to_combo = customtkinter.CTkComboBox(master=root, values = currencies)

# the conversion button (calls the conversion function when clicked)
from_currency = from_combo.get() 
print(from_currency)
entry = customtkinter.CTkEntry(master=root, placeholder_text='   Enter your amount' ,
                               width=140, height=30, corner_radius=8)
convert_button = customtkinter.CTkButton(master=root, text="Convert", command=convert, 
                                         width=140, height=30, corner_radius=8)

# add the widgets to the window
rel_x = 0.03
from_combo.place(relx = rel_x, rely=0.10, anchor='w')
to_combo.place(relx = rel_x, rely=0.30, anchor='w')
entry.place(relx = rel_x, rely=0.50, anchor='w') 
convert_button.place(relx = rel_x, rely=0.70, anchor='w')

# run the Tkinter main loop
root.mainloop()