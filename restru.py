import tkinter as tk 
from tkinter import ttk,messagebox

class Resturantordermanagement:
    def __init__(self,root):
        self.root=root
        self.root.title("Restaurant management app")
        
        
        self.menu_items={
            "Fries meal" : 2,
            "Lunch meal" : 2,
            "Burger meal" : 3,
            "Pizza meal" : 4,
            "Cheese burger" : 2.5,
            "Drinks" : 1
        }
        
        frame=ttk.Frame(root)
        frame.pack(expand=True,padx=20,pady=20)
        
        ttk.Label(frame,
                  text="Resturant order management",
                  font=("Arial",16,"bold")).grid(row=0,
                                                 columnspan=2,
                                                 padx=10,
                                                 pady=10)
                  
                  
        self.quantity_entries = {}

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            ttk.Label(frame,
                    text=f"{item} (${price}):",
                    font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5, sticky="w")

            
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5, sticky="e")
            quantity_entry.insert(0, "0")

            self.quantity_entries[item] = quantity_entry
            
            
        # Order button
        ttk.Button(frame,
                    text="Place Order",
                    command=self.place_order).grid(row=len(self.menu_items)+1,
                                                columnspan=2,
                                                pady=20)

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"

        for item, entry in self.quantity_entries.items():

        try:
            quantity = int(entry.get())
            if quantity < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", f"Invalid quantity for {item}")
            return

        price = self.menu_items[item]
        if quantity > 0:
            cost = quantity * price
            total_cost += cost
            order_summary += f"{item}: {quantity} x ${price} = ${cost:.2f}\n"

    if total_cost > 0:
        order_summary += f"\nTotal Cost: ${total_cost:.2f}"
        messagebox.showinfo("Order Placed", order_summary)

    else:

        messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":

    root = tk.Tk()

app = RestaurantOrderManagement(root)

root.geometry("500x500")

root.mainloop()    
          
        