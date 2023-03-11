import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Macro Pad")
window.geometry("300x300")

# Define a function to handle button clicks
def button_click(button_id):
    print(f"Button {button_id} clicked")

# Create the buttons
buttons = []
for i in range(9):
    button = tk.Button(window, text=str(i+1), width=5, height=2, command=lambda i=i: button_click(i+1))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Start the main event loop
window.mainloop()
