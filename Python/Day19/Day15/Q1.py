def IsInteger(num):
    import re
    #num=str(num)
    pat = re.compile('^([+-]?[0-9]\d*|0)$')
    mo = re.search(pat,num).group()
    if mo == num:
        
        return True
    return False 

print(IsInteger('125'))
