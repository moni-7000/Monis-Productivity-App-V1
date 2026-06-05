import customtkinter as ctk
import textwrap
import time 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Moni's Productivity App")
        self.geometry("500x600+900+300")
        
        #set theme
        ctk.set_default_color_theme("themes/theme.json")
        ctk.set_appearance_mode("light")
        
        #allow window stretching
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.titleFont = ctk.CTkFont(family="Times", size=27, weight="bold")
        self.bodyFont = ctk.CTkFont(family="Times", size=15)
        self.createFrames()
        
    def createFrames(self):
        
        #create all frames that will be used
        #use grid to allow overlapping, sticky to cover whole window
        self.main_menu_frame = MainMenu(self,self)
        self.main_menu_frame.grid(row=0, column=0, sticky="nsew")
        
        self.start_frame = StartScreen(self,self)
        self.start_frame.grid(row=0, column=0, sticky="nsew")
        

        self.calculator_frame = Calculator(self,self)
        self.calculator_frame.grid(row=0, column=0, sticky="nsew")

        self.todo_frame = TodoList(self,self)
        self.todo_frame.grid(row=0, column=0, sticky="nsew")

        self.timer_frame = FocusTimer(self,self)
        self.timer_frame.grid(row=0, column=0, sticky="nsew")

        self.addTask_Frame = AddTaskScreen(self,self)
        self.addTask_Frame.grid(row=0, column=0, sticky="nsew")
        
        #show the start screen first
        self.start_frame.tkraise()
    
       
        
    
class StartScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #use a center frame to keep centered as window size changes
        self.start_center_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)
        self.start_center_frame.place(relx=0.5, rely=0.5, anchor="center")

        #pack widgets onto center frame
        startLabel = ctk.CTkLabel(self.start_center_frame, text="\n     Welcome to Moni's     \n     Productivity App!!      \n", font=self.controller.titleFont)
        startLabel.pack(pady=40)
        startButton = ctk.CTkButton(self.start_center_frame, command= lambda: self.controller.main_menu_frame.tkraise(), text=" Click to start! ", font=("Times", 20), width=200)
        startButton.pack(pady=30)
        authorLabel = ctk.CTkLabel(self.start_center_frame, text=" created by Monica Ago ! ", font=("Times", 12))
        authorLabel.pack(pady=30)
        

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #use another center frame so menu is centered
        self.main_center_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)
        self.main_center_frame.place(relx=0.5, rely=0.5, anchor="center")

        #pack widgets on main menu 
        menuLabel = ctk.CTkLabel(self.main_center_frame, text="   MAIN MENU   ", font=self.controller.titleFont)
        menuLabel.pack(pady=60)
        calcButton = ctk.CTkButton(self.main_center_frame, text="♡  CALCULATOR ♡", command= lambda: self.controller.calculator_frame.tkraise(), font=self.controller.bodyFont)
        calcButton.pack()
        todoButton = ctk.CTkButton(self.main_center_frame, text="♡  TO-DO LIST  ♡", command= lambda: self.controller.todo_frame.tkraise(), font=self.controller.bodyFont)
        todoButton.pack(pady=50)
        focusButton = ctk.CTkButton(self.main_center_frame, text="♡  FOCUS TIMER  ♡", command= lambda: self.controller.timer_frame.tkraise(), font=self.controller.bodyFont)
        focusButton.pack()
        

        
