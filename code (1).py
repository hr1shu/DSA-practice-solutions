##Palindromic

def isPal(string):
    begin = 0
    end = len(string) - 1
    while begin < end:
        if string[begin] != string[end]:
            return False
        begin += 1
        end -= 1
    return True
    
print(isPal('AABCA'))
