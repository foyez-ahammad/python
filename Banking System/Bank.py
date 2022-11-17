from random import randint


class BankAccount:

    no_of_cust = 0
    acc_num = randint(1111111, 9999999)

    def __init__(self, name, mobile_no, gender, date_of_birth, account_type, initial_depo, pin):

        self.name = name
        self.gender = gender
        self.dOB = date_of_birth
        self.acc_type = account_type
        self.cust_acc_num = BankAccount.acc_num
        self.mobile_no = mobile_no
        self.acc_balance = initial_depo
        self.pin = pin

        BankAccount.acc_num = BankAccount.acc_num + 1
        BankAccount.no_of_cust = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(
            f'-----> Welcome, Bank Of Foyez Ltd. <------\n \nAccount No: {self.cust_acc_num}\t Balance: ${self.acc_balance}\nName: {self.name} \nMobile No: {self.mobile_no} \nGender: {self.gender} \nBirth Date: {self.dOB} \nAccount Type: {self.acc_type}')
        print('--------------------------------------------------------')

    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance = self.acc_balance + amount
            print(
                f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawl(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            print(
                f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def payment(self, other):
        amount = int(input('Enter the payment amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance = self.acc_balance - amount
            other.acc_balance = other.acc_balance + amount
            print(
                f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')
