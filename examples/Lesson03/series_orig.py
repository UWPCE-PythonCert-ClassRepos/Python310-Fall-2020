"""
series.py from Angela

to be refactored
"""

def fibonacci(n):
    """return nth place of Fibonacci series"""
    fibList = []
    if n == 1:
        fibList = [0]
    elif n == 2:
        fibList = [0,1]
    else:
        fibList = [0,1]
        while len(fibList) < n:
            x = len(fibList)
            i = fibList[x - 2] + fibList[x - 1]
            fibList.append(i)
    print(fibList[n-1])

def lucas(n):
    """return nth place of Lucas series"""
    lucList = []
    if n == 1:
        lucList = [2]
    elif n == 2:
        lucList = [2,1]
    else:
        lucList = [2,1]
        while len(lucList) < n:
            x = len(lucList)
            i = lucList[x - 2] + lucList[x - 1]
            lucList.append(i)
    print(lucList[n-1])


def sum_series(n, n0=0, n1=1):
    """return nth place of fibonacci series as default, returns nth value of Lucas if n0 set to 2 and n1 set to 1"""
    genList = [n0,n1]
    while len(genList) < n:
        x = len(genList)
        i = genList[x - 2] + genList[x - 1]
        genList.append(i)
    print(genList[n-1])