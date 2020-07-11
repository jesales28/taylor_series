# -*- coding: utf-8 -*-
""""
taylor.py
Driver:  Anthony Overton
Navigator: Julia Sales
AM129 HW5 - Problem 8

Calculating a Taylor series approximation.

!/usr/bin/env python

exp_appx(x,n)
Routine returns an approximation to exp(𝑥) based on the Taylor series summed
only up to the n-th degree term.

path:

sin_appx(x,n):
Routine approximates the sine function
at a point x by evaluating the Taylor series approximation of degree n. 

cos_appx(x,n):
Routine approximates the cosine function 
at a point x by evaluating the Taylor series approximation of degree n.

"""
global result, sinResult
def exp_appx(x,n):
    result = 0.0
    for i in range(0,n+1):
        result = float(result) + ((float(x)**i)/get_factorial(i))
    print result

def sin_appx(x,n):
    if n < 0:
        print "*** Invalid input: n must be non-negative integer"
        print "nan"
    else:
        sinResult = 0.0
        if n==1 or n==2:
            num1 = ((-1)**0)
            num2 = (float(x))**((2*0)+1)
            numerator = num1*num2
            denominator = get_factorial(2*0+1)
            sinResult = sinResult + (numerator/denominator)
            print sinResult
        elif n==3:
            for i in range(0,n-1):
                num1 = ((-1)**i)
                num2 = (float(x))**((2*i)+1)
                numerator = num1*num2
                denominator = get_factorial(2*i+1)
                sinResult = sinResult + (numerator/denominator)
            print sinResult
                
        else:
            for i in range(0,n-2):
                num1 = ((-1)**i)
                num2 = (float(x))**((2*i)+1)
                numerator = num1*num2
                denominator = get_factorial(2*i+1)
                sinResult = sinResult + (numerator/denominator)
                #print sinResult
            print sinResult

def cos_appx(x,n):
    if n < 0:
        print "*** Invalid input: n must be non-negative integer"
        print "nan"
    else:
        cosResult = 0.0
        if n==1:
            num1 = ((-1)**0)
            num2 = (float(x))**(2*0)
            numerator = num1*num2
            denominator = get_factorial(2*0)
            cosResult = cosResult + (numerator/denominator)
            print cosResult
        elif n==2 or n==3:    #if n is even
            for i in range(0,2):
                num1 = ((-1)**i)
                num2 = (float(x))**(2*i)
                numerator = num1*num2
                denominator = get_factorial(2*i)
                cosResult = cosResult + (numerator/denominator)
                #print cosResult
            print cosResult
        elif n==4 or n==5:
            for i in range(0,3):
                num1 = ((-1)**i)
                num2 = (float(x))**(2*i)
                numerator = num1*num2
                denominator = get_factorial(2*i)
                cosResult = cosResult + (numerator/denominator)
                #print cosResult
            print cosResult
        else:                      # for n is even
            if n%2!=0:
                for i in range(0,n-3):
                    num1 = ((-1)**i)
                    num2 = (float(x))**(2*i)
                    numerator = num1*num2
                    denominator = get_factorial(2*i)
                    cosResult = cosResult + (numerator/denominator)
            else:
                for i in range(0,n-2):
                    num1 = ((-1)**i)
                    num2 = (float(x))**(2*i)
                    numerator = num1*num2
                    denominator = get_factorial(2*i)
                    cosResult = cosResult + (numerator/denominator)
                    #print cosResult
            print cosResult



import os, sys
# syspath = "/Users/julia/Desktop/workspace/AM129"
syspath = "../factorial"
sys.path.append(syspath)

from factorial import get_factorial


    

