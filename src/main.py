import customtkinter as ctk

def showFrame(frame):
    frame.tkraise()
    
#this makes the window i think
root = ctk.CTk()
root.title("MoniMode")
root.geometry("500x530+900+300")

ctk.set_default_color_theme("themes/theme.json")
ctk.set_appearance_mode("light")

#this allows for the window stretching
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#use grid to allow overlapping, nsew to cover whole window
start_frame = ctk.CTkFrame(root)
start_frame.grid(row=0, column=0, sticky="nsew")
main_menu_frame = ctk.CTkFrame(root)
main_menu_frame.grid(row=0, column=0, sticky="nsew")
    
    
#make the custom fonts to reuse 
titleFont = ctk.CTkFont(family="Times", size=23, weight="bold")
bodyFont = ctk.CTkFont(family="Times", size=15)

#pack stuff onto start frame
showFrame(start_frame)
startLabel = ctk.CTkLabel(start_frame, text="   Welcome to moniMode!!!! :3   ", font=titleFont)
startLabel.pack(pady=100)
startButton = ctk.CTkButton(start_frame, command=main_menu_frame.tkraise, text=" Click to start! ", font=bodyFont)
startButton.pack()
authorLabel = ctk.CTkLabel(start_frame, text=" created by moni_7000 ! ", font=("Times", 12))
authorLabel.pack(pady=60)

#pack stuff on main menu 
menuLabel = ctk.CTkLabel(main_menu_frame, text="   MAIN MENU   ", font=titleFont)
menuLabel.pack(pady=100)
calcButton = ctk.CTkButton(main_menu_frame, text="♡  CALCULATOR ♡", font=bodyFont)
calcButton.pack()
todoButton = ctk.CTkButton(main_menu_frame, text="♡  TO-DO LIST  ♡", font=bodyFont)
todoButton.pack(pady=30)
focusButton = ctk.CTkButton(main_menu_frame, text="♡  FOCUS TIMER  ♡", font=bodyFont)
focusButton.pack()


root.mainloop()

