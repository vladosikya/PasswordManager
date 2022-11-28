import tkinter
from tkinter import messagebox

class Interface:
    def __init__(self, generate):
        self.generate = generate
        window = tkinter.Tk()
        window.title('Password Manager')
        window.config(width=200, height=200, padx=30, pady=30)
        canv = tkinter.Canvas()
        photo = tkinter.PhotoImage(file="logo.png")
        canv.create_image(160, 100, image=photo)
        canv.grid(row=1, column=1)

        #Labels

        label_website = tkinter.Label(text="Website")
        label_email = tkinter.Label(text="Email/Username")
        label_password = tkinter.Label(text="Password")
        label_website.grid(column=0, row=2)
        label_email.grid(column=0, row=3)
        label_password.grid(column=0, row=4)

        #Entry
        self.entry_website = tkinter.Entry()
        self.entry_email = tkinter.Entry()
        self.entry_password = tkinter.Entry()
        self.entry_website.grid(column=1, row=2, columnspan=2, padx=30)
        self.entry_website.config(width=62)
        self.entry_email.grid(column=1, row=3, columnspan=2, padx=30)
        self.entry_email.config(width=62)
        self.entry_password.grid(column=1, row=4, padx=30, columnspan=1, sticky='w')
        self.entry_password.config(width=42)


        #Buttons
        button_generate = tkinter.Button(text='Generate Password', command=self.generate_)
        button_add = tkinter.Button(text='Add', command=self.add)
        button_generate.place(x=390, y=310)
        button_add.grid(column=1, row=5, columnspan=2, pady=10)
        button_add.config(width=53)

        window.mainloop()

    def generate_(self):
        self.entry_password.delete(1, len(self.entry_password.get())+1)
        self.generate.generate_password()
        self.entry_password.insert(0, self.generate.result)

    def add(self):
        website = self.entry_website.get()
        email = self.entry_email.get()

        if website == "" or email == "" or self.generate.result == "":
            messagebox.showwarning(title='Warning!', message='You have not completed all fields.')
        else:
            self.generate.add(website, email)

            #Clear
            self.entry_website.delete(0, len(self.entry_password.get())+1)
            self.entry_email.delete(0, len(self.entry_password.get())+1)
            self.entry_password.delete(0, len(self.entry_password.get())+1)

            messagebox.showinfo(title="Info", message='Data saved!')
