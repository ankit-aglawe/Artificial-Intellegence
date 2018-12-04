def array():
    start = input('Enter a start of array: ')
    start = int(start)

    stop = input('Enter a stop of array: ')
    stop = int(stop+1)

    import numpy as np

    k = stop - start

    for i in range(2,11):
        if k%i==0:
            p=k/i
            q=i


    ar = np.arange(start, stop).reshape(p,q)

    print(ar)

    num = input('Enter a number: ')
    num = int(num)

    new1 = np.where(ar%num==0,ar,0)

    new2 = np.where(ar%num!=0,ar,0)


    print(new1)
    print(new2)

    np.savetxt('ar',ar, delimiter=',')
    np.savetxt('new1',new1, delimiter=',')
    np.savetxt('new2',new2, delimiter=',')


array()
