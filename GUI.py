# Importing all the important libraries
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

import pandas as pd     # Importing pandas for managing csv data
from datetime import date
from datetime import datetime
from csv import writer
import csv
import numpy as np      # Importing numpy for getting the index of the required value

class WEBGURU:          # Creating the main class for tkinter
    def __init__(self):
        self.root=Tk() 
        self.root.title('WEB GURU')     # Adding the title to tkinter GUI
        self.root.geometry("600x500")   # Defining the size of main window
        self.root.configure(bg="#FFBA7A")   #Defining background color of tkinter window
        self.df = pd.read_csv("sampledata.csv")     # Opening up the csv file
        self.create_widgets()
    def create_widgets(self):
        self.c0 = Canvas(self.root,bg = "#FFBA7A",bd=0, highlightthickness=0, relief='ridge')
        self.c0.place(x = 0, y  = 0, width = 600,height = 500)  #   Defining a new canvas on the the window
        #   Adding label on canvas
        Label(self.c0,text='Action Pannel',font=("Georgia 13 bold",15),bg="#FFBA7A").place(x=240,y=50)
        #   Adding buttons on the canvas
        Button(self.c0,text='Create',relief = "groove",bg="#FFBA7A",font=("Georgia 13 bold",10),command=self.create).place(x=240,y=100,width=120,height=30)
        Button(self.c0,text='Read',relief = "groove",bg="#FFBA7A",font=("Georgia 13 bold",10),command=self.read).place(x=240,y=150,width=120,height=30)
        Button(self.c0,text='Update',relief = "groove",bg="#FFBA7A",font=("Georgia 13 bold",10),command=self.update).place(x=240,y=200,width=120,height=30)
        Button(self.c0,text='Delete',relief = "groove",bg="#FFBA7A",font=("Georgia 13 bold",10),command=self.delete).place(x=240,y=250,width=120,height=30)
        Button(self.c0,text='Exit',relief = "groove",bg="#FFBA7A",font=("Georgia 13 bold",10),command=self.root.destroy).place(x=240,y=300,width=120,height=30)
        # Adding the munubar on the canvas
        menubar = Menu(self.root)  
        file = Menu(menubar, tearoff=0)  # Creating File Menu
        file.add_command(label ='Create', command = self.create)
        file.add_command(label ='Read', command = self.read)
        file.add_separator() 
        file.add_command(label ='Exit', command = self.root.destroy)   
        menubar.add_cascade(label="File", menu=file)  
        
        edit = Menu(menubar, tearoff=0)  
        edit.add_command(label ='Update', command = self.update)
        edit.add_command(label ='Delete', command = self.delete)          
        menubar.add_cascade(label="Edit", menu=edit)  

        help = Menu(menubar, tearoff=0)  
        help.add_command(label="About", command = self.about)  
        menubar.add_cascade(label="Help", menu=help)

        self.root.config(menu=menubar)
    #   Definig the create function
    def create(self):
        self.c1 = Canvas(self.root,bg = "#FFBA7A",bd=0, highlightthickness=0, relief='ridge')# Defining canvas for create window
        self.c1.place(x = 0, y  = 0, width = 600,height = 500)
        ## Defining labels
        Label(self.c1,text='CREATE',font=("Georgia 13 bold",30),bg="#FFBA7A").place(x=200,y=20)
        Label(self.c1,text='Priorities: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=80)
        Label(self.c1,text='Categoriies: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=120)
        # Defining dropdown menus
        self.priority = StringVar()
        self.category = StringVar()
        self.priority.set("M")
        self.category.set("SOD")
        self.drop_list = ["M","S","W","D"]
        self.category_list = ['SOD','FCS','Personal','CPD','PERS','MEN',"PPR"]
        
        self.drop_1 = OptionMenu(self.c1 , self.priority, *self.drop_list).place(x = 250,y = 80,width=150)
        self.drop_2 = OptionMenu(self.c1 , self.category, *self.category_list).place(x = 250,y = 120,width=240)

        Label(self.c1,text='Details: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=160)
        #   Defing Entry Widget
        self.detail = StringVar()
        Entry(self.c1,textvariable=self.detail).place(x = 250, y = 160, width = 300, height=30)

        Label(self.c1,text='Deadline(DD/MM/YYYY):',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=200)
        
        self.deadline = StringVar()
        Entry(self.c1,textvariable=self.deadline).place(x = 250, y = 200, width = 300, height=30)

        Label(self.c1,text='Is task complete?:',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=240)
        
        self.complete = StringVar()
        self.complete.set("N")
        self.complete_list = ["N","Y"]
        self.drop_3 = OptionMenu(self.c1 , self.complete, *self.complete_list).place(x = 250,y = 240,width=240)

        self.today = date.today()
        self.dateOfEntry = self.today.strftime("%d/%m/%Y")

        self.task_id = int(max(self.df["Task ID"])) + 1
        # Defining two buttons for submit and back
        Button(self.c1,text='Submit',font=("Georgia 13 bold",14),bg="#FFBA7A",command=self.create_done).place(x=70,y=300,width = 200)
        Button(self.c1,text='<<Back',font=("Georgia 13 bold",14),bg="#FFBA7A",command=self.create_widgets).place(x=280,y=300,width = 200)
    # Defining function for submit button
    def create_done(self):
        #   Validating the entry
        if "/" not in self.deadline.get():
            messagebox.showerror("Error","Please Insert '/' character in Deadline(DD/MM/YYYY)!")
            self.create()
        else:
            #   CCreating a list of new data
            self.new_row = [self.task_id, self.priority.get(), self.category.get(), self.detail.get(), self.dateOfEntry, self.deadline.get(), self.complete.get()]
            with open("sampledata.csv", "a", newline='') as f_object:
                # Adding the created list to the csv
                new_object = writer(f_object)
                new_object.writerow(self.new_row)
                f_object.close()
                messagebox.showinfo("Done!","New Task is created successfully")
    #   Definign function for read

    def about(self):
        self.c = Canvas(self.root,bg = "#FFBA7A",bd=0, highlightthickness=0, relief='ridge')
        self.c.place(x = 0, y  = 0, width = 600,height = 500)

        Label(self.c,text='Welcome to this App. This app performs CRUD functions',font=("Georgia 13 bold",10),bg="#FFBA7A").place(x=100,y=20)
        Button(self.c,text='<<Back',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.create_widgets).place(x=200,y=460,width = 200)
    def read(self):
        # Creating all the widgets, dropdown menus, buttons and labels and entry widgets
        self.data = pd.read_csv("sampledata.csv")
        self.c2 = Canvas(self.root,bg = "#FFBA7A",bd=0, highlightthickness=0, relief='ridge')
        self.c2.place(x = 0, y  = 0, width = 600,height = 500)

        Label(self.c2,text='Read',font=("Georgia 13 bold",30),bg="#FFBA7A").place(x=200,y=20)
        Label(self.c2,text='Action: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=80)
        Label(self.c2,text='Category: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=120)

        self.category = StringVar()
        Entry(self.c2,textvariable=self.category).place(x = 150, y = 120, width = 200, height=30)

        Button(self.c2,text='Submit',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.read_done).place(x=400,y=120,width = 100)
        Button(self.c2,text='<<Back',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.create_widgets).place(x=200,y=460,width = 200)
        
        self.task = StringVar()
        self.task.set("List all task.")
        self.task_list = ["List all task.","Search & display details for all tasks of particular category","Count the number of completed tasks as a percentage"]
        self.drop_4 = OptionMenu(self.c2 , self.task, *self.task_list).place(x = 150,y = 80,width=350)
    def read_done(self):
        self.selection = self.task.get()
        #   Creating a treevie for listing all the details of the csv file
        if self.selection == "List all task.":
            self.row = ("Id", "Priority", "Category", "Detail", "Date Of Entry", "Deadline", "Completed")
            self.tree=ttk.Treeview(self.c2,height=13,column=self.row,show='headings')
            
            self.tree.heading('Id', text="Id", anchor=W)
            self.tree.heading('Priority', text="Priority", anchor=W)
            self.tree.heading('Category', text="Category", anchor=W)
            self.tree.heading('Detail', text="Detail", anchor=W)
            self.tree.heading('Date Of Entry', text="Date Of Entry", anchor=W)
            self.tree.heading('Deadline', text="Deadline", anchor=W)
            self.tree.heading('Completed', text="Completed", anchor=W)

            self.tree.column('#1', stretch=NO, minwidth=0, width=25)
            self.tree.column('#2', stretch=NO, minwidth=0, width=80)
            self.tree.column('#3', stretch=NO, minwidth=0, width=120)
            self.tree.column('#4', stretch=NO, minwidth=0, width=120)
            self.tree.column('#5', stretch=NO, minwidth=0, width=80)
            self.tree.column('#6', stretch=NO, minwidth=0, width=80)
            self.tree.column('#7', stretch=NO, minwidth=0, width=60)
            self.tree.place(x = 20 , y = 170)
        
            with open('sampledata.csv') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    ID = row['Task ID']
                    priority = row['Priority']
                    category = row['Category']
                    detail = row['Details']
                    doe = row['Date of Entry']
                    deadline = row['Deadline']
                    com = row['Complete']
                    self.tree.insert("", 0, values=(ID, priority,category,detail,doe,deadline,com))
        #   Selecting the particular category and then displaying it in the labels
        elif self.selection == "Search & display details for all tasks of particular category":
            self.category_df = self.data[self.data["Category"]==self.category.get().upper()]
            y = 160
            for detail in self.category_df["Details"]:
                Label(self.c2,text=detail,font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=y)
                y+=30
        #   Counting the percenntage of completed task
        elif self.selection == 'Count the number of completed tasks as a percentage':
            completed_tasks = self.df["Complete"].value_counts(normalize=True)["Y"] * 100
            Label(self.c2,text=completed_tasks,font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=50,y=160)
       
        Button(self.c2,text='<<Back',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.read).place(x=200,y=460,width = 200)
    
    # Defining the function for update button
    def update(self):
        # Defininf all the widgets 
        self.data = pd.read_csv("sampledata.csv")

        self.c3 = Canvas(self.root,bg = "#FFBA7A",bd=0, highlightthickness=0, relief='ridge')
        self.c3.place(x = 0, y  = 0, width = 600,height = 500)
        
        Label(self.c3,text='UPDATE',font=("Georgia 13 bold",30),bg="#FFBA7A").place(x=200,y=20)
        Label(self.c3,text='Enter Task Id: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=80)

        self.task_ID = StringVar()
        Entry(self.c3,textvariable=self.task_ID).place(x = 250, y = 80, width = 200, height=30)

        Label(self.c3,text='Select Column: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=120)

        self.column = StringVar()
        self.column.set('Category')
        self.column_list = ['Category','Priority','Details','Date of Entry','Deadline','Complete']
        self.drop_5 = OptionMenu(self.c3 , self.column, *self.column_list).place(x = 250,y = 120,width=240)

        Label(self.c3,text='Enter New Value: ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=160)

        self.new_value = StringVar()
        Entry(self.c3,textvariable=self.new_value).place(x = 250, y = 160, width = 200, height=30)
        
        Button(self.c3,text='Update',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.update_done).place(x=200,y=300,width = 200)
        Button(self.c3,text='<<Back',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.create_widgets).place(x=200,y=350,width = 200)
        
    def update_done(self):
        # Getting the index of of the task ID in the csv file
        index = self.data["Task ID"]==int(self.task_ID.get())
        index = int(np.where(index)[0])
        self.data.at[index,self.column.get()]=self.new_value.get()
        self.data.to_csv("sampledata.csv", index=False)
        # Showing message
        messagebox.showinfo("Updated","The Entry was updated Successfully!")
    # defining the functin for delete button
    def delete(self):
        # Defining all the necessary wwidgets 
        self.data = pd.read_csv("sampledata.csv")

        self.c4 = Canvas(self.root,bg = "#FFBA7A",bd=0, highlightthickness=0, relief='ridge')
        self.c4.place(x = 0, y  = 0, width = 600,height = 500)

        Label(self.c4,text='DELETE',font=("Georgia 13 bold",30),bg="#FFBA7A").place(x=200,y=20)
        Label(self.c4,text='Enter Task Id : ',font=("Georgia 13 bold",14),bg="#FFBA7A").place(x=30,y=80)

        self.task_ID = StringVar()
        Entry(self.c4,textvariable=self.task_ID).place(x = 250, y = 80, width = 200, height=30)
        
        Button(self.c4,text='<<Back',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.create_widgets).place(x=200,y=350,width = 200)
        Button(self.c4,text='Delete',font=("Georgia 13 bold",13),bg="#FFBA7A",command=self.delete_done).place(x=200,y=300,width = 200)
    def delete_done(self):
        #   Getting the index of the Task I d fomcsv file
        new_data = self.data[self.data["Task ID"]!=int(self.task_ID.get())]
        new_data.to_csv("sampledata.csv", index=False)
        messagebox.showinfo("Deleted","The Entry was Deleted Successfully!")
        self.create_widgets()
a = WEBGURU()
mainloop()