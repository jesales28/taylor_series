#prob4_hw5.py
# Driver    Anthony Overton
# Navigator Julia Sales

def sum_list(a):
    for position in range(len(a)):
        if position == 0:
            a[position] = a[position]
        else:
            a[position] = a[position - 1] + a[position]
    print a

sum_list([1,2,3])