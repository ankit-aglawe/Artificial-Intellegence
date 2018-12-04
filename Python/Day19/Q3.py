def fare():
    import numpy as np

    ar = np.array([[3,3.20],[3.50,3.60]])

    total = np.array([118.40,135.20])

    inv = np.linalg.inv(ar)

    ans = inv.dot(total)

    a1 =np.rint(ans[0])
    a2 =np.rint(ans[1])

    print('Total childrens are :', a1)
    print('Total adults are :', a2)


fare()