class Calculator(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        #create and place all the center frames
        self.calc_center_frame = ctk.CTkFrame(self, fg_color="#ffb0c0", border_width=3)
        self.calc_center_frame.place(relx=0.5, rely=0.45, anchor="center")
        
        if ctk.get_appearance_mode().lower() == "dark":
            self.calc_center_frame.configure(fg_color = "#120f10")
    
        #Now create the calculator display
        self.calc_entry = ctk.CTkEntry(self.calc_center_frame, width=175, justify="right", state="disabled")
        self.calc_entry.grid(row=1, column=0, columnspan=3)
        
        #Array of tuples to hold (row, col, button value)
        self.buttonsxy = [(5,0,0), (5,1,"."), (5,2,"/"), (5,3,"="),
                    (4,0,1), (4,1,2), (4,2,3), (4,3,"+"),
                    (3,0,4), (3,1,5), (3,2,6), (3,3,"*"),
                    (2,0,7), (2,1,8), (2,2,9), (2,3,"-"), ]
        
        self.makeButtons()
        
        delete_button = ctk.CTkButton(self.calc_center_frame, width=50, text="<<", command=lambda: self.calculate("<<"))
        delete_button.grid(row=1, column=3)

        calc_label = ctk.CTkLabel(self.calc_center_frame, text="♡  CALCULATOR  ♡", font=("Times", 23,"bold"))
        calc_label.grid(row=0, columnspan=4, pady=20)
        self.negative = False
        
    def makeButtons(self):
        #Use a loop to create each button on the calculator
        for b_row, b_col, val in self.buttonsxy:
            myButton = ctk.CTkButton(self.calc_center_frame, width=50, text=val, command=lambda v=val: self.calculate(v))
            myButton.grid(row=b_row, column=b_col, padx=7, pady=13)

        clearButton = ctk.CTkButton(self, text="CLEAR", command=self.clearCalc, width=100, border_width=0)
        clearButton.place(relx=0.5, rely=0.77, anchor="center")

        backButton1 = ctk.CTkButton(self, text="BACK", command= lambda:self.controller.main_menu_frame.tkraise())
        backButton1.place(relx=0.5, rely=0.85, anchor="center")

            
    def calculate(self, val):
        
        operators = ["/", "+", "-", "*"]

    
        if(val in operators or val == "."):
        
            if ((self.calc_entry.get() == "") or (self.calc_entry.get()[-1] in operators)):
            
                if (val == "-"):
                    if (self.calc_entry.get() == ""):
                        self.calc_entry.configure(state="normal")
                        self.calc_entry.insert("end", str(val))
                        self.calc_entry.configure(state="disabled")
                    elif (self.calc_entry.get()[-1] in operators):
                        if not self.negative:
                            self.calc_entry.configure(state="normal")
                            self.calc_entry.insert("end", str(val))
                            self.calc_entry.configure(state="disabled")
                            self.negative = True  
            elif(val == "."):
                text = self.calc_entry.get()
            
                for i in range (len(text) -1, -1, -1):
                    if text[i] in operators:
                        index = i
                        break
                
                if ("." in text[index+1:]):
                    pass
                else:
                    self.calc_entry.configure(state="normal")
                    self.calc_entry.insert("end", str(val))
                    self.calc_entry.configure(state="disabled")
                
            else:
                self.calc_entry.configure(state="normal")
                self.calc_entry.insert("end", str(val))
                self.calc_entry.configure(state="disabled")              
        else:
            if (val == "="):
        
                result = self.calc_entry.get()
        
                try:
                    answer = eval(self.calc_entry.get())
                    self.calc_entry.configure(state="normal")  
                    self.calc_entry.delete(0, "end")
                    self.calc_entry.insert(0, answer)
                    self.calc_entry.configure(state="disabled") 
                except ZeroDivisionError:
                    self.calc_entry.configure(state="normal")  
                    self.calc_entry.delete(0, "end")
                    self.calc_entry.insert(0, "Cannot divide by zero!")
                    self.calc_entry.after(1000, lambda: (self.calc_entry.delete(0, "end"), self.calc_entry.configure(state="disabled")))
                except Exception:
                    self.calc_entry.configure(state="normal")  
                    self.calc_entry.delete(0, "end")
                    self.calc_entry.insert(0,"Invallid expression!")
                    self.calc_entry.after(1000, lambda: (self.calc_entry.delete(0, "end"), self.calc_entry.configure(state="disabled")))
            
            elif(val == "<<"):
                if (self.calc_entry.get() != ""):
                    if self.calc_entry.get()[-1] == "-":
                        self.negative = False
                
                self.calc_entry.configure(state="normal")
                self.calc_entry.delete(len(self.calc_entry.get()) - 1)
                self.calc_entry.configure(state="disabled")     
            else:
                self.calc_entry.configure(state="normal")
                self.calc_entry.insert("end", str(val))
                self.calc_entry.configure(state="disabled")
                self.negative = False
                    
    def clearCalc(self):
        self.calc_entry.configure(state="normal")  
        self.calc_entry.delete(0, "end")
        self.calc_entry.configure(state="disabled")
        
        
class TodoList(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.todo_center_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)
        self.todo_center_frame.place(relx=0.5, rely=0.5, anchor="center")

        #grid todo menu widgets onto todo list center frame
        todoLabel= ctk.CTkLabel(self.todo_center_frame, text="♡  TODAY'S TASKS  ♡", font= self.controller.titleFont)
        todoLabel.pack(pady=20)

        #create a seperate task frame to hold tasks
        self.taskFrame = ctk.CTkFrame(self.todo_center_frame, border_width=0, fg_color="#de6f92", width=300, height=200)
        self.taskFrame.pack(pady=10)

        #num of tasks at a given time
        self.taskCount = 0
        #current row to add a new task (no overlapping)
        self.taskRow = 0
        #maximum num of tasks
        self.maxTasks = 5
        #the button that takes you to the frame to make the task
        self.gotoAddTaskButton = ctk.CTkButton(self.todo_center_frame, text=" ADD TASK", font=self.controller.bodyFont, command= lambda:self.controller.addTask_Frame.tkraise())
        self.gotoAddTaskButton.pack(pady=20)

        backButton3=ctk.CTkButton(self.todo_center_frame, text="BACK", command= lambda:self.controller.main_menu_frame.tkraise())
        backButton3.pack(pady=10)
        
        self.stopTimer = False
        
    def taskRemoved(self):
        self.taskCount -= 1

    def addTask(self):
    
        taskName = self.controller.addTask_Frame.taskEntry.get()
        #wrap text to sustain window format
        wrappedTask = textwrap.fill(taskName, 30)
    
        if (taskName == "" or self.taskCount == self.maxTasks or len(taskName) > 75):
            if (self.taskCount == self.maxTasks):
                self.controller.addTask_Frame.taskEntry.delete(0, "end")
                self.controller.addTask_Frame.taskEntry.insert(0, "Maximum tasks reached!")
                self.controller.addTask_Frame.taskEntry.after(1000, lambda: self.controller.addTask_Frame.taskEntry.delete(0,"end"))
            else:
                self.controller.addTask_Frame.taskEntry.delete(0, "end")
                self.controller.addTask_Frame.taskEntry.insert(0, "Invallid task!")
                self.controller.addTask_Frame.taskEntry.after(1000, lambda: self.controller.addTask_Frame.taskEntry.delete(0,"end"))
            return
        else:
            self.controller.addTask_Frame.taskEntry.delete(0, "end")
    
            newTask = ctk.CTkLabel(self.taskFrame, text=wrappedTask)
            newTask.grid(row=self.taskRow, column=0, padx=10, pady=10, sticky="w")
    
            doneButton= ctk.CTkButton(self.taskFrame, text="✓", width = 20)
            doneButton.configure(command= lambda label=newTask, btn= doneButton: (label.destroy(), btn.destroy(), self.taskRemoved()))
            doneButton.grid(row=self.taskRow, column=1, padx=10, pady=10)
    
            self.taskRow += 1
            self.taskCount += 1
        

class AddTaskScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller= controller  
        
        #center frame for the add task frame
        self.add_task_center_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)
        self.add_task_center_frame.place(relx=0.5, rely=0.5, anchor="center")

        taskHelpLabel = ctk.CTkLabel(self.add_task_center_frame, text="♡ Tasks may be <= 75 characters!\n♡ The maximum # of tasks is 5!", font=("times", 23))
        taskHelpLabel.pack(pady=30)

        self.taskEntry = ctk.CTkEntry(self.add_task_center_frame, width=200, justify="right", state="normal")
        self.taskEntry.pack(pady=10)

        #button that makes the real task
        createTaskButton = ctk.CTkButton(self.add_task_center_frame, text=" ADD TO TASK LIST ", command= lambda: self.controller.todo_frame.addTask())
        createTaskButton.pack(pady=30)

        backButton2=ctk.CTkButton(self.add_task_center_frame, text="BACK", command= lambda:self.controller.todo_frame.tkraise())
        backButton2.pack(pady=10)
    
                
        
