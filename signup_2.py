from tkinter import * 
import signup_1,main_page
import sql_file



def clear_this_page(root,screen):
    for item in root.winfo_children():
        item.destroy()
    screen.display(root)
def confirm_all_detials(Event,a,b,c,d,e,root):

    tmp_ans_a = a.get()
    tmp_ans_b = b.get()
    tmp_ans_c = c.get()
    tmp_ans_d = d.get()
    tmp_ans_e = e.get()
    if tmp_ans_a == "" or tmp_ans_b == "" or tmp_ans_c == "" or tmp_ans_d == "" or tmp_ans_e == "":
        Label(root,text="Fields Cannot be Blank Please Fill all Fields",font=("",11),width=45, fg='red',bg='#262626').place(x=265,y=415)

    else:
        dob = f"{signup_1.tmplst[1]}/{signup_1.tmplst[2]}/{signup_1.tmplst[3]}"
        signup_1.tmplst.pop(1)
        signup_1.tmplst.pop(1)
        signup_1.tmplst.pop(1)
        signup_1.tmplst.insert(1, dob)
        signup_1.tmplst.pop(6)
        t_l = signup_1.tmplst + [tmp_ans_a, tmp_ans_b, tmp_ans_c, tmp_ans_d, tmp_ans_e]
        sql_file.add_user_to_admin(t_l)

        clear_this_page(root,main_page)





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
    A1 = StringVar()
    A2 = StringVar()
    A3 = StringVar()
    A4 = StringVar()
    A5 = StringVar()
    img1 = PhotoImage(file='back.png')
    # Back Button
    Button(root,image=img1,
    fg='#262626',
    bg='#262626',
    border=0,
    activebackground='#262626',
    command=lambda : clear_this_page(root, signup_1)
    ).place(x=25,y=25)


    Label(root,
    text="WELCOME TO PASSWORD MANAGER",
    font=('Comic Sans MS',22),
    bg='#262626',
    fg = 'white'
    ).place(x=195,y=7)
    
    
    Label(root,
    text="Security Questions",
    font=('Comic Sans MS',10),
    bg='#262626',
    fg = 'white'
    ).place(x=390,y=45)
    
    #Question 1
    Label(root,text="Q1.What is the name of your favourite pet ?",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=250+50,y=134-70)
    #Question 2
    Label(root,text="Q2.What is your mother's maiden name ?",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=250+50,y=195-60)
    #Question 3
    Label(root,text="Q3.What high school did you attend ?",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=250+50,y=255-50)
    #Question 4
    Label(root,text="Q4.What was your favourite food as a child ?",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=250+50,y=315-40)
    #Question 5
    Label(root,text="Q5.What is your favourite movie ?",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=250+50,y=375-30)

    
    

    textarea_q1 = Entry(root,
        textvariable=A1,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q2 = Entry(root,
        textvariable=A2,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q3 = Entry(root,
        textvariable=A3,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q4 = Entry(root,
        textvariable=A4,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q5 = Entry(root,
        textvariable=A5,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q1.place(x=275+50,y=165-70)
    textarea_q2.place(x=275+50,y=225-60)
    textarea_q3.place(x=275+50,y=285-50)
    textarea_q4.place(x=275+50,y=345-40)
    textarea_q5.place(x=275+50,y=405-30)

    bttn(root,547,450,'C O N F I R M','#417aba','#57a2f8',lambda:confirm_all_detials(Event,A1,A2,A3,A4,A5,root))


    root.mainloop()