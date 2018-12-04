def shop():
    import numpy as np
    
    price = np.array([30000,35000,40000])

    items = np.array([[1,5,2,3],[5,6,3,1],[7,6,2,1]])

    mon = items[:,0]*price
    tue = items[:,1]*price
    wed = items[:,2]*price
    thu = items[:,3]*price

    print(price)
    print(items)
    print('sales for mon is -- hp-',mon[0], ' sony-',mon[1], ' dell-', mon[2])
    print('sales for Tue is -- hp-',tue[0], ' sony-',tue[1], ' dell-', tue[2])
    print('sales for Wed is -- hp-',wed[0], ' sony-',wed[1], ' dell-', wed[2])
    print('sales for thu is -- hp-',thu[0], ' sony-',thu[1], ' dell-', thu[2])


shop()
