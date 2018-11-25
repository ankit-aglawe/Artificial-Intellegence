
from mod import*

try:
    if e==0:
        raise IOERROR
    else:
        def mod(k):
            if k == 1:
                import mod

            elif k == 2:
                con = a + 10 * b * c - 5 * d / e
                print con
            elif k == 3:
                reload(mod)
                con = a + 10 * b * c - 5 * d / e
                print con
            elif k == 0:
                next
            else:
                print 'ERROR-INVALID INPUT'
    
except Exception:
    print "e cannot be zero"
