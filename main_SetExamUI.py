from tkinter import *
from setExamUI import window


root = Tk()
root.configure(background="green")
root.wm_title("Js Industries")

#width, height, x, y
root.geometry('1200x650+100+50')	

#resize
root.resizable(True,True)


#transparency z
root.attributes('-alpha',1)
root.attributes('-topmost',0)

#Full Screen
root.state("zoomed")



#### Run

if __name__ == "__main__":
	page = window.page
	page = 1
	if (page == 1):
		window.ui(root)	
	elif page == 2:
		window.ui2(root)
		print("Page2 should be running now")
	




root.mainloop()