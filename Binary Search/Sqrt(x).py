def squareroot(x):
    if x < 2:
        return x
    l, r = 2, x//2
    print("l_start " + str(l))
    print("r_start " + str(r))
    while l <= r:
        mid = l + (r-l)//2
        print("mid " + str(mid))

        num = mid*mid
        if num > x:
            r = mid - 1
        elif num < x:
            l = mid + 1
        else:
            print("mid " +str(mid))
        print("l " + str(l))
        print("r " + str(r))

    print("r02 " + str(r))

squareroot(10)
