from tkinter import * 
from tkinter import ttk
import customtkinter
from password_generator import random_pass
import sql_file 
import main_page



def clear_this_page(root,screen):
    for item in root.winfo_children():
        item.destroy()
    screen.display(root)
    
def create_tree(root):
    global my_tree,data,websitelist
    """
    function to make the row and column entries of the username, password, website
    """
    data = sql_file.retrive(main_page.var1)
    websitelist = [i[1] for i in data]
    tree_frame = Frame(root,borderwidth=4,relief=SUNKEN,bg='#262626')
    tree_frame.place(x=173,y=45)
    

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll.pack(side=RIGHT,fill=Y)
   
   
    my_tree=ttk.Treeview(tree_frame,style="mystyle.Treeview",yscrollcommand=tree_scroll.set,selectmode=BROWSE)
    my_tree.pack()
    
    
    my_tree['columns'] = ("Sno.", "Website", "Username","Password")

    my_tree.bind('<Motion>', "break")   
    tree_scroll.config(command=my_tree.yview)
    
    # Formate Our Columns
    my_tree.column("#0", width=0, stretch=0)

    my_tree.column("Sno.", anchor=CENTER, width=140,stretch=0)
    my_tree.column("Website", anchor=CENTER, width=340,stretch=0)
    my_tree.column("Username", anchor=CENTER, width=340,stretch=0)
    my_tree.column("Password", anchor=CENTER, width=340,stretch=0)
    
    # # Create Headings 
    my_tree.heading("#0",text="" ,anchor = CENTER)

    my_tree.heading("Sno.",text="Sno.", anchor=CENTER)
    my_tree.heading("Website",text="Website", anchor=CENTER)
    my_tree.heading("Username",text="Username", anchor=CENTER)
    my_tree.heading("Password", text="Password",anchor=CENTER)

    my_tree.tag_configure('oddrow', background="#262626")
    my_tree.tag_configure('evenrow', background="#101010")

    global count
    count=1

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3]), tags=('evenrow'))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2],record[3]), tags=('oddrow'))
        count += 1

def delete_credential(Event):
    global data
    try:
        x = my_tree.selection()[0]
        selected = my_tree.focus()
        values = my_tree.item(selected,'values')
        
        sql_file.del_query(values[1],main_page.var1) #website is going in 
        my_tree.delete(x)
        data = sql_file.retrive(main_page.var1)
    except:
        pass


def add_credentials(Event,frame,w,u,p):
    data = sql_file.retrive(main_page.var1)
    websitelist = [i[1] for i in data]
    
    tmp_web = w.get()
    tmp_user = u.get()
    tmp_pass = p.get()
    if tmp_web == "":
        for item in frame.winfo_children():
            item.destroy()
        Label(frame,text="Please Enter Website",font=("",13), fg='red',bg='#262626').pack(side=LEFT)
    elif tmp_user == "":
        for item in frame.winfo_children():
            item.destroy()
        Label(frame,text="Please Enter Username",font=("",13), fg='red',bg='#262626').pack(side=LEFT)
    elif tmp_pass == "":
        for item in frame.winfo_children():
            item.destroy()
        Label(frame,text="Please Enter Password",font=("",13), fg='red',bg='#262626').pack(side=LEFT)
    elif len(tmp_user) <=1:
        for item in frame.winfo_children():
            item.destroy()
        Label(frame,text="Username Must be of 2 characters or more",font=("",13), fg='red',bg='#262626').pack(side=LEFT)
    elif len(tmp_pass) <=7:
        for item in frame.winfo_children():
            item.destroy()
        Label(frame,text="Password Must be of 8 characters or more",font=("",13), fg='red',bg='#262626').pack(side=LEFT)
    elif tmp_web in websitelist:
        for item in frame.winfo_children():
            item.destroy()
        Label(frame,text="You have already entered this website",font=("",13), fg='red',bg='#262626').pack(side=LEFT)
    else:
        for item in frame.winfo_children():
            item.destroy()
        sql_file.insert(tmp_web, tmp_user, tmp_pass,main_page.var1)
        global count
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(count,tmp_web,tmp_user,tmp_pass), tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text="", values=(count,tmp_web,tmp_user,tmp_pass), tags=('oddrow',))
        my_tree.yview_moveto('1.0')
        count += 1

    







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


