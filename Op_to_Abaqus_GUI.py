from mesh.Mesh import Mesh
from Tkinter import Tk, Label, Button, Listbox, END, PhotoImage, RIGHT, LEFT, BOTTOM, TOP
import tkFileDialog


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Optistruct to Abaqus")
        #minusImage = PhotoImage(file="minus_svg.gif")
        #plusImage = ImageTk.PhotoImage(Image.open('plus_svg.png'))
        #minusImage = ImageTk.PhotoImage(Image.open('minus_svg.gif'))
        #plusImage=PhotoImage(file="plus.gif")
        #minusImage=PhotoImage(file="minus.gif")
        
        self.fileList = []
        
        self.label = Label(master, text="Optistruct to Abaqus Conversion")
        self.label.pack()
        
        self.listbox = Listbox(master, width=100)
        self.listbox.pack(side=LEFT)
        
        self.plus_button = Button(master, text='+', width="1", height="1", command=self.addFile)
        self.plus_button.grid(row=0,column=0)
        self.plus_button.pack(side=RIGHT)
        
        self.minus_button = Button(master, text='-', width="1", height="1", command=self.removeFile)
        self.minus_button.grid(row=1,column=0)
        self.minus_button.pack(side=RIGHT)
        
        self.convert_button = Button(master, text="Convert", command=self.convertFiles)
        self.convert_button.grid(row=1,column=0)
        self.convert_button.pack()
        
        self.clear_button = Button(master, text="Clear", command=self.clear)
        self.clear_button.grid(row=2,column=0)
        self.clear_button.pack(side=BOTTOM)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=2,column=1)
        self.close_button.pack(side=BOTTOM)
        
    def removeFile(self):    
        self.listbox.delete(self.listbox.curselection()[0])
        self.fileList.pop(self.listbox.curselection()[0])

    def clear(self):
        self.fileList = []
        self.listbox.delete(0,END)
    
    def convertFiles(self):
        for mesh in self.fileList:
            currMesh = Mesh.fromOptistruct(mesh)
            currMesh.toAbaqus()
    
    def addFile(self):
        files = tkFileDialog.askopenfilenames(initialdir = "/",title = "Select file",filetypes = (("Optistruct Mesh","*.fem"),("All Files","*.*")))
        if files != None:
            for file in files:
                if not file in self.fileList:
                    self.fileList.append(file)
                    self.listbox.insert(END, file)

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()