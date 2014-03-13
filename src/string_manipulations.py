'''
Created on Mar 5, 2014

@author: marphill
'''
import math

def hex2decimal(hexa):
    """ A hexadecimal number is defined thusly:
        
        Hexadecimal counting is based on a radix of 16 (meaning 16 possible values
        for each position in the number system). So, for example, a number
        in decimal has a radix of ten, and the number 0-9 can be placed in a 
        given position (ie. 1, 123, 445, 213455, etc. are valid in decimal, but
        not a23, af345, etc).
        
        To account for values in the numeral position above ten in decimal counting, 
        often alphabetic characters are used, normally letter a-f (or A-F). 
        Therefore, hexadecimal numeral position values that are valid are as 
        follows:
        
            0 - 0                9 - 9
            1 - 1                A - 10 ; a - 10
            2 - 2                B - 11 ; b - 11
            3 - 3                C - 12 ; c - 12
            4 - 4                D - 13 ; d - 13
            5 - 5                E - 14 ; e - 14
            6 - 6                F - 15 ; f - 15
            7 - 7
            8 - 8
        
        This function will take a hexadecimal string and convert it into a
        decimal number. Each numeral position can be viewed as 16^0, 16^1, 16^2, etc.
        
        So, for example, ff = 255, 100e7 == 65767, 12 = 18
    """
    
    hexvals = {'a' : 10, 'b' : 11, 'c' : 12, 'd' : 13, 'e' : 14, 'f' : 15}
    i =  0
    number = 0
    while i < len(hexa) :
        if hexa[len(hexa) - i - 1].isdigit():
            number += int(hexa[len(hexa) - i - 1]) * math.pow(16, i)
        else:
            number += hexvals[hexa[len(hexa) - i - 1].lower()] * math.pow(16, i)
        i += 1
    return int(number)

def reverse_string(reverse):
    """ Given a string, reverse the characters in the string to print out
        backwards in a new string. For example, a palindrome will look 
        unchanged with this method, but "look" will become "kool" and "go utes"
        will become "setu og". Spaces need to be preserved as a valid part of
        the string.
    """
    output = ""
    k = len(reverse) - 1
    while k >= 0:
        output += reverse[k]
        k-=1
    return output

def main():
    # hex2decimal testing
    print hex2decimal('100e7') == 65767
    print hex2decimal('13bD') == 5053
    print hex2decimal('FBC') == 4028
    print hex2decimal('12') == 18
    print hex2decimal('f') == 15
    print hex2decimal('1') == 1
    print "------------ Reverse string test ------------"
    #reverse_string
    print reverse_string('hello') == "olleh"
    print reverse_string('_what up doc') == "cod pu tahw_"
    print reverse_string(' what up doc') == "cod pu tahw "

if __name__ == "__main__": main()