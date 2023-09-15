import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="12345",database="atm_db")
mycursor=mydb.cursor()
def first():
    print("enter number1------>Activated account")
    print("enter number2------->deposit amount")
    print("enter number3------->withdraw amount")
    print("enter number4------->check balance")
    print("enter numberr5----->change pin number")
    var=int(input("enter your number:"))
    if var==1:
         activate()
    elif var==2:
         deposit()
    elif var==3:
         withdraw()
    elif var==4:
         balance()
    elif var==5:
         change_pin()
    else:
         print("please enter the above mentioned number")
def activate():
 sql="insert into atm_mac(mobile_number,account_number,pin_number) values(%s,%s,%s)" 
 print("********Activation*********")
 mobile_number=int(input("enter your mobile number:"))
 account_number=int(input("enter your account number:"))
 pin_number=int(input("enter your 4digit pin number:"))
 val=(mobile_number,account_number,pin_number)
 mycursor.execute(sql,val)
 mydb.commit()
 print("data saved successfully") 

def deposit():
   pin=int(input("enter the 4 digit pin number:"))
   amount=int(input("enter your deposit amount:"))
   sql1=f"update atm_mac set deposit_amount={amount} where pin_number={pin}" 
   mycursor.execute(sql1)
   mydb.commit()
   print("amount deposit successfully")

def withdraw():
    pin=int(input("enter the 4 digit pin number:"))
    amount=int(input("enter the amount of withdraw:"))
    sql=f"update atm_mac set withdraw_amount={amount}"
    mycursor.execute(sql)
    mydb.commit()
    print("withdraw successfully")
    var=input("do you want recipt yes/no:")
    if var=="yes":
        sql=f"select * from atm_mac  where pin_number={pin} "
        mycursor.execute(sql)
        myresult=mycursor.fetchall()
        print(myresult)
    else:
        print("wlcome")
def balance():
  pin=int(input("enter the 4 digit pin number:"))
  print("your balance:")
  update=f"update atm_mac set balance_amount=deposit_amount-withdraw_amount where pin_number='{pin}'"
  mycursor.execute(update)
  mydb.commit()
  sql=f"select* from atm_mac  where pin_number={pin} "
  mycursor.execute(sql)
  myresult=mycursor.fetchall()
  print(myresult)

def change_pin():
  mobile_number=int(input("enter your mobile number:"))
  account_number=int(input("enter your account number:"))
  pin=int(input("enter your 4digit pin number:"))
  change=int(input("enter the change pin number:"))
  sql=f"update atm_mac set pin_number={change} where pin_number={pin} "
  print("your pin number changed successfully")
  mycursor.execute(sql)
  mydb.commit()
first()
 



     

   

    