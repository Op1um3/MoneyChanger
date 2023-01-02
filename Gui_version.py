import tkinter as tk
import tkinter.ttk as ttk
import requests

def convert():
  # obtenir le montant à convertir
  amount = entry.get()

  # obtenir la devise de départ et la devise de destination
  from_currency = from_combo.get()
  to_currency = to_combo.get()

  # envoyer une demande à l'API de conversion de devises pour obtenir le taux de conversion
  response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
  data = response.json()
  rate = data["rates"][to_currency]

  # convertir le montant et afficher le résultat
  result = float(amount) * rate
  result_label.config(text=f"{amount} {from_currency} = {result} {to_currency}")

# créer la fenêtre principale
root = tk.Tk()
root.title("Convertisseur de devises")

# créer les widgets
from_combo = tk.ttk.Combobox(root)
from_combo["values"] = ("USD", "EUR", "CAD", "GBP")
from_combo.current(0)

to_combo = ttk.Combobox(root)
to_combo["values"] = ("USD", "EUR", "CAD", "GBP")
to_combo.current(1)

entry = tk.Entry(root)
convert_button = tk.Button(root, text="Convertir", command=convert)
result_label = tk.Label(root)

# ajouter les widgets à la fenêtre
from_combo.pack()
to_combo.pack()
entry.pack()
convert_button.pack()
result_label.pack()

# exécuter la boucle principale de Tkinter
root.mainloop()
  
  


