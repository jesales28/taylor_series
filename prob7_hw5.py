# Driver: Julia Sales
# Navigator: Anthony Overton
# HW5 Problem 7

def triangle_check(pair1, pair2, pair3):
    # define variables/coordinates
    x1 = pair1[0]
    y1 = pair1[1]
    x2 = pair2[0]
    y2 = pair2[1]
    x3 = pair3[0]
    y3 = pair3[1]

    # first check x2 - x1 = 0
    temp1 = x2 - x1
    if temp1 == 0:
        temp2 = x3 - x1
        if temp2 == 0:
            print False
        else:
            print True
    else:        
        # find slope of pair1 and pair2
        m1 = (y2 - y1)/(x2 - x1)

        # find the slope of pair1 and pair3
        m2 = (y3 - y1)/(x3 - x1)

        # compare slopes
        if m1 == m2:
            print False
        elif m1 == 0 or m2 == 0:
            print False
        else:
            print True

triangle_check([1,1], [1,3], [3,4])
triangle_check([1,1],[2,2],[3,3])

