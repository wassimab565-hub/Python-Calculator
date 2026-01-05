import tkinter as tk

# ---------------- Functions ----------------
def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

# ---------------- GUI Setup ----------------
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")

screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=5, relief=tk.RIDGE, justify='right')
screen.pack(fill='both', ipadx=8, pady=10, padx=10)
# ---------------- Buttons ----------------
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
    ['C']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill='both')
    for b in row:
        btn = tk.Button(frame, text=b, font="Arial 18", relief=tk.RIDGE, bd=2)
        btn.pack(side='left', expand=True, fill='both')
        btn.bind("<Button-1>", click)

# ---------------- Run App ----------------
root.mainloop()
