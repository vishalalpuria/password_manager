from tkinter import * 
import forget_pass_1
import main_page,sql_file


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
def submit(root,npass,npass_conf):
    if len(npass.get()) < 8:
        Label(root,text="Please Enter Password Greater than 8 characters ",font=("",13),width=45, fg='red',bg='#262626').place(x=210,y=235)
    elif npass.get() != npass_conf.get():
        Label(root,text="Password Did not match Enter Correct Password",font=("",13),width=45, fg='red',bg='#262626').place(x=210,y=235)
    else:
        if sql_file.change_password(forget_pass_1.e_mail_final, npass.get()) == True:
            l4 = Label(root,text="PASSWORD CHANGED SUCCESSFULLY",font=("",13),width=55, fg='green',bg='#262626')
            l4.place(x=230,y=235)
            l4.after(1000,lambda:clear_this_page(root, main_page))
            
            


def display(root):

    newpass = StringVar()
    newpass_c = StringVar()
    # Back Button
    img1 = PhotoImage(file='back.png')
    Button(root,image=img1,
    fg='#262626',
    bg='#262626',
    border=0,
    activebackground='#262626',
    command=lambda : clear_this_page(root, forget_pass_1)
    
    ).place(x=25,y=25)



    Label(root,text=f"Your Username is : {forget_pass_1.usr_name}",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white'
    ).place(x=120+132,y=55)

    Label(root,text="Create New Password : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white',
    ).place(x=120+83,y=120)

    textarea_new_pass = Entry(root,
        textvariable=newpass,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white',
        show="●"
    )
    textarea_new_pass.place(x=120+350,y=125)

    Label(root,text="Confirm Password : ",
        font=("Comic Sans Ms",18),
        bg='#262626',
        fg = 'white',
        
    ).place(x=120+125,y=190)

    textarea_new_pass_c = Entry(root,
        textvariable=newpass_c,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white',
        show="●"
    )

    textarea_new_pass_c.place(x=120+350, y=200)
    bttn(root,620,400,'C O N T I N U E','#417aba','#57a2f8',lambda:submit(root,newpass,newpass_c))


    root.mainloop()