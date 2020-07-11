#prob6_hw5.py
# Driver:  Anthony Overton
# Navigator: Julia Sales
# AM129 HW5 - Problem 6
#
# Palindrome routine:
# Returns TRUE if arg is a Palindrome, False if not.
#
#!/usr/bin/env python

def palindrome(word):
    length = len(word)
    print(word)
    reverse_word = [None]*length
    norm_word = [None]*length

    # put reverse order into a list
    for i in range(length-1, -1, -1):
        reverse_word = word[i]

    # put normal order into a list
    for j in range(0, length):
        norm_word = word[j]
    
    # compare list elements
    for k in range(0, length):
        if reverse_word[i] == norm_word[i]:
            answer = True
            print(answer)
        else:
            print('gonna set false!')
            answer = False
            return answer
    return answer        

answer = palindrome('madam')
print('Final Value:')
print(answer)