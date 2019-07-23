def sqrt(number):
    """
    This is a binary search method for finding a floor value square root
    """

    
    low = 1
    high = number
    mid =  0
    while low <=high:
        mid = int((low+high)/2)
        if(mid*mid == number):
            return mid
        if(mid*mid > number):
            high = mid -1
        else:
            low = mid + 1
    return high
   
    pass

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (356 == sqrt(127000)) else "Fail")