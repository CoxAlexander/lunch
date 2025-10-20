"""
Alexander Cox
10/17/2025
Goal make a working gui application that can take input from a barcode scanner and keyboard to accurately store the information for the 
lunch room that can then be input into facts to store that information.

To Do:
Make GUI
Figure out how to make the scanner import data
what data needs to be stored
make plan for how to organize the data
"""
#imports
from tkinter import *
from math import floor

#Main class
class gui:
    #defining the main window
    def __init__(self):
        #variables
        self.counter = 0
        self.counterY = 0
        self.changes: bool = False
        self.currentOrder: list = []
        self.currentName: StringVar = ""
        self.currentID: int = 0
        self.currentPrice: list = []
        self.totalCost: float = 0
        self.currentList:list =[self.currentName, self.currentID, self.currentOrder, self.currentPrice, self.totalCost]
        self.catagories:list = menuWindow.categories

        #GUI
        self.root = Tk()
        self.root.title("Lunch")

        #Menu bar
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)

        #menu options
        self.file_menu = Menu(self.menuBar, tearoff=0)
        self.menu_menu = Menu(self.menuBar, tearoff=0)

        #adding command to the file menu option
        self.file_menu.add_command(label = 'Exit', command = self.exit)
        self.menu_menu.add_command(label='Change Menu', command = self.menu)
        
        #add the menu options onto the menu bar
        self.menuBar.add_cascade(label="File", menu=self.file_menu)
        self.menuBar.add_cascade(label='Menu', menu=self.menu_menu)

        #   Full screen
        self.screenHeight:int = self.root.winfo_screenheight()
        self.screenWidth:int = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (self.screenWidth,self.screenHeight))
        
        #Label that stores the total of the transactions
        self.totalLabel = Label(self.root, font = ("Times New Romans", 40), text = "$0.00", borderwidth=1, relief= SOLID, background="#BCA5F8")
        self.totalLabel.place(relx = 0.8, rely=0.8, relheight=0.2, relwidth=0.2)

        #Label that stores all the items and their cost
        self.itemsLabel=Label(self.root, font = ("Times New Romans",20), text = "test2\ntest3\ntest4", borderwidth=1, relief= SOLID, background="#838383")
        self.itemsLabel.place(relx=0.8, rely=0, relheight=0.8, relwidth=0.2)
        
        #catagories 
        for cat in self.catagories:
            self.catLabel = Label(self.root,text=cat, font=("Times New Romans",15), borderwidth=1, relief=SOLID)
            self.catLabel.place(relx=((self.counter)*0.1),rely=0.05+(floor(self.counterY/8)*0.1),relheight=0.05,relwidth=0.1)
            self.counter += 1
            self.counterY += 1
            if self.counter >= 8:
                self.counter = 0
        
        self.root.mainloop()
    
    #button function that adds item to the total and changes the change variable to true
    def add(self):
        pass
    
    #adds the curent data of the student to be stored
    def confirm(self):
        pass

    #exits the program and asks to save if changed variable is set to true
    def exit(self):
        if (self.changes):
            pass
        else:
            self.root.destroy()
            

    #Opens the menu window to change the menu and its prices
    def menu(self):
        if (self.changes):
            pass
        else:
            self.root.destroy()
            menuWindow()

    #exports the current data as a csv and resets the change variable to false
    def save(self):
        pass

    #stores all the current items in the list allowing items to also be removed and keeps track of the total cost
    def total(self):
        pass

#a subclass of the main that has the menu and ability to change what the menu is
class menuWindow():
    categories: list = [1,2,3,4,5,6,7,8,9,10,"asdfghjklqwerty"]
    #The menu gui settings that are different from main
    def __init__(self):
        
        #variables
        self.changes: bool = False
        self.counter = 0
        self.counterY = 0
        self.root = Tk()
        self.root.title("Menu")
        index = 0
        #menu bar commands
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)
        self.file_menu = Menu(self.menuBar, tearoff=0)
        self.file_menu.add_command(label="Order", command=self.main)
        self.file_menu.add_command(label = 'Exit', command = self.exit)
        self.menuBar.add_cascade(label="File", menu=self.file_menu)
        
        for cat in menuWindow.categories:
            self.catTitle = Label(self.root, text=cat, font=("Times New Romans", 15),borderwidth=1, relief=SOLID)
            self.catTitle.place(relx=(0.05+(self.counter)*0.1),rely=0.05+(floor(self.counterY/9)*0.1),relheight=0.05,relwidth=0.1)
            self.catDelete = Button(self.root,text="Delete", command =lambda: self.removeCategory(index))
            self.catDelete.place(relx=(0.05+(self.counter)*0.1),rely=0.1+(floor(self.counterY/9)*0.1),relheight=0.05,relwidth=0.1)
            self.counter += 1
            self.counterY += 1
            index += 1
            if self.counter >8:
                self.counter =0
        #screen size
        self.screenHeight:int = self.root.winfo_screenheight()
        self.screenWidth:int = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (self.screenWidth,self.screenHeight))

        #buttons
        self.addCatButton = Button(self.root, text="Add Category", command=self.addCategory)
        self.addCatButton.place(relx=0.1,rely=0.8,relheight=0.05,relwidth=0.05)

    #adds a category to the page
    def addCategory(self):
        #title
        self.addCatWindow = Tk()
        self.addCatWindow.title("Add a Category")

        #buttons and inputs
        self.catLabel = Label(self.addCatWindow, text="Name of Category" , font=("Times New Romans",12))
        self.catLabel.place(relx=0.025,rely=0.1,relwidth=1,relheight=0.2) 
        self.catInput = Text(self.addCatWindow, height=1, width=15,wrap=None)
        self.catInput.place(relx=0.2,rely=0.3)
        self.catConfirm = Button(self.addCatWindow, text="Confirm", font= ("Times New Romans",10), command= self.addCatConfirm)
        self.catConfirm.place(relx=0.6, rely=0.7, relwidth=0.25, relheight=0.2)
        self.catCancel = Button(self.addCatWindow, text= "Cancel", font= ("Times New Romans",10), command=lambda :self.addCatWindow.destroy())
        self.catCancel.place(relx=0.2,rely=0.7, relwidth=0.25, relheight=0.2)

    #confirm and add category to list
    def addCatConfirm(self):
        menuWindow.categories.append(self.catInput.get('1.0', 'end-1c'))
        self.addCatWindow.destroy()
        self.catTitle = Label(self.root, text=menuWindow.categories[-1], font=("Times New Romans", 15))
        self.catTitle.place(relx=((self.counter)*0.1),rely=0.05+(floor(self.counterY/9)*0.1),relheight=0.05,relwidth=0.1)
        self.counterY += 1
        self.counter += 1
        if self.counter > 8:
                self.counter = 0
        self.root.update()        
    
    #adds a price to a category
    def addPrice(self):
        pass
    
    #exits to main after saving the changes to a database
    def exit(self):
        if (self.changes):
            pass
        else:
            self.root.destroy()

    #goes back to the main GUI menu
    def main(self):
        if (self.changes):
            pass
        else:
            self.root.destroy()
            gui()


    #removes a category from the page
    def removeCategory(self,index):
        print(index)
        print(self.categories[10])
        self.categories.remove(self.categories[index])
        print(self.categories)

    #removes a price from a category
    def removePrice(self):
        pass
    
if __name__ == "__main__":
    gui()