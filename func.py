# def welcome():
#     print("welcome")
# welcome()    

# ✍️ Create a function square(num) that returns the square of a number.
# num = int(input("Enter number: "))

# def square(num):
#     print(f"sqaure of {num} is ", num*num)

# square(num)    


# 📏 Create a function is_even(n) that returns True if number is even, False otherwise.

# n = int(input("Enter any number: "))
# def is_even(n):
#     if n%2 != 0:
#         print("It is not an even number, false")
#     else:
#         print("It is an even number, True")    
# is_even(n)        



# 🧮 Create a function sum_upto(n) that returns the sum of numbers from 1 to n.? 

# def sum_upto(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
# print(sum_upto(9))

# 📊 Create a function print_triangle(rows) to print:

# def triangle(row):
#     for i in range(1 , row + 1):
#         print("*" *i )
# triangle(6)        

# def triangle(rows):
#     for i in range(1, rows + 1):
#         spaces = rows - i
#         stars = i
#         print(" " * spaces + "*" * stars)

# triangle(6)        

# def sum_num(num):
#     total = 0
#     for i in range(1, num + 1):
#         total += i
#         print(total)
# sum_num(int(input("Enter your number: ")))        


# def triangle_patt(num):
#     for i in range(1, num + 1):
#         print("*" *i)
# triangle_patt(int(input("number: ")))

def sum_num():
    num = int(input("Your number: "))
    total = 0
    for i in range(1, num + 1):
        total += i
        print(f"the sum of {num} is ", total)
sum_num()