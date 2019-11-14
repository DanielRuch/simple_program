# Basic Form with Open File Dialog
# Read in CSV
import os # This will allow us to create file paths across operating systems
import csv # Module for reading CSV files
from tkinter import filedialog
from tkinter import *
import tkinter as tk #Module for some new user input options
import tkinter.filedialog as tkFileDialog

#Get path to the folder this file is in
rootFolderPath = os.path.dirname(os.path.abspath(__file__))
formNumber = 0
formMaxNum = 0
formList = []
formNameList = []

### Create App Class
class App(object):
    """"""
    #----------------------------------------------------------------------
    #Initialize class
    def __init__(self, parent):
        """Constructor"""
        self.root = parent #Set parent variable
        self.root.title("Main Window") #Set title of root
        self.c_Main = tk.Frame(parent, name="main_container") #Create frame to serve as main container
        self.c_Main.grid(sticky="WENS") #Stick West, East, North, South

    #----------------------------------------------------------------------
    #Opens Open File Dialog. Returns path to the file selected
    def fileDialogOpen(self, initialdir=rootFolderPath):
        #Open file dialog through tkinter
        output = tkFileDialog.askopenfilename(initialdir=initialdir)
        return output

class Window(App):

    #----------------------------------------------------------------------
    # Create button. Return widget control
    def makeButton(self, master, row, column, width=0, height=0, text="default", fgcolor="black", bgcolor="gainsboro", command=quit, padx=0, pady=0, sticky=""):
        #Create Button
        button = tk.Button(master=master, width=width, height=height, text=text, fg=fgcolor, bg=bgcolor, command=command)
        button.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return button
    
    #----------------------------------------------------------------------
    # Create Entry field. Return widget control
    def makeEntry(self, master, row, column, variable=StringVar, width=100):
        #Create Entry field
        entry = Entry(master=master, textvariable=variable, width=width)
        entry.grid(row=row, column=column)
        return entry
    
    #----------------------------------------------------------------------
    # Create frame. Return widget control
    def makeFrame(self, master, name, width, height, row, column, rowspan=1, columnspan=1, bg="gainsboro", bd=0, relief="flat", padx=0, pady=0, sticky="", gridprop=True):
        #Create frame
        frame = tk.Frame(master=master, name=(name.lower()), width=width, height=height, bg=bg, bd=bd, relief=relief)

        #Check grid propagation settings. Defaults to True
        if gridprop == False:
            frame.grid_propagate(False)
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return frame
    
    #----------------------------------------------------------------------
    def makeLabel(self, master, name, width, height, row, column, rowspan=1, columnspan=1, text="", bg="gainsboro", bd=0, relief="flat", padx=0, pady=0, sticky="", gridprop=True):
        #Create label
        label = tk.Label(master=master, name=(name.lower()), text=text, width=width, height=height, bg=bg, bd=bd, relief=relief)

        #Check grid propagation settings. Defaults to True
        if gridprop == False:
            label.grid_propagate(False)
        label.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return label

    #----------------------------------------------------------------------
    #Show the window
    def show(self):
        """"""
        #Update root, deiconify
        self.root.update()
        self.root.deiconify()

    #----------------------------------------------------------------------
    #Hide the window
    def hide(self):
        """"""
        self.root.withdraw()

    #----------------------------------------------------------------------
    #Close the window
    def close(self):
        self.root.destroy()
    
#----------------------------------------------------------------------

#Generate Form Layouts

#Footer form
def genFooter(formWidth):
    #Footer containter frame, horizontal spacer, vertical spacer
    c_Footer = formMain.makeFrame(master= formMain.c_Main, name="footer_container", width=formWidth, height=100, row=2, column=1, bd=2, pady=5, relief="groove", gridprop=True)
    f_ftrHSpacer = formMain.makeFrame(master=c_Footer, name="footer_Hspacer", width=formWidth, height=10, row=10, column=1, columnspan=10)
    f_ftrVSpacer = formMain.makeFrame(master=c_Footer, name="footer_vspacer", width=1, height=10, row=1, column=10, rowspan=10)

    #Create buttons
    b_Close = formMain.makeButton(master=c_Footer,row=9, column=1, text="Close", command=clearForm, fgcolor="red", padx=10, pady=10, sticky="SW")   #Close Button, bottom left
    b_Next = formMain.makeButton(master=c_Footer,row=9, column=10, text="Next", command=lambda: nextButtonClick(b_Back, b_Next), padx=10, pady=10, sticky="SE") #Next button, bottom right
    b_Back = formMain.makeButton(master=c_Footer,row=9, column=2, text="Back", command=lambda: backButtonClick(b_Back, b_Next), padx=10, pady=10, sticky="SW") #Next button, bottom right

    #If starting on first form, disable back button
    global formNumber
    if formNumber <= 0:
        #b_Back.grid_forget()
        b_Back.configure(state='disabled')

