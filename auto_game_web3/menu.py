import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import threading
import requests
from datetime import datetime
import time
import json

# with open('webhooks.json') as f:
#     webhook_urls = json.load(f)
    
with open('webhooks.json') as f:
    webhook_urls = json.load(f)
    account_options = list(webhook_urls.keys())

def switch_to_root(window):
    window.destroy()  # Close the new window
    root.deiconify()  # Bring the root window back into focus

def Submit_button(account, discord_wh):
    if account.strip() == "" or discord_wh.strip() == "":
        messagebox.showerror("Error", "Please fill in both fields.")
    else:
        # Proceed with your desired functionality
        # Read existing data from the JSON file
        with open('webhooks.json', 'r') as f:
            existing_data = json.load(f)
        
        # Update the existing data with the new account and webhook URL pair
        existing_data[account] = discord_wh
        
        # Write the updated data back to the JSON file
        with open('webhooks.json', 'w') as f:
            json.dump(existing_data, f)
        print("Account:", account)
        print("Discord WH:", discord_wh)
        print("Done")

def button1_click():
    new_window = tk.Toplevel()  # Create a new window
    new_window.title("New Interface")

    label0 = tk.Label(new_window, text="")
    label0.grid(row=0, column=0, padx=10, pady=5)

    labelx = tk.Label(new_window, text="Add User")
    labelx.place(x=120, y=5)

    label1 = tk.Label(new_window, text="Account")
    label1.grid(row=1, column=0, padx=10, pady=5)

    label2 = tk.Label(new_window, text="Discord WH")
    label2.grid(row=2, column=0, padx=10, pady=5)

    entry1 = tk.Entry(new_window)
    entry1.grid(row=1, column=1, padx=10, pady=5)

    entry2 = tk.Entry(new_window)
    entry2.grid(row=2, column=1, padx=10, pady=5)

    button1 = tk.Button(new_window, text="Back", command=lambda: switch_to_root(new_window))
    button1.grid(row=3, column=0, padx=10, pady=5)

    button2 = tk.Button(new_window, text="Submit", command=lambda: Submit_button(entry1.get(), entry2.get()))
    button2.grid(row=3, column=1, padx=10, pady=5)

    root.withdraw()  # Hide the root window

