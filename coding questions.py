#question 1

def hello_name(user_name):
  
    print("Hello,", user_name + "!")

#hello_name("chris")

#question 2
def first_odds():
   for num in range(0, 100 + 1):
    if num % 2 != 0:
        print(num, end = " ")

#first_odds()

#question 3

def max_num_in_list(a_list):
    a_list.sort()
    print(a_list[-1])

max_num_in_list([1,3,5,6,7,9,8])

#question 4

def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year% 100 == 0) or (a_year % 400 == 0):
        print("yeap year")
    else:
        print("not a leap year")

#is_leap_year(2000)

#question 5

 def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1)

is_consecutive([1,2,3,4,5])