#Input screen form
def genScreenInputFile(formwidth):
    #Increase max form number
    global formMaxNum
    formMaxNum += 1

    #Update Window Title
    windowTitle = "File Select"
    formMain.root.title(windowTitle)

    #Store frame/container for File Select screen UI elements
    c_FileSelect = formMain.makeFrame(name="fileselect_container", master=formMain.c_Main, width=200, height=100, row=1, column=1, bd=2, relief="groove", gridprop=True) #, bg="red"
    
    #Add UI Element containers and Title to lists
    formList.append([c_FileSelect, windowTitle])
    
    #Create UI Elements
    #Horizontal and vertical spacers to set window height
    f_FSHSpacer = formMain.makeFrame(master=c_FileSelect, name="footer_Hspacer", width=formwidth, height=10, row=10, column=1, columnspan=10)
    #f_FSVSpacer = formMain.makeFrame(master=c_FileSelect, name="footer_vspacer", width=1, height=200, row=1, column=10, rowspan=10)

    #Create label for file path
    l_FPLabel = formMain.makeLabel(master=c_FileSelect, name="FS_fplabel", width=50, height=10, row=2, column=3, text="Enter path of file to open:", sticky="NW")

    #Create file path entry box; bind filepath entry variable
    filepath = StringVar()
    e_FPEntry = formMain.makeEntry(master=c_FileSelect, row=3, column=3, variable=filepath, width=50)

    #Create browse button
    b_Browse = formMain.makeButton(master=c_FileSelect,row=3, column=4, text="Browse", command=lambda: browseButtonClick(filepath))
    
    #COOL NOTE: lambda allows for passing an argument without invoking the method. Really cool stuff!

def genScreenParameters(formwidth):
    #Increase max form number
    global formMaxNum
    #formMaxNum += 1
    #Window Title
    windowTitle = "Parameters"

    #Store frame/container for File Select screen UI elements
    c_Parameters = formMain.makeFrame(name="parameter_container", master=formMain.c_Main, width=200, height=100, row=1, column=1, bd=2, relief="groove", gridprop=True) #, bg="red"
    f_PHSpacer = formMain.makeFrame(master=c_Parameters, name="footer_Hspacer", width=formwidth, height=10, row=10, column=1, columnspan=10)
    f_PVSpacer = formMain.makeFrame(master=c_Parameters, name="footer_vspacer", width=1, height=200, row=1, column=10)
    e_testEntry = formMain.makeEntry(master=c_Parameters, row=2, column=3, variable=readFilePath, width=50)     #Entry box for path of file to open

    #Add UI Element containers and Title to lists
    formList.append([c_Parameters, windowTitle])

    #Hide element after generated
    c_Parameters.grid_forget()

def reset(container):
    container.grid_forget()

def nextButtonClick(backbutton, nextbutton):
    #Increase form number
    global formNumber
    global formMaxNum
    formNumber += 1

    #Hide previous form
    formList[formNumber-1][0].grid_forget()

    #Show next form
    formMain.root.title(formList[formNumber][1])
    formList[formNumber][0].grid(row=1, column=1)

    #If no longer on first form, undither/unhide back button
    if formNumber >= 1:
        backbutton.grid()
    #If on form other than first, undither back button
    if formNumber >= 1:
        backbutton.configure(state='normal')

    #If on last form, dither next button
    if formNumber >= formMaxNum:
        nextbutton.configure(state='disabled')
    
def backButtonClick(backbutton, nextbutton):
    #Decrease form number
    global formNumber
    formNumber -=1

    #Hide current form
    formList[formNumber+1][0].grid_forget()

    #Show previous form
    formMain.root.title(formList[formNumber][1])
    formList[formNumber][0].grid(row=1, column=1)

    #If on first form, dither the back button
    if formNumber <= 0:
        #backbutton.grid_forget()
        backbutton.configure(state='disabled')

    #If on form other than last, undither next button
    if formNumber < formMaxNum:
        nextbutton.configure(state='normal')

def browseButtonClick(filepath):
    #Open File Dialog and store response
    #Set input entry value
    filepath.set(formMain.fileDialogOpen())
    #return output

def clearForm():
    formMain.close()
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    formMain = Window(root)

#Build main form

#Build Form to get path of file to open from user
readFilePath = StringVar()
genFooter(600)
genScreenInputFile(600)
genScreenParameters(600)

root.mainloop()

########################
