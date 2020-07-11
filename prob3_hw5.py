# Driver: Julia Sales
# Navigator: Anthony Overton
# HW5 Problem 3

def is_sorted(thisList):
    correct = False
    for position in range(len(thisList)):
        thisList[position] = thisList[position]
    
    for check in range(len(thisList)-1):
        if thisList[check] < thisList[check + 1]:
            correct = True
        elif thisList[check] > thisList[check + 1]:
            correct = False
            break
        elif thisList[check] == thisList[check + 1]:
            correct = True
    print correct

is_sorted([1,2,2])
is_sorted(['b', 'a'])

is_sorted([3,1,2])
is_sorted(['a','b'])
