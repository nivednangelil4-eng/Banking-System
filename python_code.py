def Deposit(amt,bal):
    if amt>0:
        bal=bal+amt
        print(amt,"Deposited Successfully")
    else:
        print("Invalid Deposit Amount")
    return bal

def Withdraw(amt,bal):
    if amt>bal:
        print("Insufficient Balance")
    elif amt<=0:
        print("Invalid Withdrawal Amount")
    else:
       bal=bal-amt
       print(amt,"Withdrawn Successfully")
    return bal

def Check(bal):
    print("Current Balance: ",bal)

#Main
bal=0
print("---------------------------------------------------------------")
print("              Welcome to Simple Banking System                 ")
print("---------------------------------------------------------------")
name=input("Enter your name: ")
while True:
    print("1.Deposit")
    print("2. Withdrawal")
    print("3. Check Balance")
    print("4. Exit")
    ch=int(input("Enter your choice(1-4): "))
    print("---------------------------------------------------------------")

    if ch==1:
        amt=float(input("Enter the Amount to Deposit: "))
        bal=Deposit(amt,bal)
        print("---------------------------------------------------------------")
    elif ch==2:
        amt=float(input("Enter the Amount to Withdraw: "))
        bal=Withdraw(amt,bal)
        print("---------------------------------------------------------------")
    elif ch==3:
        Check(bal)
        print("---------------------------------------------------------------")
    elif ch==4:
        print("Thank You",name,"for using our Banking System")
        print("---------------------------------------------------------------")
        break
    else:
        print("Invalid Choice.Please Try Again")
        print("---------------------------------------------------------------")
