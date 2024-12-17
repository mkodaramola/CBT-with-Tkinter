from tkinter import *
from Exam_UI import window

root = Tk()
root.configure(background="green")
root.wm_title("CBT")

#width, height, x, y
root.geometry('1200x650+100+50')

#resize
root.resizable(True,True)

#transparency 
root.attributes('-alpha',1)
root.attributes('-topmost',0)

#Full Screen
root.state("zoomed")


#### Run

app = window(root)
window.ui(root)	
	



root.mainloop()




