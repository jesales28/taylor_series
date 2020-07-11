#prob2_hw5
# HW5 Problem2 am129
# Driver:    Anthony Overton
# Navigator: Julia Sales
#-----------------------------------------------

def do_twice(f,s):
    f(s)
    f(s)

def print_twice(s):
    print s

do_twice(print_twice,'spam')
