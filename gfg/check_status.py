"""Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
Return True for the following cases:

    Either a or b (not both) is non-negative and the flag is false.
    Both a and b are negative and the flag is true.

Otherwise, return false."""


def check_status(a, b, flag):
    if (a>0) ^ (b>0) and not flag:
        return True
    elif a<0 and b<0 and flag:
        return True
    else:
        return False
    
result = check_status(1,-1,False)

print(result)