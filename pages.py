import tkinter as tk
import database
from tkinter import *
from tkinter import messagebox
from database import *
from modes import *

db = database()
mode = modes()

class pages():

    global login_name
    global login_id
    global login_LRL
    global login_URL
    global login_AA
    global login_APW
    global login_VA
    global login_VPW 
    global login_VRP
    global login_ARP
    global login_M
    
    def welcome_screen(self):

        def open():

            def reopen():
                window.destroy()
                self.create_acct()
                open()

            def login():
                logins = db.query()
                loginSuccessful = False
        
                for login in logins:
                    if username_entry.get()==login[0] and password_entry.get()==login[1] and username_entry.get() == "admin":

                        self.admin_screen()
                        loginSuccessful = True
                        window.destroy()
                        self.open_profile()
                        open()

                    elif username_entry.get()==login[0] and password_entry.get()==login[1]: #need to pull from database
                        login_name = login_name = login[2] + " " + login[3]
                        login_id = login[13]
                        login_LRL = login[4]
                        login_URL = login[5]
                        login_AA = login[6]
                        login_APW = login[7]
                        login_ARP = login[10]
                        login_VA = login[8]
                        login_VPW = login[9]
                        login_VRP = login[11]
                        login_M = login[12]

                        loginSuccessful = True
                        window.destroy()
                        self.open_profile()
                        open()
                if (not loginSuccessful):
                    messagebox.showinfo(title="Invalid Login",message="Your login credentials are invalid.") #**need a way to link this to create account

            #make the window
            window = tk.Tk()
            window.title("Login")
            window.geometry('500x400')
            window.configure(bg='#4863A0')
                
            #frame for the widgets--makes it responsive when you change window size
            frame = tk.Frame(bg='#4863A0')

            #make widgets
            login_label = tk.Label(frame, text="Login", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
            username_label = tk.Label(frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
            password_label = tk.Label(frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
            username_entry = tk.Entry(frame, font=("Arial", 12))
            password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
            login_button = tk.Button(frame, text="Login", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=login)
            new_acct_button = tk.Button(frame, text="Create New Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=reopen)

            #place widgets
            login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
            username_label.grid(row=1, column=0) 
            password_label.grid(row=2, column=0)
            username_entry.grid(row=1, column=1, pady=10) #spacing will affect everything in the same row
            password_entry.grid(row=2, column=1, pady=20) 
            login_button.grid(row=3, column=0, columnspan=2)
            new_acct_button.grid(row=4, column=0, columnspan=2, pady=10)

            frame.pack() #pack is responsive by default

            window.mainloop() #infinite loop that executes the app (stops when window is closed)

    def open_profile(self):

        page = pages()
        profile = tk.Tk()
        profile.geometry("600x650")
        profile.configure(bg='#4863A0')
        profile.title("Profile Page")
        profile_topframe = tk.Frame(profile, bg='#4863A0')
        profile_middleframe = tk.Frame(profile, bg='#4863A0')
        profile_bottomframe = tk.Frame(profile, bg='#4863A0')

        def reopen():
            profile.destroy()
            db.edit(str(login_id))
            page.open_profile()
        
            
        message = "Welcome," + " " + login_name #matches username entered to name stored in database
        LRLmessage = "Lower Rate Limit: " + str(login_LRL)
        URLmessage = "Upper Rate Limit: " + str(login_URL)
        APWmessage = "Atrial Pulse Width: " + str(login_APW)
        AAmessage = "Atrial amplitude: " + str(login_AA)
        ARPmessage = "ARP: " + str(login_ARP)
        VPWmessage = "Ventricular Pulse Width: " + str(login_VPW)
        VAmessage = "Vntricular Amplitude: " + str(login_VA)
        VRPmessage = "VRP: " + str(login_VRP)
        Mmessage = "Pacing Mode: " + str(login_M)

        #create info for corner of screen
        connection_message = tk.Label(profile, text="Connection Status: Pacemaker not connected\nPacemaker version: 1\nDate of implant: 01/01/2023", bg='#4863A0', fg='#FFFFFF', font=("Arial",8))
        welcome_message = tk.Label(profile_topframe, text = message, bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        tracing_message = tk.Label(profile_middleframe, text = "Tracing Methods", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        sign_out = tk.Button(profile_bottomframe, text = "Sign Out", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = profile.destroy)
        aoo = tk.Button(profile_middleframe, text = "AOO", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = mode.open_AOO)
        voo = tk.Button(profile_middleframe, text = "VOO", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = mode.open_VOO)
        aai = tk.Button(profile_middleframe, text = "AAI", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = mode.open_AAI)
        vvi = tk.Button(profile_middleframe, text = "VVI", bg='#FFFFFF', fg='#000000', font=("Arial", 12), command = mode.open_VVI)
    
        profile_edit = tk.Button(profile_bottomframe, text = "Edit Profile", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command = reopen)

        #pacing modes
        pulseratelow_acc_title = tk.Label(profile_middleframe, text= LRLmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        pulseratehigh_acc_title = tk.Label(profile_middleframe, text= URLmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        pulsewidth_arial_title = tk.Label(profile_middleframe, text= APWmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        pulseamp_arial_title = tk.Label(profile_middleframe, text= AAmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        pulsewidth_ventr_title = tk.Label(profile_middleframe, text= VPWmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        pulseamp_ventr_title = tk.Label(profile_middleframe, text= VAmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        VRP_acc_title = tk.Label(profile_middleframe, text= VRPmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        pacingmode_acc_title = tk.Label(profile_middleframe, text= Mmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        ARP_acc_title = tk.Label(profile_middleframe, text= ARPmessage, bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))

            #acc title alignment
        pulseratelow_acc_title.grid(row=2,column=0)
        pulseratehigh_acc_title.grid(row=3,column=0)
        pulsewidth_arial_title.grid(row=4,column=0)
        pulseamp_arial_title.grid(row=5,column=0)
        pulsewidth_ventr_title.grid(row=6,column=0)
        pulseamp_ventr_title.grid(row=7,column=0)
        VRP_acc_title.grid(row=8,column=0)
        pacingmode_acc_title.grid(row=10,column=0)
        ARP_acc_title.grid(row=9,column=0)
        
        connection_message.place(rely=1.0, relx=1.0, x=0, y=0, anchor=tk.SE)
        welcome_message.grid(row=0, column=0, columnspan=6, sticky="news", pady = 20)
        tracing_message.grid(row=1, column=2, pady=10)
        profile_edit.grid(row=0, column = 0)
        sign_out.grid(row=1, column=0, pady=10)
        aoo.grid(row=2, column=2)
        voo.grid(row=3, column=2, pady=10)
        aai.grid(row=4, column=2)
        vvi.grid(row=5, column=2, pady=10)

        #fixing row spacing
        profile_middleframe.grid_rowconfigure(6, minsize=35)
        profile_middleframe.grid_rowconfigure(7, minsize=35)
        profile_middleframe.grid_rowconfigure(8, minsize=35)
        profile_middleframe.grid_rowconfigure(9, minsize=35)
        profile_middleframe.grid_rowconfigure(10, minsize=35)
        profile_middleframe.grid_rowconfigure(11, minsize=35) 
        profile_middleframe.grid_rowconfigure(12, minsize=50)
        profile_middleframe.grid_columnconfigure(1, min = 150)
        profile_topframe.pack()
        profile_middleframe.pack()
        profile_bottomframe.pack()

        #later will check whether pacemaker is connected before displaying error message
        messagebox.showinfo(title="Connection Error",message="Pacemaker is not connected.")

        #check if new pacemaker is different than previous pacemaker
        # if pacemaker != current_pacemaker:
        #     messagebox.showinfo(title="New Pacemaker",message="New pacemaker device has been approached.")

        profile.mainloop()

    def admin_screen(self):
        admin_window = tk.Tk()
        admin_window.title("Admin Settings")
        admin_window.geometry('500x600')
        admin_window.configure(bg='#4863A0')
        
        #get admin id number
        records = db.query()
        for record in records:
            if(record[0] == "admin"):
                admin_id = record[13]
        
        #print records
        def show_users():
            print_records = ''
            records = db.query()
            for record in records:
                if record[0] == "admin":
                    pass
                else:
                    print_records+= str(record[0])+", "+str(record[13])+"\n"

            query_label = Label(admin_frame, text = print_records, bg='#4863A0', fg='#FFFFFF')
            query_label.grid(row=4, column=0, columnspan = 2)

        #frame for the widgets--makes it responsive when you change window size
        admin_frame = tk.Frame(admin_window, bg='#4863A0')

        #make widgets
        delete_user_entry = tk.Entry(admin_frame, font=("Arial", 12))
        delete_user_label = tk.Label(admin_frame, text="Enter ID", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        delete_user_button = tk.Button(admin_frame, text="Delete User", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=lambda: db.delete(delete_user_entry.get()))
        admin_label = tk.Label(admin_frame, text="Admin Settings", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
        show_users_button = tk.Button(admin_frame, text="Show Usernames/IDs", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=show_users)
        password_entry = tk.Entry(admin_frame, font=("Arial",12))
        password_label = tk.Label(admin_frame, text="Admin Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 12))
        change_password_button = tk.Button(admin_frame, text="Change Password", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command= lambda: db.changePassword(admin_id,password_entry.get()))
        signout_button = tk.Button(admin_frame, text="Sign Out", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=admin_window.destroy)

        #place widgets
        admin_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
        delete_user_entry.grid(row=1, column=1, padx=10)
        delete_user_label.grid(row=1, column=0)
        delete_user_button.grid(row=2, column=0, columnspan=2, pady=10)
        show_users_button.grid(row=3, column=0, columnspan=2, pady=10)
        password_entry.grid(row=7, column=1, padx=10)
        password_label.grid(row=7,column=0)
        change_password_button.grid(row=8, column=0, columnspan=2, pady=10)
        signout_button.grid(row=9, column=0, columnspan=2)

        records = db.query()
        for record in records:
            if record[0] == "admin":
                current_password = record[1]
                password_entry.insert(0, current_password)

        admin_frame.pack() #pack is responsive by default

        admin_window.mainloop() #infinite loop that executes the app (stops when window is closed)

    def start(self):

        page = pages()

        def reopen():
            window.destroy()
            page.create_acct()
            page.welcome_screen()

        def login():
            logins = db.query()
            loginSuccessful = False
            global login_name
            global login_id
            global login_LRL
            global login_URL
            global login_AA
            global login_APW
            global login_VA
            global login_VPW 
            global login_VRP
            global login_ARP
            global login_M
    
            for login in logins:
                if username_entry.get()==login[0] and password_entry.get()==login[1] and username_entry.get() == "admin":

                    page.admin_screen()
                    loginSuccessful = True
                    window.destroy()
                    page.open_profile()
                    page.start()

                elif username_entry.get()==login[0] and password_entry.get()==login[1]: #need to pull from database
                    login_name = login_name = login[2] + " " + login[3]
                    login_id = login[13]
                    login_LRL = login[4]
                    login_URL = login[5]
                    login_AA = login[6]
                    login_APW = login[7]
                    login_ARP = login[10]
                    login_VA = login[8]
                    login_VPW = login[9]
                    login_VRP = login[11]
                    login_M = login[12]

                    loginSuccessful = True
                    window.destroy()
                    page.open_profile()
                    page.start()
            if (not loginSuccessful):
                messagebox.showinfo(title="Invalid Login",message="Your login credentials are invalid.") #**need a way to link this to create account

        #make the window
        window = tk.Tk()
        window.title("Login")
        window.geometry('500x400')
        window.configure(bg='#4863A0')
            
        #frame for the widgets--makes it responsive when you change window size
        frame = tk.Frame(bg='#4863A0')

        #make widgets
        login_label = tk.Label(frame, text="Login", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
        username_label = tk.Label(frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        password_label = tk.Label(frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        username_entry = tk.Entry(frame, font=("Arial", 12))
        password_entry = tk.Entry(frame, show="*", font=("Arial", 12))
        login_button = tk.Button(frame, text="Login", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=login)
        new_acct_button = tk.Button(frame, text="Create New Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=reopen)

        #place widgets
        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0) 
        password_label.grid(row=2, column=0)
        username_entry.grid(row=1, column=1, pady=10) #spacing will affect everything in the same row
        password_entry.grid(row=2, column=1, pady=20) 
        login_button.grid(row=3, column=0, columnspan=2)
        new_acct_button.grid(row=4, column=0, columnspan=2, pady=10)

        frame.pack() #pack is responsive by default

        window.mainloop() #infinite loop that executes the app (stops when window is closed)

         #creates a new user and adds their information to database

    def create_acct(self):
        page = pages()

        #handles creating a new user after the "create account" is pressed
        def new_user():
            if not(firstname_entry.get()):
                messagebox.showinfo(title="Account Creation Error",message="Enter a valid first name.")
            elif not(lastname_entry.get()):
                messagebox.showinfo(title="Account Creation Error",message="Enter a valid last name.")
            elif not(new_username_entry.get()):
                messagebox.showinfo(title="Account Creation Error",message="Enter a valid username.")
            elif len(new_username_entry.get()) < 4:
                messagebox.showinfo(title="Account Creation Error",message="Username must be at least 4 characters.")
            elif not(new_password_entry.get()):
                messagebox.showinfo(title="Password Creation Error",message="Enter a valid password.")
            elif new_password_entry.get()!=confirm_password_entry.get():
                messagebox.showinfo(title="Password Creation Error",message="Password entries do not match.")
            elif len(new_password_entry.get()) < 8:
                messagebox.showinfo(title="Password Creation Error",message="Password must be at least 8 characters")
            else:
                #check usernames
                usernameExists = False
                logins = db.query()
                count = 0
                for login in logins:
                    count += 1
                    if (new_username_entry.get() == login[0]):
                        usernameExists = True
                        messagebox.showinfo(title="Username Creation Error",message="Username already exists.")
                if usernameExists:
                    messagebox.showinfo(title="Username Creation Error",message="Username already exists.")
                elif count > 10:
                    messagebox.showinfo(title="Account Creation Error",message="Too many existing users.")
                
                else:
                    db.submit(new_username_entry.get(),new_password_entry.get(),firstname_entry.get(),lastname_entry.get())
                    messagebox.showinfo(title="Account Creation Success",message="Account creation successful.")
                    create_window.destroy()
                    page.start()
            
        #window
        create_window = tk.Tk()
        create_window.title("Create Account")
        create_window.geometry('600x450')
        create_window.configure(bg='#4863A0')

        #frame to hold the widgets
        create_frame = tk.Frame(create_window, bg='#4863A0')

        #create widgets
        create_acct_label = tk.Label(create_frame, text="Create Account", bg='#4863A0', fg='#FFFFFF', font=("Arial", 30))
        firstname_label = tk.Label(create_frame, text="First Name", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        lastname_label = tk.Label(create_frame, text="Last Name", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        new_username_label = tk.Label(create_frame, text="Username", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        new_password_label = tk.Label(create_frame, text="Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        confirm_password_label = tk.Label(create_frame, text="Confirm Password", bg='#4863A0', fg='#FFFFFF', font=("Arial", 16))
        firstname_entry = tk.Entry(create_frame, font=("Arial", 12))
        lastname_entry = tk.Entry(create_frame, font=("Arial", 12))
        new_username_entry = tk.Entry(create_frame, font=("Arial", 12))
        new_password_entry = tk.Entry(create_frame, show="*", font=("Arial", 12))
        confirm_password_entry = tk.Entry(create_frame, show="*", font=("Arial", 12))
        create_acct_button = tk.Button(create_frame, text="Create Account", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=new_user)
        back_button = tk.Button(create_frame, text="Back", bg='#FFFFFF', fg='#000000', font=("Arial", 10), command=create_window.destroy)

        #place widgets
        create_acct_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)
        firstname_label.grid(row=1, column=0)
        lastname_label.grid(row=2, column=0)
        new_username_label.grid(row=3, column=0) 
        new_password_label.grid(row=4, column=0)
        confirm_password_label.grid(row=5, column=0)
        firstname_entry.grid(row=1,column=1, pady=10)
        lastname_entry.grid(row=2, column=1, pady=10)
        new_username_entry.grid(row=3, column=1, pady=10) #spacing will affect everything in the same row
        new_password_entry.grid(row=4, column=1, pady=10) 
        confirm_password_entry.grid(row=5, column=1, pady=10, padx=5)
        create_acct_button.grid(row=6, column=0, columnspan=2, pady=10)
        back_button.grid(row=7,column=0, columnspan=2)

        create_frame.pack() #pack is responsive by default

        create_window.mainloop() #infinite loop that executes the app

