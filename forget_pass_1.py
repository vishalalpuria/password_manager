from tkinter import *
import main_page
import forget_pass_2
import sql_file
import random


mail_list = sql_file.retrive_admin_emails()
usr_name = ""
e_mail_final = ""


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
def check_answers(a1,a2,myans_list,a,b,email,root):
    global usr_name
    if a1.get().lower() == myans_list[0][a].lower() and a2.get().lower() == myans_list[0][b].lower():
        usr_name = sql_file.get_username(email.get())
        global e_mail_final
        e_mail_final = email.get()
        clear_this_page(root, forget_pass_2)
    else:
        Label(root,text="Answers Does Not Match ! try again",font=("",13),width=45, fg='red',bg='#262626').place(x=42,y=400)


def showquestions(qf,email,rand_list,a,b,root):

    ans_1 = StringVar()
    ans_2 = StringVar()
    ans_list = sql_file.retrive_5_ans(email.get())
    q1 = "What is the name of your favourite pet ?"
    q2 = "What is your mother's maiden name ?"
    q3 = "What high school did you attend ?"
    q4 = "What was your favourite food as a child ?"
    q5 = "What is your favourite movie ?"
    ques1 = ""
    ques2 = ""
    if rand_list[0] == 0:
        ques1 = q1
    elif rand_list[0] == 1:
        ques1 = q2
    elif rand_list[0] == 2:
        ques1 = q3
    elif rand_list[0] == 3:
        ques1 = q4
    elif rand_list[0] == 4:
        ques1 = q5

    if rand_list[1] == 0:
        ques2 = q1
    elif rand_list[1] == 1:
        ques2 = q2
    elif rand_list[1] == 2:
        ques2 = q3
    elif rand_list[1] == 3:
        ques2 = q4
    elif rand_list[1] == 4:
        ques2 = q5


    # Question 1
    Label(qf,text=f"Q1.{ques1}",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=6,y=50)
        
    textarea_q1 = Entry(qf,
        textvariable=ans_1,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q1.place(x=30,y=78)

    # Question 2
    Label(qf,text=f"Q2.{ques2}",
        font=('Product Sans',13),
        bg='#262626',
        fg = 'white'
        ).place(x=6,y=109)
        
    textarea_q2 = Entry(qf,
        textvariable=ans_2,
        font=('Product Sans', 12),
        borderwidth=4,
        width=32,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_q2.place(x=30,y=138)
    bttn(qf,600,200,'C O N T I N U E','#417aba','#57a2f8',lambda:check_answers(ans_1, ans_2, ans_list,a,b,email,root))

def dest_questions(qf):
    for item in qf.winfo_children():
        item.destroy()
        

def create_questions(root,email,qf,rand_list,a,b):
    # qf is the question frame
    flag = False
    for item in mail_list:
        if item == email.get():
            flag = True
            break
    if flag==True:
        Label(root,text="Answer the Questions to Proceed",font=("",13),width=45, fg='green',bg='#262626').place(x=130,y=106)
        showquestions(qf,email,rand_list,a,b,root)
    else:
        Label(root,text="Entered Email does not match",font=("",13),width=45, fg='red',bg='#262626').place(x=130,y=106)
        dest_questions(qf)
    

def display(root):
    global mail_list
    mail_list = sql_file.retrive_admin_emails()
    rand_list = random.sample(range(0,5),2)


    email = StringVar()
    img1 = PhotoImage(file='back.png')
    # Back Button
    Button(root,image=img1,
    fg='#262626',
    bg='#262626',
    border=0,
    activebackground='#262626',
    command=lambda:clear_this_page(root, main_page)
    ).place(x=25,y=25)
    
    que_frame = Frame(root,width=880,height=270,bg='#262626')
    que_frame.place(x=10,y=200)
    Label(root,text="Enter Your Email Address : ",
        font=('',15),
        bg='#262626',
        fg = 'white'
        ).place(x=80,y=60)
    
    textarea_email = Entry(root,
        textvariable=email,
        font=('Product Sans', 12),
        borderwidth=4,
        width=23,
        relief=SUNKEN,
        bg='#262626',
        fg = 'white'
    )
    textarea_email.place(x=330,y=60)
    
    bttn(root,620,100,'C O N T I N U E','#417aba','#57a2f8',lambda:create_questions(root,email,que_frame,rand_list,rand_list[0],rand_list[1]))  
      

    root.mainloop()
