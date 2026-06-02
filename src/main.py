import customtkinter as ctk
import textwrap
import time 

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
#use grid to allow overlapping, sticky to cover whole window
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

addTask_Frame = ctk.CTkFrame(root)
addTask_Frame.grid(row=0, column=0, sticky="nsew")
    
    
#make the custom fonts to reuse 
titleFont = ctk.CTkFont(family="Times", size=27, weight="bold")
bodyFont = ctk.CTkFont(family="Times", size=15)


showFrame(start_frame)
#use a center frame to keep centered as window size changes
start_center_frame = ctk.CTkFrame(start_frame, fg_color="transparent", border_width=0)
start_center_frame.place(relx=0.5, rely=0.5, anchor="center")

#pack widgets onto center frame
startLabel = ctk.CTkLabel(start_center_frame, text="\n     Welcome to Moni's     \n     Productivity App!!      \n", font=titleFont)
startLabel.pack(pady=40)
startButton = ctk.CTkButton(start_center_frame, command=main_menu_frame.tkraise, text=" Click to start! ", font=("Times", 20), width=200)
startButton.pack(pady=30)
authorLabel = ctk.CTkLabel(start_center_frame, text=" created by Monica Ago ! ", font=("Times", 12))
authorLabel.pack(pady=30)


#use another center frame so menu is centered
main_center_frame = ctk.CTkFrame(main_menu_frame, fg_color="transparent", border_width=0)
main_center_frame.place(relx=0.5, rely=0.5, anchor="center")

#pack widgets on main menu 
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
calc_center_frame.place(relx=0.5, rely=0.45, anchor="center")

todo_center_frame = ctk.CTkFrame(todo_frame, fg_color="transparent", border_width=0)
todo_center_frame.place(relx=0.5, rely=0.5, anchor="center")

timer_center_frame = ctk.CTkFrame(timer_frame, fg_color="transparent", border_width=0)
timer_center_frame.place(relx=0.5, rely=0.5, anchor="center")

#Now create the calculator display
calc_entry = ctk.CTkEntry(calc_center_frame, width=175, justify="right", state="disabled")
calc_entry.grid(row=1, column=0, columnspan=3)

delete_button = ctk.CTkButton(calc_center_frame, width=50, text="<<", command=lambda: calculate("<<"))
delete_button.grid(row=1, column=3)

calc_label = ctk.CTkLabel(calc_center_frame, text="♡  CALCULATOR  ♡", font=("Times", 23,"bold"))
calc_label.grid(row=0, columnspan=4, pady=20)

#Array of tuples to hold (row, col, button value)
buttonsxy = [(5,0,0), (5,1,"."), (5,2,"/"), (5,3,"="),
             (4,0,1), (4,1,2), (4,2,3), (4,3,"+"),
             (3,0,4), (3,1,5), (3,2,6), (3,3,"*"),
             (2,0,7), (2,1,8), (2,2,9), (2,3,"-"),
             ]


#Where val is the button the user pressed
#Complete the appropriate operation
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


def clearCalc():
    calc_entry.configure(state="normal")  
    calc_entry.delete(0, "end")
    calc_entry.configure(state="disabled")

#Use a loop to create each button on the calculator
for b_row, b_col, val in buttonsxy:
    myButton = ctk.CTkButton(calc_center_frame, width=50, text=val, command=lambda v=val: calculate(v))
    myButton.grid(row=b_row, column=b_col, padx=7, pady=13)

clearButton = ctk.CTkButton(calculator_frame, text="CLEAR", command=clearCalc, width=100, border_width=0)
clearButton.place(relx=0.5, rely=0.77, anchor="center")

backButton1 = ctk.CTkButton(calculator_frame, text="BACK", command=main_menu_frame.tkraise)
backButton1.place(relx=0.5, rely=0.85, anchor="center")

if ctk.get_appearance_mode().lower() == "dark":
    calc_center_frame.configure(fg_color = "#120f10")


#Moving onto the Todo list
#grid todo menu widgets onto todo list center frame
todoLabel= ctk.CTkLabel(todo_center_frame, text="♡  TODAY'S TASKS  ♡", font=titleFont)
todoLabel.pack(pady=20)

#create a seperate task frame to hold tasks
taskFrame = ctk.CTkFrame(todo_center_frame, border_width=0, fg_color="#de6f92", width=300, height=200)
taskFrame.pack(pady=10)

#num of tasks at a given time
taskCount = 0
#current row to add a new task (no overlapping)
taskRow = 0
#maximum num of tasks
maxTasks = 5

def taskRemoved():
    global taskCount
    taskCount -= 1

def addTask():
    global taskRow
    global maxTasks
    global taskCount
    
    taskName = taskEntry.get()
    #wrap text to sustain window format
    wrappedTask = textwrap.fill(taskName, 30)
    
    if (taskName == "" or taskCount == maxTasks or len(taskName) > 75):
        if (taskCount == maxTasks):
            taskEntry.delete(0, "end")
            taskEntry.insert(0, "Maximum tasks reached!")
            taskEntry.after(1000, lambda: taskEntry.delete(0,"end"))
        else:
            taskEntry.delete(0, "end")
            taskEntry.insert(0, "Invallid task!")
            taskEntry.after(1000, lambda: taskEntry.delete(0,"end"))
        return
    else:
        taskEntry.delete(0, "end")
    
        newTask = ctk.CTkLabel(taskFrame, text=wrappedTask)
        newTask.grid(row=taskRow, column=0, padx=10, pady=10, sticky="w")
    
        doneButton= ctk.CTkButton(taskFrame, text="✓", width = 20, command= lambda: (newTask.destroy(), doneButton.destroy(), taskRemoved()))
        doneButton.grid(row=taskRow, column=1, padx=10, pady=10)
    
        taskRow += 1
        taskCount += 1
    

