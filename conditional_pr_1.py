# 1) check if number is even or odd

# num = int(input("enter any number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")    


# 2) login system with correct username and password 

# print("welcome to secured login system\n Please enter your valid information ")
# _username_ = "hemant"
# _password_ = 9090

# _user_input = input("Enter Your Username: ").strip().lower()
# _user_pass_input = int(input("Enter Your 4 digit password: "))

# if _user_input == _username_ and _user_pass_input == _password_:
#     print("welcome")

# elif _user_input != _username_ or _user_pass_input != _password_ or len(str(_user_pass_input)) != 4:
#     print("your username or password is wrong ")

# else:
#     print("something is wrong there")    

# 3) discount checker based on purchase amount 

# rs 2000 - rs 6000 = 2% off
# rs 6000 - rs 1000 = 4% off
# less than rs 1000 = 0% off

purchase_amt = float(input("Enter your purchase amount: "))

if 2000 <= purchase_amt <= 6000:
    discount = purchase_amt * 0.02
    final_price = purchase_amt - discount
    print(f"Discounted amount is {discount}")
    print(f"final amount {final_price}")

elif 6000 <= purchase_amt <= 10000:
    discount = purchase_amt * 0.04
    final_price = purchase_amt - discount
    print(f"Discounted amount is {discount}")
    print(f"final amount {final_price}")

elif 1000 >= purchase_amt:
    print("0% off ")


else:
    print("we dont have anything for you")
