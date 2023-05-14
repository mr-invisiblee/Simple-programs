"""Module used for importing time functionds"""
import time

maximum = 101

minimum = -4


"""Main module which performm lift operation"""


def lift(x, y):

    if x < maximum and y < maximum and x > minimum and y > minimum:
        global z
        z = x

        if z > y:

            print(z)

            while z != y:

                z -= 1

                time.sleep(1)

                print(z)

        elif z < y:

            while z != y:

                z += 1

                time.sleep(1)

                print(z)

        else:

            print("you are on same floor")

    else:
        z = x
        print("please check building range the maximum is ",
              maximum, "and minimum is ", minimum)

        liftloop()


"""Module which perform looping of lift operation"""
def liftloop():

    c = input("Would you want to go to another floor ? \n")

    print("You are on floor ", z)

    if c == 'yes' or c == 'Yes' or c == 'YES' or c == 'y':

        a = int(input("Enter your destination floor :"))

        lift(z, a)

        liftloop()

    else:

        print("Thanks for using our lift service")


print("Welcome to lift service, This apartments limit is between -3 and 100")
x = int(input("Enter your current floor : "))

if x < maximum and x > minimum:
    if x != 0:
        print("please wait the lift is on floor 0")
        time.sleep(x/10)

        y = int(input("Enter your destination floor : "))

        lift(x, y)

        liftloop()
else:
    print("Please check Limit of this apartment")
