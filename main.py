import json
import random
import string
from pathlib import Path


class Bank:
    database='data.json'
    data=[]

    try:
      if Path(database).exists():
        with open(database) as fs:
          data = json.loads(fs.read())

      else:
         print("No such file exists")
    except Exception as err:
        print(f"an Exception occured as {err}")      

    @staticmethod
    def __update():
       with open(Bank.database, "w") as fs:
          fs.write(json.dumps(Bank.data))
          
    @classmethod
    def __accountgenerate(cls):
       alpha = random.choices(string.ascii_letters,k=3)      
       num = random.choices(string.digits,k=3)      
       spchar = random.choices("!@#$%^&*",k=1)      
       id=alpha+num+spchar
       random.shuffle(id)
       return "".join(id)




    def Createaccount(self):
          info ={
            "name": input("Enter your name : "),
            "age": int(input("Enter your age : ")),
            "email":input("Enter your Email : "),
            "pin": int(input("Enter your 4 number Pin : ")),
            "accountNo":Bank.__accountgenerate(),
            "balance":0
          }

          if info["age"]<18 or len(str(info["pin"])) != 4:
             print("Sorry your account is not created")
          else:
             print("Account has been created succesfully")
             for i in info:
                print(f"{i}:{info[i]}")
             print("Please note down your account number")

             Bank.data.append(info)

             Bank.__update()


    def depositmoney(self):
       accnumber=input("Please tell your account number ")
       pin=int(input("Please tell your account pin  "))

      #  print(Bank.data)

       userdata=[i for i in Bank.data if i['accountNo'] == accnumber and i["pin"] == pin]

       if not userdata:
        print("❌ Sorry, no data found. Please check your account number and pin.")
        return
       else:
          amount=int(input("How much you want to deposit? "))
          if amount>100000 or amount<0 :
             print("Please enter in range 0 - 100000")

          else:
            #  print(userdata)
             userdata[0]['balance']+=amount
             Bank.__update()
             print("Amount Deposited successfully")
             
    def withdrawmoney(self):
       accnumber=input("Please tell your account number ")
       pin=int(input("Please tell your account pin  "))

      #  print(Bank.data)

       userdata=[i for i in Bank.data if i['accountNo'] == accnumber and i["pin"] == pin]

       if not userdata:
        print("❌ Sorry, no data found. Please check your account number and pin.")
        return
       else:
          amount=int(input("How much you want to withdraw ? "))
          if userdata[0]["balance"] < amount :
             print("Sorry you don't have that much money!")

          else:
            #  print(userdata)
             userdata[0]['balance']-=amount
             Bank.__update()
             print("Amount withdrew successfully")
             
    def showdetails(self):
       accnumber=input("Please tell your account number ")
       pin=int(input("Please tell your account pin  "))
       userdata=[i for i in Bank.data if i['accountNo'] == accnumber and i["pin"] == pin]

       print("\nYour information \n")

       for i in userdata[0]:
          print(f"{i} : {userdata[0][i]}")

       
    def updatedetails(self):
       accnumber=input("Please tell your account number ")
       pin=int(input("Please tell your account pin  "))
       userdata=[i for i in Bank.data if i['accountNo'] == accnumber and i["pin"] == pin]

       if not userdata:
        print("❌ Sorry, no data found. Please check your account number and pin.")
        return
       else:
          print("You cannot change your Age , Account Number ,Balance")
          print("Fill the details for change or leave it empty if no change ")

          newdata={
             "name":input("Enter your name or press enter to skip : "),
             "email":input("Enter your email or press enter to skip : "),
             "pin":input("Enter your pin or press enter to skip : ")
          }
          if newdata["name"]=="":
             newdata["name"]=userdata[0]['name']
          if newdata["email"]=="":
             newdata["email"]=userdata[0]['email']
          if newdata["pin"]=="":
             newdata["pin"]=userdata[0]['pin']

          newdata['age']=userdata[0]['age']
          newdata['accountNo']=userdata[0]['accountNo']
          newdata['balance']=userdata[0]['balance']

          if type(newdata['pin'])==str:
             newdata['pin']=int(newdata['pin'])

          for i in newdata:
             if newdata[i]==userdata[0][i]:
               continue
             else:
                userdata[0][i]=newdata[i]
                Bank.__update()
                print("Details updated Successfully")


    def delete(self):
       accnumber=input("Please tell your account number ")
       pin=int(input("Please tell your account pin  "))
       userdata=[i for i in Bank.data if i['accountNo'] == accnumber and i["pin"] == pin]

       if not userdata:
        print("❌ Sorry, no data found. Please check your account number and pin.")
        return
       else:
          check = input ("Press y if you want to delete an account or press n :")
          if check == 'n' or check == 'N':
             print("bypassed")
          else:
             index= Bank.data.index(userdata[0])
             Bank.data.pop(index)
             print("Account Deleted Successfully ")
             Bank.__update()
       
user = Bank()


print("Press 1 for Creating an account")
print("Press 2 to Deposit money in the account")
print("Press 3 to Withraw money from account")
print("Press 4 for Details")
print("Press 5 for Updating the details")
print("Press 6 for deleting an account")


check = int(input("Enter your choice: "))

if check == 1:
    user.Createaccount()


if check == 2:
   user.depositmoney()

if check == 3:
   user.withdrawmoney()

if check == 4:
   user.showdetails()

if check == 5:
   user.updatedetails()
   
if check == 6:
   user.delete()