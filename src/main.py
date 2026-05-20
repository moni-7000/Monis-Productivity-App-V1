import customtkinter as ctk

root = ctk.CTk()
root.title("MoniMode")
root.geometry("500x500+900+300")

start_frame = ctk.CTkFrame(root)
main_menu_frame = ctk. CTkFrame(root)

def startButtonClicked():
    print("You clicked the button!\n")
    showFrame(main_menu_frame)
    start_frame.pack_forget()

def showFrame(frame):
    frame.tkraise()
    frame.pack()
    
def hideFrame(frame):
    pass

showFrame(start_frame)
startLabel = ctk.CTkLabel(start_frame, text="Welcome to moniMode!!!! :3")
startLabel.pack()
startButton = ctk.CTkButton(start_frame, command=startButtonClicked, text="Click this to start!")
startButton.pack()

menuLabel = ctk.CTkLabel(main_menu_frame, text="MAIN MENU\n")
menuLabel.pack()
calcButton = ctk.CTkButton(main_menu_frame, text="♡  CALCULATOR ♡")
calcButton.pack()
todoButton = ctk.CTkButton(main_menu_frame, text="♡  TO-DO LIST  ♡")
todoButton.pack()
focusButton = ctk.CTkButton(main_menu_frame, text="♡  FOCUS TIMER  ♡")
focusButton.pack()



root.mainloop()