#center frame for the add task frame
add_task_center_frame = ctk.CTkFrame(addTask_Frame, fg_color="transparent", border_width=0)
add_task_center_frame.place(relx=0.5, rely=0.5, anchor="center")

taskHelpLabel = ctk.CTkLabel(add_task_center_frame, text="♡ Tasks may be <= 75 characters!\n♡ The maximum # of tasks is 5!", font=("times", 23))
taskHelpLabel.pack(pady=30)

taskEntry = ctk.CTkEntry(add_task_center_frame, width=200, justify="right", state="normal")
taskEntry.pack(pady=10)

#button that makes the real task
createTaskButton = ctk.CTkButton(add_task_center_frame, text=" ADD TO TASK LIST ", command=addTask)
createTaskButton.pack(pady=30)

backButton2=ctk.CTkButton(add_task_center_frame, text="BACK", command=todo_frame.tkraise)
backButton2.pack(pady=10)

#the button that takes you to the frame to make the task
gotoAddTaskButton = ctk.CTkButton(todo_center_frame, text=" ADD TASK", font=bodyFont, command=addTask_Frame.tkraise)
gotoAddTaskButton.pack(pady=20)

backButton3=ctk.CTkButton(todo_center_frame, text="BACK", command=main_menu_frame.tkraise)
backButton3.pack(pady=10)


#now move onto timer implementation
#grid stuff onto focus timer center frame
testLabel3= ctk.CTkLabel(timer_center_frame, text="  ♡ TIMER ♡  ", font=titleFont)
testLabel3.pack(pady=20)


timerLabel = ctk.CTkLabel(timer_center_frame, text= " 00:00:00 ", font=("times", 65, "bold"))
timerLabel.pack(pady=10)

timer_hrs = 0
timer_mins = 0
timer_sec = 0

def updateTimer():
    timerLabel.configure(text=f" {timer_hrs:02}:{timer_mins:02}:{timer_sec:02} ")

timerStarted = False
  
def addMin():
    global timer_mins
    if timer_mins <= 59 and not timerStarted:
        timer_mins += 1
        updateTimer()
    
def rmMin():
    global timer_mins
    if timer_mins > 0 and not timerStarted:
        timer_mins -= 1
        updateTimer()   
    
def addHr():
    global timer_hrs
    if not timerStarted:
        timer_hrs += 1
        updateTimer()
    
def rmHr():
    global timer_hrs
    if timer_hrs > 0 and not timerStarted:
        timer_hrs -= 1
        updateTimer()
    
timerConfigureFrame = ctk.CTkFrame(timer_center_frame, border_width=0)
timerConfigureFrame.pack(pady=10)

upMinButton = ctk.CTkButton(timerConfigureFrame, text= "+1 Min", command=addMin)
upMinButton.grid(row=0, column=0, padx=10, pady=10)

downMinButton = ctk.CTkButton(timerConfigureFrame, text= "-1 Min", command=rmMin)
downMinButton.grid(row=0, column=1, padx=10, pady=10)

upHrButton = ctk.CTkButton(timerConfigureFrame, text="+1 Hr", command=addHr)
upHrButton.grid(row=1, column=0, padx=10, pady=10)

downHrButton = ctk.CTkButton(timerConfigureFrame, text="-1 Hr", command=rmHr)
downHrButton.grid(row=1, column=1, padx=10, pady=10)

stopTimer = False

def pressedStop():
    if timerStarted:
        global stopTimer
        stopTimer = True
  

def startTimer():
    global timer_hrs
    global timer_mins
    global timer_sec
    global timerStarted
    global stopTimer
    
    if not stopTimer:
        timerStarted = True 
        updateTimer()
    
        if timer_hrs <= 0 and timer_mins <= 0 and timer_sec <= 0:
            timerStarted = False
            return
        if timer_sec <= 0:    
            if timer_mins <= 0:
                timer_hrs -= 1
                timer_mins += 59
                timer_sec = 59      
            else:
                timer_mins -= 1
                timer_sec += 59
        else:
            timer_sec -= 1
        timerLabel.after(1000, startTimer)
    else:
        timer_mins = 0
        timer_sec = 0
        timer_hrs = 0
        timerStarted = False
        stopTimer = False
        updateTimer()
        return



startTimerButton = ctk.CTkButton(timerConfigureFrame, text=" START ", command=startTimer, width=50)
startTimerButton.grid(row=2, column=0, columnspan=2,pady=10)

stopTimerButton = ctk.CTkButton(timerConfigureFrame, text=" STOP ", command=pressedStop, width=50)
stopTimerButton.grid(row=3, column=0, columnspan=2, pady=10)

backButton3=ctk.CTkButton(timer_center_frame, text="BACK", command=main_menu_frame.tkraise)
backButton3.pack(pady=10)








root.mainloop()

