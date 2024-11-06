import tkinter as tk

# Function to update the expression in the entry box
def update_expression(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

# Function to clear the expression
def clear():
    entry.delete(0, tk.END)

# Function to evaluate the expression
def evaluate():
    try:
        current_expression = entry.get()
        result = str(eval(current_expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for displaying expressions and results
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define button labels and positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

# Create buttons and add to grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=9, height=3, command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, width=9, height=3, command=clear)
    else:
        button = tk.Button(root, text=text, width=9, height=3, command=lambda t=text: update_expression(t))
    
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()
# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y
# def multiply(x,y):
#     return x*y
# def divide(x,y):
#     return x/y
# def modulus(x,my):
#     return x%y
# def ceil(x,y):
#     return x**y
# def floor(x,y):
#     return x//y

# while True:
#     x = int(input("Enter X value:"))
#     y = int(input("Enter Y value:"))
#     choice=input("Enter your Choice(+,-,*,/,//,%,**):")
#     if choice== "+":
#         print("The addition of two numbers is",add(x,y))
#     elif choice== "-":
#         print("The subtraction of two numbers is",sub(x,y))
#     elif choice== "*":
#         print("The multiplication of two numbers is",multiply(x,y))
#     elif choice=="/":
#         print("The Division of two numbers is",divide(x,y))
#     elif choice=="%":
#         print("The modulus of two numbers is",modulus(x,y))
#     elif choice== "***":
#         print("The ceil of two numbers is",ceil(x,y))
#     elif choice== "//":
#         print("The floor division of two numbers is",floor(x,y))
#     ask_user = input("Do you want to calculate again:").lower()
#     if ask_user=="yes":
#         continue
#     else:
#         print("thank you for using calculator!")
#         break