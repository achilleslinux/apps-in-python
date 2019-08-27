from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=50, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.grid(row=1, columnspan=5)

        self.setup()
        self.__thisTextArea.grid(sticky = N + E + S+W) 
		
		# To open new file 
        self.__thisFileMenu.add_command(label="New", 
										command=self.__newFile)	 
		
		# To open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
										command=self.__openFile) 
		
		# To save current file 
		self.__thisFileMenu.add_command(label="Save", 
										command=self.__saveFile)
		
		#To close the current file
		# self.__thisFileMenu.add_command(label="Close",
		# 								command=self.bell)	 

		# To create a line in the dialog		 
		self.__thisFileMenu.add_separator()										 
		self.__thisFileMenu.add_command(label="Exit", 
										command=self.__quitApplication) 
		self.__thisMenuBar.add_cascade(label="File", 
									menu=self.__thisFileMenu)	 
		
		# To give a feature of cut 
		self.__thisEditMenu.add_command(label="Cut", 
										command=self.__cut)			 
	
		# to give a feature of copy	 
		self.__thisEditMenu.add_command(label="Copy", 
										command=self.__copy)		 
		
		# To give a feature of paste 
		self.__thisEditMenu.add_command(label="Paste", 
										command=self.__paste)		 
		
		# To give a feature of editing 
		self.__thisMenuBar.add_cascade(label="Edit", 
									menu=self.__thisEditMenu)	 
		
		# To create a feature of description of the notepad 
		self.__thisHelpMenu.add_command(label="About Notepad", 
										command=self.__showAbout) 
		self.__thisMenuBar.add_cascade(label="Help", 
									menu=self.__thisHelpMenu) 

		self.__root.config(menu=self.__thisMenuBar) 

		self.__thisScrollBar.pack(side=RIGHT,fill=Y)					 
		
		# Scrollbar will adjust automatically according to the content		 
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)	 
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
		
	def __quitApplication(self): 
		self.__root.destroy() 
		# exit() 

	def __showAbout(self): 
		showinfo("Notepad","This editor can be used as notepad. By Avinash Kumar") 

	def __openFile(self): 
		
		self.__file = askopenfilename(defaultextension=".txt", 
									filetypes=[("All Files","*.*"), 
										("Text Documents","*.txt")]) 

		if self.__file == "": 
			
			# no file to open 
			self.__file = None
		else: 
			
			# Try to open the file 
			# set the window title 
			self.__root.title(os.path.basename(self.__file) + " - Notepad") 
			self.__thisTextArea.delete(1.0,END) 

			file = open(self.__file,"r") 

			self.__thisTextArea.insert(1.0,file.read()) 

			file.close() 

		
	def __newFile(self): 
		self.__root.title("Untitled - Notepad") 
		self.__file = None
		self.__thisTextArea.delete(1.0,END) 

	def __saveFile(self): 

		if self.__file == None: 
			# Save as new file 
			self.__file = asksaveasfilename(initialfile='Untitled.txt', 
											defaultextension=".txt", 
											filetypes=[("All Files","*.*"), 
												("Text Documents","*.txt")]) 

			if self.__file == "": 
				self.__file = None
			else: 
				
				# Try to save the file 
				file = open(self.__file,"w") 
				file.write(self.__thisTextArea.get(1.0,END)) 
				file.close() 
				
				# Change the window title 
				self.__root.title(os.path.basename(self.__file) + " - Notepad") 
				
			
		else: 
			file = open(self.__file,"w") 
			file.write(self.__thisTextArea.get(1.0,END)) 
			file.close() 
			
	def answer():
		showerror("Answer", "Sorry, no answer available")

	def __cut(self): 
		self.__thisTextArea.event_generate("<<Cut>>") 

	def __copy(self): 
		self.__thisTextArea.event_generate("<<Copy>>") 

	def __paste(self): 
		self.__thisTextArea.event_generate("<<Paste>>") 

	def run(self): 

		# Run main application 
		self.__root.mainloop() 

        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()