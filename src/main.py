import customtkinter as ctk

def showFrame(frame):
    frame.tkraise()
    
#this makes the window i think
root = ctk.CTk()
root.title("Moni's Productivity App")
root.geometry("500x600+900+300")


#set theme
ctk.set_default_color_theme("themes/theme.json")
ctk.set_appearance_mode("light")

#this allows for the window stretching
root.grid_rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


#create all frames that will be used
#use grid to allow overlapping, nsew to cover whole window
start_frame = ctk.CTkFrame(root)
start_frame.grid(row=0, column=0, sticky="nsew")

main_menu_frame = ctk.CTkFrame(root)
main_menu_frame.grid(row=0, column=0, sticky="nsew")

calculator_frame = ctk.CTkFrame(root)
calculator_frame.grid(row=0, column=0, sticky="nsew")

todo_frame = ctk.CTkFrame(root)
todo_frame.grid(row=0, column=0, sticky="nsew")

timer_frame = ctk.CTkFrame(root)
timer_frame.grid(row=0, column=0, sticky="nsew")
    
    
#make the custom fonts to reuse 
titleFont = ctk.CTkFont(family="Times", size=27, weight="bold")
bodyFont = ctk.CTkFont(family="Times", size=15)


showFrame(start_frame)
#use a center frame to keep centered as window size changes
start_center_frame = ctk.CTkFrame(start_frame, fg_color="transparent", border_width=0)
start_center_frame.place(relx=0.5, rely=0.5, anchor="center")

#pack stuff onto center frame
startLabel = ctk.CTkLabel(start_center_frame, text="     Welcome to Moni's     \n     Productivity App!!      ", font=titleFont)
startLabel.pack(pady=40)
startButton = ctk.CTkButton(start_center_frame, command=main_menu_frame.tkraise, text=" Click to start! ", font=bodyFont)
startButton.pack(pady=30)
authorLabel = ctk.CTkLabel(start_center_frame, text=" created by moni_7000 ! ", font=("Times", 12))
authorLabel.pack(pady=30)


#use another center frame so menu is centered
main_center_frame = ctk.CTkFrame(main_menu_frame, fg_color="transparent", border_width=0)
main_center_frame.place(relx=0.5, rely=0.5, anchor="center")

#pack stuff on main menu 
menuLabel = ctk.CTkLabel(main_center_frame, text="   MAIN MENU   ", font=titleFont)
menuLabel.pack(pady=60)
calcButton = ctk.CTkButton(main_center_frame, text="♡  CALCULATOR ♡", command=calculator_frame.tkraise, font=bodyFont)
calcButton.pack()
todoButton = ctk.CTkButton(main_center_frame, text="♡  TO-DO LIST  ♡", command=todo_frame.tkraise, font=bodyFont)
todoButton.pack(pady=50)
focusButton = ctk.CTkButton(main_center_frame, text="♡  FOCUS TIMER  ♡", command=timer_frame.tkraise, font=bodyFont)
focusButton.pack()

#create and place all the center frames
calc_center_frame = ctk.CTkFrame(calculator_frame, fg_color="#ffb0c0", border_width=3)
calc_center_frame.place(relx=0.5, rely=0.5, anchor="center")

todo_center_frame = ctk.CTkFrame(todo_frame, fg_color="transparent", border_width=0)
todo_center_frame.place(relx=0.5, rely=0.5, anchor="center")

timer_center_frame = ctk.CTkFrame(timer_frame, fg_color="transparent", border_width=0)
timer_center_frame.place(relx=0.5, rely=0.5, anchor="center")

#Now create the calculator display

entry=""
#backButton1=ctk.CTkButton(calc_center_frame, text="BACK", command=main_menu_frame.tkraise)
calc_entry = ctk.CTkEntry(calc_center_frame, width=175, textvariable=entry, justify="right", state="disabled")
calc_entry.grid(row=1, column=0, columnspan=3)

delete_button = ctk.CTkButton(calc_center_frame, width=50, text="<<", command=lambda: calculate("<<"))
delete_button.grid(row=1, column=3)

calc_label = ctk.CTkLabel(calc_center_frame, text="♡  CALCULATOR  ♡", font=("Times", 23,"bold"))
calc_label.grid(row=0, columnspan=4, pady=20)

buttonsxy = [(5,0,0), (5,1,"."), (5,2,"/"), (5,3,"="),
             (4,0,1), (4,1,2), (4,2,3), (4,3,"+"),
             (3,0,4), (3,1,5), (3,2,6), (3,3,"*"),
             (2,0,7), (2,1,8), (2,2,9), (2,3,"-"),
             ]

def calculate(val):
    
    operators = ["/", "+", "-", "*"]
    
        
    if(val in operators or val == "."):
        if ((calc_entry.get() == "") or (calc_entry.get()[-1] in operators)):
            pass    
        elif(val == "."):
            text = calc_entry.get()
            
            for i in range (len(text) -1, -1, -1):
                if text[i] in operators:
                    index = i
                    break
                
            if ("." in text[i+1:]):
                pass
            else:
                calc_entry.configure(state="normal")
                calc_entry.insert("end", str(val))
                calc_entry.configure(state="disabled")
                
        else:
            calc_entry.configure(state="normal")
            calc_entry.insert("end", str(val))
            calc_entry.configure(state="disabled")              
    else:
        if (val == "="):
            result = calc_entry.get()
            calc_entry.configure(state="normal")  
            calc_entry.delete(0, "end")
            calc_entry.insert(0, eval(result))
            calc_entry.configure(state="disabled") 
        elif(val == "<<"):
            calc_entry.configure(state="normal")
            calc_entry.delete(len(calc_entry.get()) - 1)
            calc_entry.configure(state="disabled")     
        else:
            calc_entry.configure(state="normal")
            calc_entry.insert("end", str(val))
            calc_entry.configure(state="disabled")




for b_row, b_col, val in buttonsxy:
    myButton = ctk.CTkButton(calc_center_frame, width=50, text=val, command=lambda v=val: calculate(v))
    myButton.grid(row=b_row, column=b_col, padx=7, pady=13)

backButton1 = ctk.CTkButton(calculator_frame, text="BACK", command=main_menu_frame.tkraise)
backButton1.place(relx=0.5, rely=0.85, anchor="center")


#grid stuff onto todo list center frame
testLabel2= ctk.CTkLabel(todo_center_frame, text="♡  TODAY'S TASKS  ♡", font=titleFont)
testLabel2.pack(pady=20)

taskFrame = ctk.CTkFrame(todo_center_frame, border_width=10, fg_color="#de6f92")
taskFrame.pack()

backButton2=ctk.CTkButton(todo_center_frame, text="BACK", command=main_menu_frame.tkraise)
backButton2.pack(pady=10)

#grid stuff onto focus timer center frame
testLabel3= ctk.CTkLabel(timer_center_frame, text="timer frame test")
testLabel3.pack()
backButton3=ctk.CTkButton(timer_center_frame, text="BACK", command=main_menu_frame.tkraise)
backButton3.pack(pady=10)








root.mainloop()

