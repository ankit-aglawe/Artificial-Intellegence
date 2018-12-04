
def HasVowel(char):
    import re
    
    pat = re.compile('^[aeyiuo]+$')

    mo = re.search(pat, char)

    if mo:
        return True
    return False

 

print(HasVowel('Batman'))
