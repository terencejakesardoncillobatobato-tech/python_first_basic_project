# this is a simple program that will ask the user for their preferred schedule
schedule = input(" What kind of sched do you like?: ")

section = input("Inter the preffered value for the schedule: ")

# this section will ask the user for preffered days and weeks
num_of_weeks= int(input(f"number of weeks: "))
num_of_days = int(input(f"number of days: "))


# this section will ask the user for preffered Day of the week
day = input(""" choose 
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday: """)


results = section, num_of_weeks,  num_of_days, day 


print(results)

# this section will check if the user input is valid or not and will print the result of the user input.

if results == "day":
    print("you have chosen day")
elif results == "num_of_weeks":
    print("you have chosen num_of_weeks")
elif results == "num_of_days":
    print("you have chosen num_of_days")
elif results == "section":
    print("you have chosen section")





