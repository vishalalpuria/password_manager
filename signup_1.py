from tkinter import *
import main_page,signup_2,sql_file

tmplst = []
def checkNumber(num):
    import re
    Pattern = re.compile(r'^[0-9]{10}$|^[0-9]{12}$')
    if Pattern.search(num):
        return True
    else:
        return False

def check_username(uname):
    import re
    regex = re.compile('[_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(uname) == None):
        return True
    else:
        return False
     
def checkemail(email):
    import re   
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'   
    if(re.search(regex,email)):   
        return True   
    else:   
        return False 

def add_credentials_1(Event,a,b,c,d,e,f,g,h,i,root):
    global tmplst

    email_list = sql_file.retrive_admin_emails()
    usernames_list = sql_file.retrive_admin_usernames()
    t_name = a.get()
    t_dob_date = b.get()
    t_dob_month = c.get()
    t_dob_year = d.get()
    t_phn_no = e.get()
    t_email = f.get()
    t_username = g.get()
    t_passwd = h.get()
    t_passwd_conf = i.get()

    if t_name == "" or t_dob_date == "" or t_dob_month == "" or t_dob_year == "" or t_phn_no =="" or t_email == "" or t_username=="" or t_passwd == "" or t_passwd_conf =="":
        Label(root,text="Fields Cannot be Blank Please Fill all Fields",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)

    elif t_dob_date.isalpha() or t_dob_month.isalpha() or t_dob_year.isalpha():
        Label(root,text="Please Enter only Numbers in DOB ",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif int(t_dob_date) < 1 or int(t_dob_date) > 31 or int(t_dob_month) < 1 or int(t_dob_month) > 12 or int(t_dob_year) < 1900:
        Label(root,text="Please Enter Correct DOB ",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif checkNumber(t_phn_no)==False:
        Label(root,text="Please Enter Correct Mobile number ",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif checkemail(t_email) == False:
        Label(root,text="Please Enter Correct Email ID ",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif len(t_username) < 4:
        Label(root,text="Please Enter Username Greater than 4 characters ",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif len(t_passwd) < 8:
        Label(root,text="Please Enter Password Greater than 8 characters ",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif t_passwd != t_passwd_conf:
        Label(root,text="Password Did not match Enter Correct Password",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif t_username[0].isnumeric():
        Label(root,text="Username can't start with a number",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif check_username(t_username) == False:
        Label(root,text="Username can't contain any special characters",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif t_email in email_list:
        Label(root,text="Email already been registered",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
    elif t_username in usernames_list:
        Label(root,text="Username already been registered",font=("",13),width=45, fg='red',bg='#262626').place(x=200,y=420)
        
    else:
        tmplst = [t_name,
                t_dob_date,
                t_dob_month,
                t_dob_year,
                t_phn_no,
                t_email,
                t_username,
                t_passwd,
                t_passwd_conf]
        
        clear_this_page(root, signup_2)








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



 

def reset_func(Event,a,b,c,d,e,f,g,h,i):
    a.set("")
    b.set("")
    c.set("")
    d.set("")
    e.set("")
    f.set("")
    g.set("")
    h.set("")
    i.set("")


def display(root):
    name = StringVar()

    dob_date = StringVar()
    dob_month = StringVar()
    dob_year = StringVar()

    phn_no = StringVar()
    email = StringVar()
    username = StringVar()
    passwd = StringVar()
    passwd_conf = StringVar()
    # to be used later in the code


    img1 = PhotoImage(file='back.png')
    # Back Button
    Button(root,image=img1,
    fg='#262626',
    bg='#262626',
    border=0,
    activebackground='#262626',
    command=lambda : clear_this_page(root, main_page)
    ).place(x=25,y=25)

    
    Label(root,
    text="WELCOME TO PASSWORD MANAGER",
    font=('Comic Sans MS',22),
    bg='#262626',
    fg = 'white'
    ).place(x=195,y=7)

    Label(root,text="Enter Your Name : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=109-35)

    Label(root,text="Enter Your DOB : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=165-35-10)
    Label(root,text="Enter Your Phone No. : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=215-35)
    Label(root,text="Enter Your Email : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=265-35)
    Label(root,text="Enter Your Username : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=315-35)
    Label(root,text="Enter Your Password : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=365-35)
    Label(root,text="Confirm Password : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=11,y=415-35)
    
    Label(root,text="(Date)",
        bg='#262626',
        fg = 'white'
    ).place(x=280,y=155)
    Label(root,text="(Month)",
        bg='#262626',
        fg = 'white'
    ).place(x=345,y=155)
    Label(root,text="(Year)",
        bg='#262626',
        fg = 'white'
    ).place(x=420,y=155)
    
    Label(root,text="-",
        bg='#262626',
        fg = 'white',
        font=("",20)
    ).place(x=325,y=120)
    Label(root,text="-",
        bg='#262626',
        fg = 'white',
        font=("",20)
    ).place(x=395,y=120)

    bttn(root,184,450,'R E S E T','#417aba','#57a2f8',lambda:reset_func(Event,name,dob_date,dob_month,dob_year,phn_no,email,username,passwd,passwd_conf))
    bttn(root,547,450,'C O N F I R M','#417aba','#57a2f8',lambda:add_credentials_1(Event,name,dob_date,dob_month,dob_year,phn_no,email,username,passwd,passwd_conf,root))
    
    
    # started text areas 
    textarea_name = Entry(root,textvariable=name,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )


    textarea_dob_date = Entry(root,textvariable=dob_date,
        font=('Product Sans', 12),
        borderwidth=4,
        width=3,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_dob_month = Entry(root,textvariable=dob_month,
        font=('Product Sans', 12),
        borderwidth=4,
        width=3,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_dob_yr = Entry(root,textvariable=dob_year,
        font=('Product Sans', 12),
        borderwidth=4,
        width=5,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )



    textarea_phn_no = Entry(root,textvariable=phn_no,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_email = Entry(root,textvariable=email,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_user = Entry(root,textvariable=username,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_pass = Entry(root,textvariable=passwd,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white',
        show="●"
    )
    textarea_pass_con = Entry(root,textvariable=passwd_conf,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white',
        show="●"
    )
    
    textarea_name.place(x=279,y=117-35)

    textarea_dob_date.place(x=279,y=173-35-10)
    textarea_dob_month.place(x=350,y=173-35-10)
    textarea_dob_yr.place(x=420,y=173-35-10)


    textarea_phn_no.place(x=279,y=222-35)
    textarea_email.place(x=279,y=271-35)

    textarea_user.place(x=279,y=320-35)
    textarea_pass.place(x=279,y=369-35)
    textarea_pass_con.place(x=279,y=418-35)

    root.mainloop()
