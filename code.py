##check if subsequence


def isSub(string, char):
    n = len(string)
    m = len(char)
    j = 0
    i = 0
    if m > n:
        return False
    for i in range(n):
        if i < n and j < m:
            if string[i] == char[j]:
                j += 1
    return (j == m)
        
    
print(isSub('ABC','CB'))