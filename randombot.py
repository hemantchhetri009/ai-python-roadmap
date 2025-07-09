username = ""
password = ""

def create_login():
    global username, password
    print("Please fill valid Data\n")
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    print("Thank You, for creating your account here💗🎉")

def login():
    while True:
        print("Login here to chat with bot\n")
        entered_username = input("enter your username: ").strip()
        entered_password = input("enter your password: ").strip()

        if entered_username == username and entered_password == password:
            print("Login Successfull")
            break
        else:
            print("Login Failed")

def menu():
    print("🤖What would you like to do....")
    print("1. Greet Me")
    print("2. Calculate Sum up to N")
    print("3. Check Even or Odd")
    print("4. Print Triangle Pattern")
    print("5. Exit")

#user greeting 1.
def greet_me():
    name_user = input("Your Name: ").strip()
    print(f"Hi Mr\Mrs. {name_user}, Hope you're doing well.")    

#sum of n number 2.
def sum_num():
    num = int(input("Your number: "))
    total = 0
    for i in range(1, num + 1):
        total += i
        print(f"The sum of {num} is ", total)


#checking whether entered number is even or odd 3.

def num_checker():
    _num_check_input = int(input("Enter any number that you like to verify: "))
    if _num_check_input % 2 != 0:
        print("It is an odd number ")
    else:
        print("It is an even number ")    

# print triangle pattern 4.


def triangle_patt():
    num = int(input("your number: "))
    for i in range(1, num + 1):
        print("*" *i)



# main bot 

def chatbot():
    print("Hello, Chatobot is here to server you\n Please create your account to access")

    create_login()

    print("Please login with same informatiob=n for confirmation")

    login()

    while True:
    # print("Choose numbers between 1-5 ")
        menu()
        user_choose = int(input("Enter number between 1 -5 : "))
        if user_choose ==  1:
            greet_me()
        elif user_choose == 2:
            sum_num()
        elif user_choose == 3:
            num_checker()
        elif user_choose == 4:
            triangle_patt()
        elif user_choose == 5:
            print("Have a great day ahead")            
            break
    else:
        print("Invalid number choose")             

chatbot()

# finally did it 