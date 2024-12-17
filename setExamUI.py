import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Button,Frame,Label,Style, Combobox, LabelFrame
import tkinter.ttk as ttk
from PIL import ImageTk, Image

# ord('A')
# >> 65

# chr(65)
# >> 'A'

# bin(65)
# >> '0b1000001'




class window(Frame):

	

	noq = 1
	nop = 1
	page = 1

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master

	


	def ui(MainFrame):
		
		scrW = MainFrame.winfo_screenwidth()
		scrH = MainFrame.winfo_screenheight()

		s = Style()
		s.configure('MainFrame.TFrame')

		
		
		midFrame = Frame(MainFrame, width=600, height=400, borderwidth=3,style="MainFrame.TFrame")
		midFrame.pack(padx=20,pady=150)

		label1 = Label(midFrame, text="Number of Questions:")
		label1.grid(column=0,row=0, stick=W)
		no_of_queVal = StringVar()

		def nextPage(e):
			q = no_of_queVal.get()
			p = no_of_optVal.get()

			if not q.isdigit():
				messagebox.showerror("showerror",f"{no_of_queVal.get()} is not a number")
			else:
				midFrame.destroy()
				no_of_optFrame.destroy()
				window.noq = int(no_of_queVal.get())
				window.nop = int (no_of_optVal.get())
				window.page = 2
				window.ui2(MainFrame)

				

		no_of_que = Entry(midFrame,textvariable=no_of_queVal, width=40)
		no_of_que.grid(column=0,row=1, pady=10)
		no_of_que.focus_set()
		no_of_que.bind('<Return>',nextPage)

		

		label2 = Label(midFrame, text="Number of Options:")
		label2.grid(column=0,row=2, stick=W)
		
		# cbVal = StringVar()
		# no_of_opt = Combobox(midFrame,textvariable=cbVal, width=5)
		# no_of_opt['values'] = ('2','3','4','5')
		# no_of_opt.grid(column=0,row=3, stick=W)		
		# no_of_opt.current(3)	


		s = Style()
		s.configure('cbFrame.TFrame',background="green")		
		no_of_optFrame = Frame(midFrame,width=30,height=30,borderwidth=3)
		no_of_optFrame.grid(column=0,row=3, stick=W, pady=(0,10))

		no_of_optVal = StringVar()
		no_of_optVal.set("4")

		for i in range(1,5):
			no_of_opt = Radiobutton(no_of_optFrame,variable = no_of_optVal, value=f"{i+1}", text = f"{i+1}").grid(column=i,row=3, stick=W)

		
				
				



		nxtB = Button(midFrame, text="Next")
		nxtB.grid(column=0,row=4, stick=E, pady=(0,10))
		nxtB.bind('<Button-1>',nextPage)


	def ui2(MainFrame):
		bgc = "green"
		fgc = "#FFF"	
		scrW = MainFrame.winfo_screenwidth()
		scrH = MainFrame.winfo_screenheight()
		MainFrame.configure(background=f"{bgc}")

		s = Style()
		s.configure("tf.TFrame",background=f"{bgc}")
		topFrame = Frame(MainFrame, style="tf.TFrame", width=scrW, height=50)
		topFrame.pack()

		label = Label(topFrame,background=f"{bgc}",foreground=f"{fgc}", text=f"Questions: {window.noq} \n \n  Options: {window.nop}")
		label.place(x=5,y=5)

		submitB = Button(topFrame,text=f"Submit")
		submitB.place(x=scrW-200,y=5)

		scv = Style()
		scv.configure("cv.TFrame",background=f"{bgc}")
		cvFrame = Frame(MainFrame, style="cv.TFrame")
		cvFrame.pack(side=LEFT,fill=BOTH,expand=True)

		
		canvas = Canvas(cvFrame,width=scrW, background=f"{bgc}")	
		canvas.pack(side=LEFT,fill=BOTH,expand=True)

		scroll = Scrollbar(canvas,orient="vertical")
		scroll.pack(side=RIGHT,fill=Y)

		

		canvas.configure(yscrollcommand=scroll.set)
		canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
		scroll.config(command=canvas.yview)

		
		s = Style()
		s.configure('bf.TFrame', background=f"{bgc}")
		bodyFrame = Frame(canvas, width=1300,height=500, style="bf.TFrame")
		bodyFrame.pack(side=LEFT,fill=BOTH,expand=True)

		


		os.chdir('Diagrams/')
		Lfiles = []
		for file in os.listdir():
			Lfiles.append(file)
			print(file)
		Tfiles = tuple(Lfiles)		

		


		# Questions --------
		tp = [None]*window.noq
		dv = [None]*window.noq
		diagEntry = [None]*window.noq
		lf = [None]*window.noq

		mi = 0


			

		for i in range(window.noq):
			s = ttk.Style()
			s.configure('lf.TFrame',bordercolor="white", bd=5, relief=SUNKEN, foreground=f"{fgc}", background=f"{bgc}")
			lf[i] = LabelFrame(bodyFrame, width=scrW, text=f"Question {i+1}", style="lf.TFrame")
			lf[i].pack(expand=True,fill=BOTH, padx=10, pady=10)

			qT = Text(lf[i], width=10, height=3).pack(side=TOP, expand=True, fill=BOTH, pady=5)

			#opts = [chr(65+o) for o in range(window.nop)]

			tp[i] = StringVar()
			dv[i] = StringVar()
			for r in range(window.nop):
					
				op = Radiobutton(lf[i],variable = tp[i], background=f"{bgc}",text=f"{chr(65+r)}", value=f"{chr(65+r)}").pack(side=LEFT, expand=True, fill=BOTH)
				opT = Text(lf[i], width=10, height=0).pack(side=LEFT, expand=True, fill=X,pady=5)


			diaLabel = Label(lf[i],text="Enter name of Diagram: ", foreground=f"{fgc}", font=('Helvitica', 10, 'bold'), background=f"{bgc}").pack(side=LEFT, expand=True, fill=BOTH,pady=5, padx=5)
			diagEntry[i] = Combobox(lf[i], width=10, height=0, textvariable=dv[i], name=f"{i}")
			diagEntry[i]['values'] = Tfiles
			lf[i].id = i
			diagEntry[i].pack(side=LEFT, expand=True, fill=BOTH,pady=5, padx=(5,0))
			def dispImage(e,fm):
				path = f"{e.widget.get()}"
				img = Image.open(path)
				img = img.resize((50,40))
				img = ImageTk.PhotoImage(img)
				disp = Label(lf[0])
				print(fm)
				disp.image = img
				disp.configure(image=img)
				disp.pack(side=LEFT, padx= 20)
			
				

			diagEntry[i].bind('<<ComboboxSelected>>',lambda e:dispImage(e,diagEntry[i].index))
			# path = f"d1.jpg"
			# img = Image.open(path)
			# img = img.resize((50,40))
			# img = ImageTk.PhotoImage(img)
			# disp = Label(lf)
			# disp.image = img
			# disp.configure(image=img)
			# disp.pack(side=LEFT, padx= 20)
			
		
		i = 0
		
		canvas.create_window((0,0),window=bodyFrame, anchor="nw")

		
		print(lf)
		

