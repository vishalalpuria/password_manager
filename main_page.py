from tkinter import *
import forget_pass_1,signup_1,sql_file
import dashboard

root = Tk()
root.geometry('900x500+250+150')
root.resizable(0,0)
root.title("PASSWORD MANAGER")
root.configure(bg='#262626')
# root.iconbitmap('favicon.ico')

var1 = ''
# username here in the var1


def login_func(Event,uname,password,root):
    global var1
    flag = False
    var1 = uname.get() #this is to pass into the main screen

    tmp_uname = uname.get()
    tmp_pass = password.get()
    u_p_list = sql_file.retrive_user_pass_only() #retriving admins username and password
    for item in u_p_list:
        if  tmp_uname == item[0] and tmp_pass == item[1]:
            flag = True

    if flag == True:
        clear_this_page(root, dashboard)
    else:
        Label(text="Invalid Credentials ",font=("",12),fg = 'red',bg = '#262626').place(x=370,y=250)


def clear_this_page(root,screen):
    for item in root.winfo_children():
        item.destroy()
    screen.display(root)

def bttn(root,x,y,text,bcolor,fcolor,cmd):
    """
    Function to create button on the screen with the given coordinates and more arguments 
    """
    def on_entera(e):
        myButton1['background'] = bcolor
        myButton1['foreground']= '#262626'  
    def on_leavea(e):
        myButton1['background'] = fcolor
        myButton1['foreground']= '#262626'
    

    myButton1 = Button(root,text=text,
        width=30,
        height=2,
        fg='#262626',
        border=0,                    
        bg=fcolor,
        activeforeground='#262626',
        activebackground=bcolor,            
        command=cmd)
                    
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)

def display(root=root):
    user_name = StringVar()
    passwd = StringVar()
    
    root.state("normal")
    root.minsize(900,500)
    root.geometry('900x500+250+150')
    # root.resizable(0,0)


    Label(root,
    text="WELCOME TO PASSWORD MANAGER",
    font=('Comic Sans MS',22),
    bg='#262626',
    fg = 'white'
    ).place(x=195,y=7)

    # sign up and login buttons 
    bttn(root,200,320,'S I G N U P ','#417aba','#57a2f8',lambda : clear_this_page(root,signup_1))

    bttn(root,490,320,'L O G I N','#417aba','#57a2f8',lambda: login_func(Event,user_name,passwd,root))

    # for USERNAME 
    Label(root,text="Username : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=315-5-35,y=125)

    textarea_user = Entry(root,textvariable=user_name,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_user.place(x=465-35,y=135)

    # for password 
    Label(root,text="Password : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white',
    ).place(x=315-35,y=203)

    textarea_pass = Entry(root,textvariable=passwd,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white',
        show="●"
    )
    textarea_pass.place(x=465-35,y=210)


    # FORGET PASSWORD BUTTON
    def func1(e):
        B1['foreground']= '#696262'  
    def func2(e):
        B1['foreground']= 'white'
    B1 = Button(text="Forget Password ? ",
        font=("comic sans ms", 14),
        bg='#262626',
        fg = 'white',
        border=0,
        activebackground="#262626",
        command= lambda : clear_this_page(root,forget_pass_1)
    
    )
    B1.place(x=665,y=410)
    B1.bind("<Enter>",func1)
    B1.bind("<Leave>",func2)
    root.mainloop()


