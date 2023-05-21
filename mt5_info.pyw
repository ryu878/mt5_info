# Ryuryu's MT5 Account Info (always on top)
# --------------------------------------
# (c) 2023 Ryan Hayabusa 
# GitGub: https://github.com/ryu878
# Web: https://aadresearch.xyz
# Discord: https://discord.gg/zSw58e9Uvf
# Telegram: https://t.me/aadresearch
# --------------------------------------

from datetime import datetime
import tkinter as tk
import MetaTrader5 as mt5


account_id = 0000000000  # Replace with your account ID

# Init
if not mt5.initialize():
    print('initialize() failed, error code =', mt5.last_error())
    quit()

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def get_account_info():
    account_info = mt5.account_info()
    if account_info is not None:
        account_info_dict = account_info._asdict()
        equity = account_info_dict['equity']
        margin_free = account_info_dict['margin_free']
        balance = account_info_dict['balance']
        positions = round((margin_free - balance), 2)

        return f"           Equity: {equity}\nFree Margin: {margin_free}\n       Balance: {balance}\n     Positions: {positions}"
    else:
        return "Account information not available"

def update_time_and_account_info():
    current_time = get_current_time()
    account_info = get_account_info()
    time_label.config(text=current_time)
    history_label.config(text=account_info)
    window.after(1000, update_time_and_account_info)  # Schedule the next update after 1 second (1000 milliseconds)

window = tk.Tk()
window.title("Account Info")
window.geometry("250x200")
window.wm_attributes("-topmost", True)  # Set the window to be always on top

time_label = tk.Label(window, text="", font=("Helvetica", 24))
time_label.pack(pady=10)

history_label = tk.Label(window, text="", font=("Helvetica", 12), justify=tk.LEFT)
history_label.pack(pady=10)

update_time_and_account_info()  # Start the initial update

window.mainloop()
