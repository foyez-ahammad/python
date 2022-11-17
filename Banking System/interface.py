from Bank import BankAccount

# use account no. as key and class object(customer account) as value
customer_dict = {}

# use mobile no. as key and store account no. as value, for linking purpose
mobile_acc_link = {}


def line():
    print('--------------------------------------------------------')


print('\nWelcome, Bank Of Foyez Ltd. Digital Banking System')


def new_cust():

    try:
        name = input('Enter Your Name: ').upper()
        mobile_no = int(input('Enter Mobile Number: '))
        gender = input('Enter Your Gender: ').upper()
        dOB = input('Enter Birth Date: ')
        acc_type = input('Enter Account Type: ').upper()
        while True:
            initial_amount = int(input('Enter initial amount: '))
            if initial_amount <= 99:
                print('Sorry, Minimum intial amount need up to 100 BDT')
            else:
                break

        while True:
            pin = int(input('Enter PIN: '))
            re_pin = int(input('Re-Enter PIN: '))
            if pin != re_pin:
                print("Don't Match Pin. Please! Try again.")
            else:
                break

        customer = BankAccount(name=name, mobile_no=mobile_no, initial_depo=initial_amount,
                               pin=pin, gender=gender, date_of_birth=dOB, account_type=acc_type)

        # acct. no. stored as key and object as value
        customer_dict[customer.cust_acc_num] = customer

        # mobile no. linked
        mobile_acc_link[customer.mobile_no] = customer.cust_acc_num

        line()
        print('Succesfully! Your Account Created.')
        print(
            f'Welcome, {customer.name} to "Bank Of Foyez Ltd". Your Account No: {customer.cust_acc_num}')
        line()

    except (ValueError, TypeError):
        line()
        print('Sorry! Incorrect Value. Enter Valid Data. \nTry again! Start From begining.')


def login():

    try:
        account_no = int(input('Enter your Account Number: '))
        account_pin = int(input('Enter your Account PIN: '))
        if account_no in customer_dict.keys() and account_pin == customer_dict[account_no].pin:
            line()
            print(f'{customer_dict[account_no].name}, Succesfully, Logged in.')
            customer_dict[account_no].basic_details()
        else:
            line()
            print('Account either not exist or the pin is wrong')
            line()
            return

        while True:
            user_input1 = input('\nPress 1 for deposit: \nPress 2 for withdrawl: \nPress 3 for money transfer: \nPress 4 to log out: \n-------------------------------------------------------- \nPress: ')

            line()

            try:
                if user_input1 == '1':
                    customer_dict[account_no].deposit()
                elif user_input1 == '2':
                    customer_dict[account_no].withdrawl()
                elif user_input1 == '3':
                    mobile = int(
                        input('Enter the mobile number of recepient: '))
                    if mobile in mobile_acc_link.keys():
                        # use mobile no. to get acct. no.
                        secondary = mobile_acc_link[mobile]
                        customer_dict[account_no].payment(
                            customer_dict[secondary])
                    else:
                        line()
                        print('Does not have an account associated with this number.')
                elif user_input1 == '4':
                    print('Logged Out')
                    line()
                    return
                else:
                    print('Invalid input try again')

            except (ValueError, TypeError):
                line()
                print(
                    'Sorry! Incorrect Value. Enter Valid Data. \nTry again! Start From begining.')

            line()
            customer_dict[account_no].basic_details()

    except (ValueError, TypeError):
        line()
        print('Sorry! Incorrect Value. Enter Valid Data. \nTry again! Start From begining.')


while True:

    user_input1 = input('\nPress 1 for creating a new customer: \nPress 2 for logging in as an existing customer: \nPress 3 for displaying number of customers: \nPress 4 for exit \n-------------------------------------------------------- \nPress: ')

    line()

    if user_input1 == '1':
        print('Process Of New Customer Profile Creation....')
        new_cust()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print('There currently', BankAccount.no_of_cust,
              'customers in Bank Of Foyez Ltd.')
        line()
    elif user_input1 == '4':
        print('Program Exited. Thank You.')
        line()
        break
    else:
        print('Invalid input try again')
        line()
