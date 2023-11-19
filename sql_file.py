import mysql.connector as sqlcon
import datetime
dt = datetime.datetime.now()
hr = dt.hour
minute = dt.minute
day = dt.day
month = dt.month
year = dt.year
idate = f"{year}-{month}-{day}"
itime = f"{hr}:{minute}:{0}"


mycon = sqlcon.connect(host="bkp5exwpri9rm0a4tjep-mysql.services.clever-cloud.com",user="ucdaknuapb0mpeku",db="bkp5exwpri9rm0a4tjep",passwd="EgldT5ExbpWBUoM11q2o")

try:
    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234')
    cur = mycon.cursor()
    cur.execute("Create Database bkp5exwpri9rm0a4tjep")
    mycon.commit()
    # mycon.close()
    # print("Created new pm database")
except:
    pass
    # print("DB OK")


try:
    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database="pm")
    cur = mycon.cursor()
    cur.execute("create table admins(admin_name varchar(20),date_of_birth varchar(10),mobile_no bigint,email varchar(30) PRIMARY KEY,username varchar(30),password varchar(100),Ans_1 varchar(20),Ans_2 varchar(20),Ans_3 varchar(20),Ans_4 varchar(20),Ans_5 varchar(20),date date,time time)")
    mycon.commit()
    # mycon.close()
    # print("Created new admin table")
except:
    pass
    # print("Admin table ok ")



def add_user_to_admin(final_list):
    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database="pm")
    cur = mycon.cursor()
    cur.execute("insert into admins values('%s','%s',%s,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(final_list[0],final_list[1],final_list[2],final_list[3],final_list[4],final_list[5],final_list[6],final_list[7],final_list[8],final_list[9],final_list[10],idate,itime))
    mycon.commit()
    # mycon.close()


def insert(website,username,password,user_name):
    """
    Function to insert the website username and password into the desired user's table (which user is logged in )
    """


    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
    cur = mycon.cursor()
    cur.execute("insert into %s values ('%s','%s','%s','%s','%s')"%(user_name,website,username,password,idate,itime))

    mycon.commit()

    # mycon.close()

def retrive(user_name):
    """
    Function to retrive the list of website username and password from user's table(which user is logged in )
    this function also made the table if the table is not present becauese the user is registered though
    """
    try:
        list1 = []
        i=1
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("select * from %s"%(user_name))
        data = cur.fetchall()
        for item in data:
            list1.append([i,item[0],item[1],item[2]])
            i+=1
        # mycon.close()
        # print("try working")
        return list1
    except:
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("create table %s (website varchar(30) primary key,username varchar (40),password varchar (40),date date,time time)"%(user_name))
        mycon.commit()
        # mycon.close()
        d = []
        # print("except working")
        
        return d
        

def del_query(x,user_name):
    """
    Function to delete any selected website's username,password 
    """
    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
    cur = mycon.cursor()
    cur.execute("delete from %s where website='%s'"%(user_name,x))
    mycon.commit()

def retrive_admin_emails():
    try:
        list1 = []
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("select email from admins")
        data = cur.fetchall()
        for item in data:
            list1.append(item[0])
        return list1
        # mycon.close()
    except:
        a = []
        return a
def retrive_admin_usernames():
    try:
        list1 = []
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("select username from admins")
        data = cur.fetchall()
        for item in data:
            list1.append(item[0])
        return list1
        # mycon.close()
    except:
        b = []
        return b

def retrive_user_pass_only():
    try:
        list1 = []
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("select username,password from admins")
        data = cur.fetchall()
        for item in data:
            list1.append([item[0],item[1]])
        # mycon.close()
        return list1
    except:
        c = []
        return c

def retrive_5_ans(mail):
    try:
        list1 = []
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("select Ans_1,Ans_2,Ans_3,Ans_4,Ans_5 from admins WHERE EMAIL = '%s'"%(mail))
        data = cur.fetchall()
        for item in data:
            list1.append([item[0],item[1],item[2],item[3],item[4]])
        # mycon.close()
        return list1
    except:
        c = []
        return c
def change_password(email,new_pass):
    try:
        # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
        cur = mycon.cursor()
        cur.execute("update admins set password = '%s' where email = '%s'"%(new_pass,email))
        mycon.commit()
        # mycon.close()
        return True
    except:
        return False
def get_username(email):
    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
    cur = mycon.cursor()
    cur.execute("select username from admins where email = '%s'"%(email))
    data = cur.fetchall()
    return data[0][0]

if __name__ == '__main__':
    pass
    # mycon = sqlcon.connect(host='localhost',user="root",passwd='1234',database='pm')
    # cur = mycon.cursor()
    # # cur.execute("insert into a values('%s',%s)"%("vishal","11234"))
    # cur.execute("select username,password from admins")
    # data = cur.fetchall()  
    # for item in data:
    #     print(item[0],item[1])
    # # mycon.commit()