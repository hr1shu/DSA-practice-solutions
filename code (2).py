##Print all Subsequences of a string.

def substr(STR,sub = ''):
    if len(STR) == 0:
        print(sub, end = ' ')
        return 
    
    
    substr(STR[:-1],sub + STR[-1])
    substr(STR[:-1],sub)
    return

def main():
    STR ='abc'
    substr(STR)
    
    
if __name__ == "__main__":
    main()