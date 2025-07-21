import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def process_text():
    msg = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        output_result.config(text="Shift must be a number.")
        return
    mode = mode_var.get()
    result = caesar_cipher(msg, shift, mode)
    output_result.config(text=result)

root = tk.Tk()
root.title("Caesar Cipher Encryptor/Decryptor")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Message:").pack(pady=5)
entry_message = tk.Entry(root, width=50)
entry_message.pack()

tk.Label(root, text="Enter Shift Value:").pack(pady=5)
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

mode_var = tk.StringVar(value="encrypt")
tk.Label(root, text="Choose Mode:").pack(pady=5)
tk.Radiobutton(root, text="Encrypt", variable=mode_var, value="encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode_var, value="decrypt").pack()

tk.Button(root, text="Process", command=process_text).pack(pady=10)

tk.Label(root, text="Result:").pack()
output_result = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=350, justify="center")
output_result.pack(pady=5)

root.mainloop()
