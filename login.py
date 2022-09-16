from tkinter import *

class login_system:
    def __init__(self, root):
        self.root = root
        self.root.title("login system")
        self.root.geometry("1350*700+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon = PhotoImage(file="images/man-user.png")
        self.pass_icon = PhotoImage(file="images/password.png")
        self.logo_icon = PhotoImage(file="images/logo.png")

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = label(self.root, text="Login system", font=("times new roman", 40, "bold"), bg="yellow", fg="red",
                      bd=10, relief=GROOVE)

        title.place(x=0, y=0, relwidth=1)


root = Tk()
obj = login_system(root)
root.mainloop()

