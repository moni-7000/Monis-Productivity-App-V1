import tkinter as tk

def buttonClicked():
    print("You clicked the button!\nNow whats the passcode?")
    userCode = input()
    
    if (userCode != "1138"):
        print("Wrong! Sorry!")
    
    else:
        print("Access Granted! Welcome to moniMode!")
    



root = tk.Tk()
root.title("MoniMode")
root.geometry("500x500+600+250")

label = tk.Label(root, text="Welcome to moniMode!!!! :3")
label.pack()
button = tk.Button(root, command=buttonClicked, text="Click this to start!")
button.pack()

root.mainloop()