def display(root):
    root.geometry("1537x791-%d+0"%(-7))
    # root.resizable(1,1)
    # root.minsize(1535,800)
    style = ttk.Style()

    style.theme_use("default")

    style.configure("Treeview",
    anchor=CENTER,
    foreground="white",
    rowheight=42,
    fieldbackground="#262626",
    font=('', 12)
    )
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold')) # Modify the font of the headings



    website = StringVar()
    username_1 = StringVar()
    password_1 = StringVar()

    Label(root,
    text=f"WELCOME User : {main_page.var1}",
    font=('Comic Sans MS',20),
    bg='#262626',
    fg = 'white'
    ).pack(anchor=CENTER)

    create_tree(root)


    # FORGET PASSWORD BUTTON
    def func1(e):
        B1['foreground']= '#696262'  
    def func2(e):
        B1['foreground']= 'white'
    B1 = Button(text="LOG OUT",
        font=("comic sans ms", 14),
        bg='#262626',
        fg = 'white',
        border=0,
        activebackground="#262626",
        command= lambda : clear_this_page(root,main_page)
    )
    B1.place(x=1300,y=740)
    B1.bind("<Enter>",func1)
    B1.bind("<Leave>",func2)


    f2 = Frame(root,width=885,
    height=195,borderwidth=4,
    relief=SUNKEN,
    background='#262626'
    
    )
    f2.place(x=330,y=575)

    error_frame = Frame(f2,background="#262626",
    )
    error_frame.place(x=130,y=150)


    Label(f2,
    text="Add New Username/Password",
    font=('Comic Sans MS',15),
    bg='#262626',
    fg = 'white'
    ).place(x=300,y=0)


    Label(f2,
    text="Website :",
    font=('Comic Sans MS',13),
    bg='#262626',
    fg = 'white'
    ).place(x=25,y=40)

    Label(f2,
    text="Username :",
    font=('Comic Sans MS',13),
    bg='#262626',
    fg = 'white'
    ).place(x=25,y=80)

    Label(f2,
    text="Password :",
    font=('Comic Sans MS',13),
    bg='#262626',
    fg = 'white'
    ).place(x=25,y=120)

    textarea_web = Entry(f2,
        textvariable=website,
        font=('Product Sans', 12),
        borderwidth=3,
        width=20,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    ).place(x=132,y=42)

    textarea_user_1 = Entry(f2,
        textvariable=username_1,
        font=('Product Sans', 12),
        borderwidth=3,
        width=20,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    ).place(x=132,y=82)

    textarea_passwd_1 = Entry(f2,
        textvariable=password_1,
        font=('Product Sans', 12),
        borderwidth=3,
        width=20,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    ).place(x=132,y=122)
    

    def getpass(Event):
        password_1.set(random_pass(int(abs(slider_1.get()))))


    Label(f2,text="Password Strength",bg="#262626",fg='white').place(x=595,y=54)

    slider_1 = customtkinter.CTkSlider(master=f2,number_of_steps=int(16),
    from_=8, to=16)
    slider_1.place(x=550,y=40)
    slider_1.set(0)
    

    bttn(f2,540,90,'GENERATE PASSWORD','#417aba','#57a2f8',lambda: getpass(Event))
    bttn(f2,540,134,'A D D','#417aba','#57a2f8',lambda: add_credentials(Event,error_frame,website,username_1,password_1))
    bttn(root,1245,515,'D E L E T E','#417aba','#57a2f8',lambda: delete_credential(Event))






    root.mainloop()

