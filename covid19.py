import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="12345",database="vaccination_db")
mycursor=mydb.cursor()
def first():
     who=input("please enter you are admin/user:")
     if who=="user":
        user()
     elif who=="admin":
        admin()
     else:
        print("type only admin/user")

def user():
    print("*******covid19 vaccination*******")
    print("enter the number 1----register")
    print("enter the number 2-----view your vaccination detail")
    print("enter the number3------update your vaccination detail")
    num=int(input(("enter the number:")))
    if num==1:
        insert()
    elif num==2:
         view()
    elif num==3:
        update()
    else:
        print("enter mentioned number only")
def insert():
        print("*******covid19 vaccination register*******")
        sql="insert into vaccination_detail (fullname,age,vaccination_status,vaccination_type,vaccination_place,mail_id,mobile_number) values (%s,%s,%s,%s,%s,%s,%s)"
        fullname=input("enter your fullname:")
        age=int(input("enter your age:"))
        vaccination_status=input("enter your vaccinated status yes/no:")
        vaccination_type=input("which dose do you have covishield/covaxin:")
        vaccination_place=input("enter the place of vaccination:")
        mail_id=input("enter your mailID:")
        mobile_number=input("enter your mobile no:")
        val=(fullname,age,vaccination_status,vaccination_type,vaccination_place,mail_id,mobile_number)
        mycursor.execute(sql,val)
        mydb.commit()
        print("data saved sucssefully")
        print(f"{fullname},{age},{vaccination_status},{vaccination_type},{vaccination_place},{mail_id},{mobile_number}")
        var=input("do ypu want to continuenpress yes:")
        if var=="yes":
           user()
        else:
           print("thanks for visiting")
def view():
        number=int(input("enter your mobile no:"))
        sql=f"select * from vaccination_detail  where mobile_number={number} "
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        print(myresult)
def update():
       name=input("enter your name:")
       monumber=input("enter your exist mobile no:")
       age1=input("enter your age:")
       vaccin=input("enter your vaccinated status yes/no:")
       vaccintype=input("which dose do you have covishield/covaxin:")
       vaccinplace=input("enter the place of vaccination:")
       mailid=input("enter your mailID:")
       num=input("enter your mobile no:")
       sql=f"update vaccination_detail set  fullname='{name}',age={age1},vaccination_status='{vaccin}',vaccination_type='{vaccintype}',vaccination_place='{vaccinplace}',mail_id='{mailid}',mobile_number={num} where mobile_number={monumber}"
       mycursor.execute(sql)
       mydb.commit()
       print("update successfully")
       var=input("do you want continue yes/no:")
       if var=="yes":
           user()
       else:
           first()
def admin():
       mycursor.execute("select * from vaccination_detail")
       myresult=mycursor.fetchall()
       print(myresult)
first()
 
    
           


 




    