def button2_click():
    # def handle_button_click():
    #     pass
    def send_message(webhook_url, message):
        payload = {"content": message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print(f"Message sent successfully: {message}")
    def send_confirmation(webhook_url, account, product, quantity, interval):
        confirmation_message = (
            f"```"
            f"md\n"
            f"> Your task has been confirmed for Account: {account}, Product: {product}, Quantity: {quantity}, in {interval}."
            f"```"
        )
        send_message(webhook_url, confirmation_message)

    def send_delayed_message(webhook_url, account, product, quantity, interval):
        send_confirmation(webhook_url, account, product, quantity, interval)
        interval_seconds = parse_interval(interval)
        time.sleep(interval_seconds)
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = (
            f"```"
            f"fix\n"
            f"Account: {account}\n"
            f"Action Required: Craft {quantity} {product}(s)\n"
            f"Time: {current_time}"
            f"```"
        )
        send_message(webhook_url, message)

    def parse_interval(interval):
        if interval.endswith("s"):
            return int(interval[:-1])
        elif interval.endswith("m"):
            return int(interval[:-1]) * 60
        elif interval.endswith("h"):
            return int(interval[:-1]) * 3600
        else:
            raise ValueError('Invalid interval format. Use "1s" for seconds, "1m" for minutes, and "1h" for hours.')

    def handle_button_click():
        account = account_var.get()
        product = product_entry.get()
        quantity_str = quantity_entry.get()
        interval = interval_entry.get()
    
        # Check if Product is a string
        if not isinstance(product, str):
            print("Product should be a string.")
            label.config(text="Product should be a string.")
            return
    
    # Check if Quantity is an integer
        try:
            quantity = int(quantity_str)
        except ValueError:
            print("Quantity should be an integer.")
            label.config(text="Quantity should be an integer.")
            return
    
    # Check if any field is empty
        if not all([product, quantity_str, interval]):
            empty_fields = [field_name for field_name, value in {"Product": product, "Quantity": quantity_str, "Interval": interval}.items() if not value]
            print(f"The following fields are empty: {', '.join(empty_fields)}")
            label.config(text=f"The following fields are empty: {', '.join(empty_fields)}")
        else:
            # Execute the script in a separate thread
            webhook_url = webhook_urls.get(account)
            if webhook_url:
                t = threading.Thread(target=send_delayed_message, args=(webhook_url, account, product, quantity, interval))
                t.start()
            else:
                print(f"No webhook URL found for account: {account}")
    
    
    
    def clear_fields():
        product_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        interval_entry.delete(0, tk.END)
        label.config(text="")
    
    new_window = tk.Toplevel()  # Create a new window
    new_window.title("Farm")
    
    account_var = tk.StringVar()
    account_label = tk.Label(new_window, text="Account:")
    account_label.grid(row=0, column=0, padx=10, pady=5)
    # account_options = ["fiddler", "asmuth", "four_arms", "benDog"] change it
    account_dropdown = ttk.Combobox(new_window, textvariable=account_var, values=account_options)
    account_dropdown.grid(row=0, column=1, padx=10, pady=5)
    account_dropdown.current(0)
    product_label = tk.Label(new_window, text="Product:")
    product_label.grid(row=1, column=0, padx=10, pady=5)
    product_entry = tk.Entry(new_window)
    product_entry.grid(row=1, column=1, padx=10, pady=5)

    quantity_label = tk.Label(new_window, text="Quantity:")
    quantity_label.grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(new_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    interval_label = tk.Label(new_window, text="Interval:")
    interval_label.grid(row=3, column=0, padx=10, pady=5)
    interval_entry = tk.Entry(new_window)
    interval_entry.grid(row=3, column=1, padx=10, pady=5)
    
    
    # button = tk.Button(new_window, text="Back", command=handle_button_click)
    button = tk.Button(new_window, text="Back", command=lambda: switch_to_root(new_window))
    button.grid(row=4, column=0, padx=10, pady=10)
    
    button = tk.Button(new_window, text="Start Task", command=handle_button_click)
    button.grid(row=4, column=1, padx=10, pady=10)

    clear_button = tk.Button(new_window, text="Clear", command=clear_fields)
    clear_button.grid(row=4, column=2, padx=10, pady=10)

    label = tk.Label(new_window, text="")
    label.grid(row=5, columnspan=2, padx=10, pady=5)
    
    
    
    root.withdraw()
    # messagebox.showinfo("Button 2", "You clicked Button 2!")

def delete_account(account):
    # Read existing data from the JSON file
    with open('webhooks.json', 'r') as f:
        existing_data = json.load(f)

    # Check if the account exists in the data
    if account in existing_data:
        # Remove the account entry
        del existing_data[account]

        # Write the updated data back to the JSON file
        with open('webhooks.json', 'w') as f:
            json.dump(existing_data, f)

        print(f"Account '{account}' deleted successfully.")
    else:
        print(f"Account '{account}' not found in the JSON file.")


# def button3_click():
#     def delete_account_command():
#         account = entry1.get()  # Get the account name from the entry
#         if account.strip() == "":
#             messagebox.showerror("Error", "Please enter the account name.")
#         else:
#             # Call the delete_account function with the provided account name
#             delete_account(account)


#     new_window = tk.Toplevel()  # Create a new window
#     new_window.title("rm -rf")

#     label0 = tk.Label(new_window, text="")
#     label0.grid(row=0, column=0, padx=10, pady=5)

#     labelx = tk.Label(new_window, text="Delete account")
#     labelx.place(x=120, y=5)

#     label1 = tk.Label(new_window, text="Account")
#     label1.grid(row=1, column=0, padx=10, pady=5)

#     entry1 = tk.Entry(new_window)
#     entry1.grid(row=1, column=1, padx=10, pady=5)

#     button1 = tk.Button(new_window, text="Back", command=lambda: switch_to_root(new_window))
#     button1.grid(row=3, column=0, padx=10, pady=5)

#     button2 = tk.Button(new_window, text="Delete", command=delete_account_command)
#     button2.grid(row=3, column=1, padx=10, pady=5)

#     root.withdraw() 

# def button3_click():
#     def delete_account_command():
#         account = account_var.get()  # Get the selected account from the dropdown
#         if account.strip() == "":
#             messagebox.showerror("Error", "Please select an account.")
#         else:
#             # Call the delete_account function with the selected account
#             delete_account(account)

#     # Read account names from the JSON file
#     with open('webhooks.json') as f:
#         webhook_urls = json.load(f)
#         account_options = list(webhook_urls.keys())

#     new_window = tk.Toplevel()  # Create a new window
#     new_window.title("rm -rf")

#     label0 = tk.Label(new_window, text="")
#     label0.grid(row=0, column=0, padx=10, pady=5)

#     labelx = tk.Label(new_window, text="Delete account")
#     labelx.place(x=120, y=5)

#     label1 = tk.Label(new_window, text="Account")
#     label1.grid(row=1, column=0, padx=10, pady=5)

#     # Dropdown menu for selecting account
#     account_var = tk.StringVar()
#     account_dropdown = ttk.Combobox(new_window, textvariable=account_var, values=account_options)
#     account_dropdown.grid(row=1, column=1, padx=10, pady=5)
#     account_dropdown.current(0)  # Set default value

#     button1 = tk.Button(new_window, text="Back", command=lambda: switch_to_root(new_window))
#     button1.grid(row=3, column=0, padx=10, pady=5)

#     button2 = tk.Button(new_window, text="Delete", command=delete_account_command)
#     button2.grid(row=3, column=1, padx=10, pady=5)

#     root.withdraw() 

def button3_click():
    def delete_account_command():
        account = account_var.get()  # Get the selected account from the dropdown
        if account.strip() == "":
            messagebox.showerror("Error", "Please select an account.")
            return
        
        # Prompt the user for confirmation
        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to delete the account '{account}'?")
        if not confirm:
            return  # Don't delete the account if the user cancels
        
        # Call the delete_account function with the selected account
        delete_account(account)

    # Read account names from the JSON file
    with open('webhooks.json') as f:
        webhook_urls = json.load(f)
        account_options = list(webhook_urls.keys())

    new_window = tk.Toplevel()  # Create a new window
    new_window.title("rm -rf")

    label0 = tk.Label(new_window, text="")
    label0.grid(row=0, column=0, padx=10, pady=5)

    labelx = tk.Label(new_window, text="Delete account")
    labelx.place(x=120, y=5)

    label1 = tk.Label(new_window, text="Account")
    label1.grid(row=1, column=0, padx=10, pady=5)

    # Dropdown menu for selecting account
    account_var = tk.StringVar()
    account_dropdown = ttk.Combobox(new_window, textvariable=account_var, values=account_options)
    account_dropdown.grid(row=1, column=1, padx=10, pady=5)
    account_dropdown.current(0)  # Set default value

    button1 = tk.Button(new_window, text="Back", command=lambda: switch_to_root(new_window))
    button1.grid(row=3, column=0, padx=10, pady=5)

    button2 = tk.Button(new_window, text="Delete", command=delete_account_command)
    button2.grid(row=3, column=1, padx=10, pady=5)

    root.withdraw()






root = tk.Tk()
root.title("Fiddler Start")

original_image = PhotoImage(file="./opp.png")
resized_image = original_image.subsample(12, 13)
image_label = tk.Label(root, image=resized_image)
image_label.place(x=150, y=30)

quantity_label = tk.Label(root, text="Fiddler")
quantity_label.grid(row=0, column=0, columnspan=2, padx=(180, 0), pady=(5, 0), sticky="ew")

button1 = tk.Button(root, text="Add acc", command=button1_click, width=8)
button1.grid(row=1, column=0, padx=10, pady=5)

button2 = tk.Button(root, text="Farm", command=button2_click, width=8)
button2.grid(row=2, column=0, padx=10, pady=5)

button3 = tk.Button(root, text="Delete acc", command=button3_click, width=8)
button3.grid(row=3, column=0, padx=10, pady=5)

window_width = 400
window_height = 170
root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)

root.mainloop()