class FocusTimer(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        self.timer_center_frame = ctk.CTkFrame(self, fg_color="transparent", border_width=0)
        self.timer_center_frame.place(relx=0.5, rely=0.5, anchor="center")

        #grid stuff onto focus timer center frame
        testLabel3= ctk.CTkLabel(self.timer_center_frame, text="  ♡ TIMER ♡  ", font=self.controller.titleFont)
        testLabel3.pack(pady=20)


        self.timerLabel = ctk.CTkLabel(self.timer_center_frame, text= " 00:00:00 ", font=("times", 65, "bold"))
        self.timerLabel.pack(pady=10)

        self.timer_hrs = 0
        self.timer_mins = 0
        self.timer_sec = 0
        
        self.timerConfigureFrame = ctk.CTkFrame(self.timer_center_frame, border_width=0)
        self.timerConfigureFrame.pack(pady=10)
        
        self.makeTimerButtons()
        
        self.backButton3=ctk.CTkButton(self.timer_center_frame, text="BACK", command= lambda: self.controller.main_menu_frame.tkraise())
        self.backButton3.pack(pady=10)
        
        self.timerStarted = False
        self.stopTimer = False
        
    def updateTimer(self):
        self.timerLabel.configure(text=f" {self.timer_hrs:02}:{self.timer_mins:02}:{self.timer_sec:02} ")

  
    def addMin(self):
        if self.timer_mins <= 59 and not self.timerStarted:
            self.timer_mins += 1
            self.updateTimer()
        
    def rmMin(self):
        if self.timer_mins > 0 and not self.timerStarted:
            self.timer_mins -= 1
            self.updateTimer()   
        
    def addHr(self):
        if not self.timerStarted:
            self.timer_hrs += 1
            self.updateTimer()
        
    def rmHr(self):
        if self.timer_hrs > 0 and not self.timerStarted:
            self.timer_hrs -= 1
            self.updateTimer()
            
    def makeTimerButtons(self):

        upMinButton = ctk.CTkButton(self.timerConfigureFrame, text= "+1 Min", command=self.addMin)
        upMinButton.grid(row=0, column=0, padx=10, pady=10)

        downMinButton = ctk.CTkButton(self.timerConfigureFrame, text= "-1 Min", command=self.rmMin)
        downMinButton.grid(row=0, column=1, padx=10, pady=10)

        upHrButton = ctk.CTkButton(self.timerConfigureFrame, text="+1 Hr", command=self.addHr)
        upHrButton.grid(row=1, column=0, padx=10, pady=10)

        downHrButton = ctk.CTkButton(self.timerConfigureFrame, text="-1 Hr", command=self.rmHr)
        downHrButton.grid(row=1, column=1, padx=10, pady=10)
        
        startTimerButton = ctk.CTkButton(self.timerConfigureFrame, text=" START ", command=self.startTimer, width=50)
        startTimerButton.grid(row=2, column=0, columnspan=2,pady=10)

        stopTimerButton = ctk.CTkButton(self.timerConfigureFrame, text=" STOP ", command=self.pressedStop, width=50)
        stopTimerButton.grid(row=3, column=0, columnspan=2, pady=10)

        
    def pressedStop(self):
        if self.timerStarted:
            self.stopTimer = True
  

    def startTimer(self): 
        if not self.stopTimer:
            self.timerStarted = True 
            self.updateTimer()
        
            if self.timer_hrs <= 0 and self.timer_mins <= 0 and self.timer_sec <= 0:
                self.timerStarted = False
                return
            if self.timer_sec <= 0:    
                if self.timer_mins <= 0:
                    self.timer_hrs -= 1
                    self.timer_mins += 59
                    self.timer_sec = 59      
                else:
                    self.timer_mins -= 1
                    self.timer_sec += 59
            else:
                self.timer_sec -= 1
            self.timerLabel.after(1000, self.startTimer)
        else:
            self.timer_mins = 0
            self.timer_sec = 0
            self.timer_hrs = 0
            self.timerStarted = False
            self.stopTimer = False
            self.updateTimer()
            return



if __name__ == "__main__":
    app = App()
    app.mainloop()

