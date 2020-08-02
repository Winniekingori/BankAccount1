from datetime import datetime
class Account:

    def __init__(self,first_name,last_name,phone_number):
        self.first_name=first_name
        self.last_name=last_name
       # self.bank=bank
        self.phone_number=phone_number
        self.withdrawals=[]
        self.deposits=[]
        self.balance=0
        self.loan=0
        self.repay_loan=[]

    def account_name(self):
        name="{account for {} {}".format(self.first_name, self.last_name )
        return name

    def deposit(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")

        if amount <=0:
            print("Sorry you cannnot deposit that amount")

        else:
            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            deposit={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance+=amount
            self.deposits.append(amount)
            print("You have deposited {} to {} at {}".format(amount,self.account_name(),formatted_time))

    def withdraw(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return

        if  amount <=0:
            print("Sorry,You cannot withdraw that amount")

        elif amount >=self.withdrawals:
            print("You do not have enough balance")

        else:
            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            withdraw={
                "time":"time",
                "amount":"amount"
            }
            
            self.balance -= amount
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {} at {}".format(amount,self.account_name(),formatted_time))

    def get_balance(self):
        return "The balance for {} is {} Ksh".format(self.account_name(),self.balance)

    def get_formatted_time(self,time):
        return time.strftime("%A ,%drd /%B /%Y, %H:%M:%P")

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            time=withdraw(['time'])
            amount=withdraw(['amount'])
            formatted_time=time.strftime("%A,%drd  %B %Y, %H:%M:%P")
            withdraw_statement="You have withdrawn {} on {}".format(amount,formatted_time)
            print(withdraw_statement)

    def show_deposit_statement(self):
        for deposit in self.deposits:
            time=deposit(['time'])
            amount=deposit(['amount'])
            formatted_time=time.strftime("%A ,%drd /%B /%Y, %H:%M:%P")
            Deposit_statement="You deposited {} on {}".format(amount,formatted_time)
            print(Deposit_statement)

    def request_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount <=0:
            print("Sorry!You cannot request that loan amount")

        else:
            self.loan = amount
            print("You have been given  a loan of {}".format(amount))

    def repay_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter amount in figures")
            return
        if amount <=0:
            print("You cannot repay that ammount")
        elif self.loan ==0:
            print("You do not have a loan balance")

        elif amount>self.loan:
            print("You loan is{} please enter an amount that is less or equal to".format(self.loan))

        else:
            self.loan-=amount
            time=datetime(now)
            repayement ={
                "time":time,
                "amount":amount
            }
            self.repayement.append(repayement)
            print("You have repaid your loan with  {},Your loan balance is {}".format(amount,self.loan)) 

    def repayement_statement(self):
            for repayement in self.loan_repayment:
                time= repayement["time"]
                amount=repayment["amount"]
                formatted_time=self.get_formatted_time[time]
                statement="You repaid{} on {} ".format(amount,formatted_time)
                print(statement)
class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_number,bank):
         self.bank = bank
         super().__init__(first_name,last_name,phone_number)

class MobileMoneyAccount(Account):
    def __init__(self,first_name,last_name,phone_number,service_provider):
         self.service_provider = service_provider
         self.airtime = []
         super().__init__(first_name,last_name,phone_number)

    def buy_airtime(self,amount):
        try:
            amount+1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You dont have enough balance.Your balance is {}".format(self.balance))
        else:
                self.balance -= amount
                time=datetime(now)
                airtime = {
                    "time" :time,
                    "airtime":airtime
                }
                self.airtime.append(airtime)
        print("You have bought airtime worth {} on {} ".format(amount,self.get_formatted_time(time)))


        def pay_bill(self,amount):
            try:
                amount+1
            except TypeError:
                 print("Please enter the amount in figures")
            return
        if amount < self.balance:
                 print("You dont have enough balance.Your balance is {}".format(self.balance))
        else:
                self.balance -= amount
                time=datetime(now)
                pay_bill = {
                    "time" :time,
                    "airtime":airtime
                }
                self.pay_bill.append(pay_bill)
        print("You have paid a bill of  {} on {} ".format(amount,self.get_formatted_time(time)))

        def send(self,amount):
            try:
                amount + 1
            except TypeError:
                  print("Please enter amount in figures")
            return

        if  amount <=0:
                  print("Sorry,You cannot send that amount")

        elif amount >=self.sents:
                  print("You do not have enough balance")
        else:
            time=datetime.now()
            formatted_time=time.strftime("%b %d %Y, %H:%M:%S")
            send={
                "time":"time",
               "amount":"amount"
            }
            
            self.balance -= amount
            self.sents.append(sents)
            print("You have sent {} from {} at {}".format(amount,self.account_name(),formatted_time))
        def receive_money(self,amount):
            print("You received {} on {},your balance is {}".format(amount,formatted_time(time),self.balance)) 
 
 


