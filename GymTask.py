#Imports the two libraries necessary to make windows and to display error messages.
import tkinter
from tkinter import messagebox
from tkinter import font
#These are used to store the password file in a .env file to allow the user to share the program without having to reveal the password.
import os
from dotenv import load_dotenv

#This loads the password from the .env file stored in the same directory as the python file.
load_dotenv()
password=os.getenv("PASSWORD")

#Function that is used by the exit button on the main screen that closes the main window and exits the program.
def closeProgram():
    window.destroy()

#Class that is used to create objects that represent each person who has data stored in the file.
class clubMember:

    def __init__(self, name, press_ups, pull_ups):
        self.name=name
        self.press_ups=int(press_ups)
        self.pull_ups=int(pull_ups)
listOfMembers=[]

#This loads the file as an object then reads the first line.
file = open("gymclub.txt", "r")
line = file.readline()

#This ensures that all data in the file is loaded and processed.
while line!="":
    #This creates three variables from the data in each row which is then used to create objects that are appended to the listOfMembers
    name, press_ups, pull_ups = line.strip().split(",")
    listOfMembers.append(clubMember(name, press_ups, pull_ups))
    #This then loads the next line in the file.
    line=file.readline()

#This function sorts the data by the chosen statistic and then prints it in formatted rows and columns.
def displaySortedData(sortKey, sortedBy):
    global window
    global listOfMembers
    #First it sorts the data and closes the old window.
    sortedList=sorted(listOfMembers, key=sortKey)
    window.destroy()
    #Then it creates a new window with the same title and a width of 400 and height of 400
    window=tkinter.Tk()
    window.title("Gym Club")
    window.geometry("400x400")
    #Then it creates a message that tells the user how they chose to sort their data
    tkinter.Label(window, text=f"Your data has been sorted by {sortedBy}.", font="Helvetica 12").grid(row=0, columnspan=3)
    #Then it creates some headers for the table
    tkinter.Label(window, text="Name:", font="Helvetica 12").grid(row=1, column=0)
    tkinter.Label(window, text="Press-ups:", font="Helvetica 12").grid(row=1, column=1)
    tkinter.Label(window, text="Pull-ups:", font="Helvetica 12").grid(row=1, column=2)
    #Then it uses two counters and two for loops to print out all of each person's statistics on the window in rows and columns.
    objectCounter=2
    for x in sortedList:
        attributeCounter=0
        for y in [x.name, x.press_ups, x.pull_ups]:
            tkinter.Label(window, text=y, font="Helvetica 12", fg="blue").grid(row=objectCounter, column=attributeCounter)
            attributeCounter+=1
        objectCounter+=1
    #This then creates a return button that the user can use to go back to the previous menu.
    tkinter.Button(window, text="Back", font="Helvetica 12", command=chooseSortingMethod, fg="red").grid(row=objectCounter+1, columnspan=3)

#This is the function that is run when the user selects the button to print user data
#This allows the user to select how to sort the data.
def chooseSortingMethod():
    #First it destroys the old window
    global window
    window.destroy()
    #THen it creates a new window 400 wide and 100 tall, with the title "Gym Club"
    window=tkinter.Tk()
    window.geometry("400x100")
    window.title("Gym Club")
    #This makes one label to instruct the user to select the sorting method as well as three buttons,
    #two of which allow the user to select the sorting method, the third allows the user to return to the previous menu.
    tkinter.Label(window, text="Please choose how you would like the data to be organised.", font = "Helvetica 11").grid(row=0, columnspan=2)
    tkinter.Button(window, text="By Press-Ups", fg="blue", font="Helvetica 10", command=lambda :displaySortedData(lambda x:x.press_ups, "press-ups")).grid(row=1, column=0)
    tkinter.Button(window, text="By Pull-Ups", fg="blue", font="Helvetica 10", command=lambda :displaySortedData(lambda x:x.pull_ups, "pull-ups")).grid(row=1, column=1)
    tkinter.Button(window, text="Back", fg="red", font="Helvetica 10", command=lambda :verifyUsr(True)).grid(row=2, columnspan=2)



#The function that verifies the user's password and if correct does block of code #1 or if incorrect does block of code #2
#However, the skipCheck variable is used to check if the user is returnign to this screen from another, in which case, it skips the password check.
def verifyUsr(skipCheck=False):
    global window
    global pwdEntry
    usrPassword=""
    try:
        usrPassword=pwdEntry.get()
    except:
        pass
    '''Block of code #1
    If the password is correct (i.e. is "password123") then the password entry window is closed
    and a new window is displayed with an option to print users' data or to exit.'''
    if (usrPassword==password) or skipCheck:
        window.destroy()
        window=tkinter.Tk()
        window.geometry("250x100")
        window.title("Gym Club")
        tkinter.Label(window, text="Welcome to the Gym Club App", font = "Helvetica 12").grid(row=0, columnspan=2)
        tkinter.Label(window, text="Please choose an option", font = "Helvetica 12").grid(row=1, columnspan=2)
        tkinter.Button(window, text="Print out user data", fg = "green", font = "Helvetica 12", command=chooseSortingMethod).grid(row=2, column=0)
        tkinter.Button(window, text="Exit Program", fg="red", command=closeProgram, font = "Helvetica 12").grid(row=2, column=1)
        window.rowconfigure((0,1), weight=1)
        window.columnconfigure((0,2), weight=1)
        '''Block of code #2
        If the password is incorrect then the password entry window remains and the user is shown a popup
        informing them of the invalid/incorrect password.'''
    else:
        messagebox.showerror(title="Error", message="Invalid Password, Please try again.")

#Function to run when the program runs.
def main():
    global window
    global pwdEntry

    #Creates the main window for the user to enter the password with the width 300 and height 150
    window=tkinter.Tk()
    window.geometry("250x100")
    window.title("Gym Club")


    #Adds text to the window that says "Please enter password", an entry for the password and a button to retrieve the password and run a command to verify it.
    tkinter.Label(window, text="Please enter password", width = "20", height = "1", font="Helvetica 12").pack()
    pwdEntry=tkinter.Entry(window, font = "Helvetica 12")
    pwdEntry.pack(ipadx=40, ipady=5)
    tkinter.Button(window, text="Enter", fg="green", command=verifyUsr, width = 15, height = 2, font = font.Font(family='Helvetica', size=12)).pack()

    #This displays the main window.
    window.mainloop()

main()
