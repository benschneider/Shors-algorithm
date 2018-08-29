import numpy as np

N = 43 * 23  # some number you like to factorise
# bigprime = 2*3*5*7*11*13*17*23*43-1
# nextprime = 2*3*5*7*11*13*17*23*43+33
# largeN = bigprime*nextprime


def gcd(a1, a2):
    ''' Greatest Common divisor '''
    r0 = a1
    while (a2 != 0):
        r0 = a1 % a2
        a1 = a2
        a2 = r0
    return a1


def get_r(x, N, maxr=2000):
    ''' finds r, This part can be implemented in a Q-algorithm to speed things up. '''
    for r in range(1, maxr):
        res = (x**r) % N
        # use higher ode
        # if r**2 > res:
        #     sq = np.sqrt(res)
        #     if sq % 1 == (0):
        #         return r, res
        if res == (1.0):
            if checkr(x, r, N):
                return r, res
            else:
                return 0, 0
    return 0, 0


def checkr(x, r, N):
    if (r % 2 == 0):  # r is even
        if not ((x**(r / 2) + 1) % N == 0):  # is not a multiple of N
            return True
    else:
        return False


def factorise_number(N, x=2, maxr=2000):
    # limit of r to maxr
    r, res = get_r(x, N, maxr)
    div = x**int(r/2)  # avoid python rounding errors
    r0 = gcd((div - 1), N)
    return r, r0, N/r0
