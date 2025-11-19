from tkinter import *
import csv
from time import sleep
import pynput
import pynput.keyboard
import threading
import re
import pyautogui
import sys

def confirm():
    global totalInput
    global codeList
    global nameLabel
    global name
    global root
    priceInput:str = totalInput.get('1.0', 'end-1c')
    #regex looking for a 2 digit then a possible . and 2 more digits
    pattern = re.compile(r"\d{1,2}(\.\d{1,2})?")
    match = pattern.match(priceInput)
    if match != None:
        price = re.search(r"\d{1,2}(\.\d{1,2})?",priceInput)
        with open('LunchInfo.csv', 'a',newline='') as lunchInfo:
             writer = csv.writer(lunchInfo, delimiter=",")
             writer.writerow([name,price.group(0)])
        name = ""
        totalInput.delete("1.0",END)
        nameLabel.focus_set()
        codeList = []
        nameLabel.config(text=name)
        root.update()

def load():
    global studentDict
    global name
    global listener
    global codeList
    global staffDict
    staffDict = {}
    codeList = []
    studentDict = {}
    name = ""
    
    with open('studentID.csv') as studentID:
            csv_reader = csv.reader(studentID, delimiter=',')
            for row in csv_reader:
                studentDict[row[0]] = f"{row[1]} {row[2]}"
    with open('staffID.csv') as staffID:
        csv_reader = csv.reader(staffID, delimiter=',')
        for row in csv_reader:
            staffDict[row[0]] = f"{row[1]} {row[2]}"
    with pynput.keyboard.Listener(on_press = scan) as listener:
        listener.join()
   
def scan(Key):
        global studentDict
        global staffDict
        global nameLabel
        global root
        global name
        global totalInput
        global codeList
        try:
            if type(Key.char) is str:
                codeList.append(Key.char)
                code = "".join(codeList)

            if (code in studentDict):
                name = studentDict[code]
                codeList = []
                sleep(1)
                totalInput.focus_set()
                pyautogui.press("backspace")
                nameLabel.config(text=name)
                root.update()
            if (code in staffDict):
                name = staffDict[code]
                codeList = []
                sleep(1)
                totalInput.focus_set()
                pyautogui.press("backspace")
                nameLabel.config(text=name)
                root.update()
            if len(codeList) > 7:
                codeList = []
        except Exception as e:
            pass

def reload():
    global nameLabel
    global name
    global root
    global codeList

    name = ""
    nameLabel.focus_set()
    codeList = []
    nameLabel.config(text=name)
    root.update() 

def exit():
    root.destroy()
    sys.exit()
    

def gui():
    global root
    global nameLabel
    global totalInput
    global name
    root = Tk()
    root.title("Lunch")
    #Full screen
    screenHeight:int = root.winfo_screenheight()
    screenWidth:int = root.winfo_screenwidth()
    root.protocol("WM_DELETE_WINDOW",exit)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    root.columnconfigure(2,weight=1)
    root.rowconfigure(0,weight=2)
    root.rowconfigure(1,weight=1)
    root.rowconfigure(2,weight=1)
    root.rowconfigure(3,weight=1)
    root.geometry("%dx%d" % (screenWidth/5,screenHeight/5))
    nameLabel = Label(root, font = ("Times New Romans", 18),text = name)
    nameLabel.grid(row=0,column=1)
    totalLabel = Label(root,font= ("Times new Romans",15), text="Enter the total")
    totalLabel.grid(row=1, column=1)
    totalInput = Text(root, height=1 , width=10, wrap = None)
    totalInput.grid(row=2,column=1)
    totalButton = Button(root, font=("Times New Romans", 15), text="Confirm" , command=confirm)
    totalButton.grid(row = 3, column= 1)
    reloadButton  = Button(root, font=("Times New Romans", 15), text="Reload", command=reload)
    reloadButton.grid(row = 3, column= 0)
    exitButton  = Button(root, font=("Times New Romans", 15), text="Exit", command=exit)
    exitButton.grid(row = 3, column= 2)
    root.mainloop()

if __name__ == "__main__":
    global t
    global th
    t = threading.Thread(target=gui)
    th = threading.Thread(target=load)
    th.daemon = True
    t.start()
    th.start()
    
    
   
