from app import login, create, delete
from tkinter import * 
 
window = Tk()

window.title("Kustomer RPA")

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
 
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
 
window.geometry("350x200+{}+{}".format(positionRight, positionDown))

login_btn = Button(window, text="Login", command=login)
create_btn = Button(window, text="Create", command=create)
delete_btn = Button(window, text="Delete", command=delete)

login_btn.place(x=15, y=57.5, height = 85, width = 100)
create_btn.place(x=125, y=57.5, height = 85, width = 100)
delete_btn.place(x=235, y=57.5, height = 85, width = 100)

window.mainloop()