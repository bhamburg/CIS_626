# Assignment 1
# Author: Brian Hamburg

from tkinter import * # Import tkinter

class ValidateInfo:
    def __init__(self):      
        window = Tk() # Create a window
        window.title("Validate Info") # Set title

        self.firstNameVar = StringVar()
        self.lastNameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()
        self.phoneVar = StringVar()
        self.birthmonthVar = StringVar()
        self.birthdayVar = StringVar()
        self.birthyearVar = StringVar()
        self.emailVar = StringVar()

        # Create a menu bar
        menubar = Menu(window)
        
        # create a pulldown menus, and add them to the menu bar
        messagesMenu = Menu(menubar, tearoff=0)
        messagesMenu.add_command(label="Birthday Greeting", command = self.birthdayGreeting)
        messagesMenu.add_command(label="Print Address", command = self.printAddress)
        menubar.add_cascade(label="Messages", menu=messagesMenu)
        
        endMenu = Menu(menubar, tearoff=0)
        endMenu.add_command(label = "Reset", command = self.resetForm)
        endMenu.add_command(label = "Exit", command = quit)
        menubar.add_cascade(label="End", menu = endMenu)
        
        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text = "Name").grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame1, textvariable = self.firstNameVar, 
            width = 20).grid(row = 1, column = 2)
        Entry(frame1, textvariable = self.lastNameVar, 
            width = 20).grid(row = 1, column = 3)
        
        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text = "Street").grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame2, textvariable = self.streetVar, 
            width = 40).grid(row = 1, column = 2)
            
        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text = "City", width = 5).grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame3, 
            textvariable = self.cityVar).grid(row = 1, column = 2)
        Label(frame3, text = "State").grid(row = 1, 
            column = 3, sticky = W)
        Entry(frame3, textvariable = self.stateVar, 
            width = 5).grid(row = 1, column = 4)
        Label(frame3, text = "ZIP").grid(row = 1, 
            column = 5, sticky = W)
        Entry(frame3, textvariable = self.zipVar, 
            width = 5).grid(row = 1, column = 6)

        frame4 = Frame(window)
        frame4.pack()
        Label(frame4, text = "Telephone", width = 9).grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame4, 
            textvariable = self.phoneVar).grid(row = 1, column = 2)

        frame5 = Frame(window)
        frame5.pack()
        Label(frame5, text = "Birthday (mm/dd/yyyy)", width = 20).grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame5, 
            textvariable = self.birthmonthVar, 
            width = 2).grid(row = 1, column = 2)
        Entry(frame5, 
            textvariable = self.birthdayVar, 
            width = 2).grid(row = 1, column = 3)
        Entry(frame5, 
            textvariable = self.birthyearVar, 
            width = 4).grid(row = 1, column = 4)

        frame6 = Frame(window)
        frame6.pack()
        Label(frame6, text = "Email address", width = 12).grid(row = 1, 
            column = 1, sticky = W)
        Entry(frame6, 
            textvariable = self.emailVar).grid(row = 1, column = 2)
        
        frame7 = Frame(window)
        frame7.pack()
        Button(frame7, text = "Validate", 
            command = self.submitForm).grid(row = 1, column = 1)
        
        window.config(menu = menubar) # Display the menu bar
        window.mainloop() # Create an event loop
        
    def birthdayGreeting(self):
        # validate birthday
        invalidCount = 0
        birthmonthStr = self.birthmonthVar.get()
        birthmonth = eval(birthmonthStr.lstrip('0'))
        birthdayStr = self.birthdayVar.get()
        birthday = eval(birthdayStr.lstrip('0'))
        birthyear = eval(self.birthyearVar.get())
        
        if birthmonth < 1 or birthmonth > 12:
            invalidCount += 1
            print("Invalid birth date!")
        elif (birthmonth == 2 and birthday > 29) or birthday < 1:
            invalidCount += 1
            print("Invalid birthday!")
        elif (birthmonth == 4 or birthmonth == 6 or birthmonth == 9 or birthmonth == 11) and birthday > 30 or birthday < 1:
            invalidCount += 1
            print("Invalid birthday!")
        elif (birthmonth == 1 or birthmonth == 3 or birthmonth == 5 or birthmonth == 7 or birthmonth == 8 or birthmonth == 10 or birthmonth == 12) and birthday > 31 or birthday < 1:
            invalidCount += 1
            print("Invalid birth date!")

        if birthyear < 1900 or birthyear > 2013:
            print("Invalid birth date!")

        # print greeting
        if invalidCount == 0:
            print("Congratulations! You were born on", birthmonth, "/", birthday, "/", birthyear)
    
    def printAddress(self):
        print(self.streetVar.get())
        print(self.cityVar.get(), ",", self.stateVar.get(), self.zipVar.get())

    def resetForm(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.frame5.destroy()
        self.frame6.destroy()

    def submitForm(self):
        invalidCount = 0
        
        # validate name
        name = self.firstNameVar.get() + self.lastNameVar.get()
        invalidNameChars = 0
        for i in range(len(name)):
            if name[i].isalpha() == False and name[i] != "," and name[i] != "-" and name[i] != " ":
                invalidNameChars += 1
        if invalidNameChars > 0 or len(name) == 0:
            invalidCount += 1
            print("Invalid name!")
            

        # validate telephone
        number = self.phoneVar.get()
        nonNumbers = 0
        for i in range(len(number)):
            if number[i].isdigit() == False:
                nonNumbers += 1
        if nonNumbers > 0 or len(number) != 10:
            invalidCount += 1
            print("Invalid telephone number!")

        # validate birthday
        birthmonthStr = self.birthmonthVar.get()
        birthmonth = eval(birthmonthStr.lstrip('0'))
        birthdayStr = self.birthdayVar.get()
        birthday = eval(birthdayStr.lstrip('0'))
        birthyear = eval(self.birthyearVar.get())

        if birthmonth < 1 or birthmonth > 12:
            invalidCount += 1
            print("Invalid birth date!")
        elif (birthmonth == 2 and birthday > 29) or birthday < 1:
            invalidCount += 1
            print("Invalid birthday!")
        elif (birthmonth == 4 or birthmonth == 6 or birthmonth == 9 or birthmonth == 11) and birthday > 30 or birthday < 1:
            invalidCount += 1
            print("Invalid birthday!")
        elif (birthmonth == 1 or birthmonth == 3 or birthmonth == 5 or birthmonth == 7 or birthmonth == 8 or birthmonth == 10 or birthmonth == 12) and birthday > 31 or birthday < 1:
            invalidCount += 1
            print("Invalid birth date!")

        if birthyear < 1900 or birthyear > 2013:
            print("Invalid birth date!")
        
        # validate email
        email = self.emailVar.get()
        atSymbols = 0
        dots = 0
        for i in range(len(email)):
            if email[i] == "@":
                atSymbols += 1
            if email[i] == ".":
                dots += 1
        if atSymbols != 1 or dots != 1:
            invalidCount += 1
            print("Invalid email address!")
        
        # check if all valid
        if invalidCount == 0:
            print("Name, telephone, birthdate, and email address fields appear to be valid.")
                

ValidateInfo() # Create GUI
