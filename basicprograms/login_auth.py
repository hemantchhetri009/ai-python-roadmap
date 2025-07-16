# creating login where user takes input and that input saved as for further login 


print("Login page\n")
# creating id & pass 

user_input = input("enter your username: ").strip()
pass_input = input("enter password: ").strip()
print("\nData Saved\n Please Login again to check authentication\n")

# again input but as a login 


log_user = input("enter your valid username: ").strip()
log_pass = input("enter your password: ").strip()


while log_user != user_input or log_pass != pass_input:
    print("login failed due to incorrect id or pass\n")
    log_user = input("Enter your username again: ")
    log_pass = input("Enter your password again: ")

print("\ncongratulations for succussfull login")    