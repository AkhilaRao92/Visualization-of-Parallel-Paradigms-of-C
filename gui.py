from Tkinter import *

class GUI(Frame):
	def __init__(self,parent):
		Frame.__init__(self, parent)   
		self.parent = parent
		self.initUI()
		self.var_array = []
		self.i = 0
		self.line_num_array = []
		self.j = 0
		self.read_from_file()
	
	def initUI(self):						#creates all the elements of the GUI
      		self.parent.title("GUI for parallel programs")
      		self.pack(fill=BOTH, expand=1)

		self.textbox1 = Text(self,height=30,width=80,background='white')
		self.textbox1.pack()
		self.textbox1.place(x=60,y=80)

		self.textbox2 = Text(self,height=30,width=40,background='white')
		self.textbox2.pack()
		self.textbox2.place(x=750,y=80)

		self.btn1 = Button(self, text ="Execute",command=self.run)
		self.btn1.pack()
		self.btn1.place(x=300,y=600)

		self.btn2 = Button(self, text ="Step",command=self.step)
		self.btn2.pack()
		self.btn2.place(x=850,y=600)
		
		self.num_can = Canvas(self,width=20,height=550)
		self.num_can.pack()
		self.num_can.place(x=39,y=80)
		
		temp = 0						#to print the line numbers beside the text area
		for i in range(1,21):
			self.num_can.create_text(10,10+temp,text=str(i))
			temp = temp+15

	def read_from_file(self):
		f = open("locals.txt","r")
		g = open("line_num.txt","r")

		for line in f:
			self.var_array.append(line)
		for line in g:
			self.line_num_array.append(line)
		
		f.close()
		g.close()

	def run(self):							#places the arrow at the beginning of the program
		#self.mycan = Canvas(self,width=35,height=600,bg='red')
		self.mycan = Canvas(self,width=35,height=600)
		self.mycan.pack()
		self.mycan.place(x=0,y=0)
	
		self.line = self.mycan.create_line(5,90,35,90,width=3)
		self.line = self.mycan.create_line(20,80,35,90,width=3)
		self.line = self.mycan.create_line(35,90,20,100,width=3)

	def step(self):			#Displays the variables in the second textarea
		self.move_pointer()
		self.textbox2.delete("1.0",END)
		length = len(self.var_array)

		if(self.i < length):
			self.textbox2.insert(INSERT,self.var_array[self.i])
			self.i = self.i+1
			self.textbox2.insert(INSERT,self.var_array[self.i])
			self.i = self.i+1
	
	def move_pointer(self):						#Goes through the program step by step based on the line numbers
		#self.mycan = Canvas(self,width=35,height=600,bg='red')
		self.mycan = Canvas(self,width=35,height=600)
		self.mycan.pack()
		self.mycan.place(x=0,y=0)
		
		length = len(self.line_num_array)
		offset = 0

		if(self.j < length):
			offset = int(self.line_num_array[self.j])
			offset = offset*13.2
			self.j = self.j+1

			self.line = self.mycan.create_line(5,90+offset,35,90+offset,width=3)
			self.line = self.mycan.create_line(20,80+offset,35,90+offset,width=3)
			self.line = self.mycan.create_line(35,90+offset,20,100+offset,width=3)
		else:							#To remove the arrow when program ends
			self.mycan = Canvas(self,width=35,height=600)
			self.mycan.pack()
			self.mycan.place(x=0,y=0)
		
def main():
	root = Tk()
	root.geometry("250x150+300+300")
	root.title('GUI for parallel programming')
	app = GUI(root)
    	root.mainloop() 

if __name__ == '__main__':
	main()  
	

