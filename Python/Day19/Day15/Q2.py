def IsFloat(num):
    import re
    #num=str(num)
    pat = re.compile('[+-]?([0-9]*[.])?[0-9]+')
    mo = re.search(pat,num).group()
    if mo == num:
        return True
    return False
        

        

print(IsFloat('125.6'))
