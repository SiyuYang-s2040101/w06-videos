# %% md
# A little reminder on Fibonacci sequence: <br />
# Start with $F_0 = 0$, $F_1 = 1$ <br />
# and the then derive the consecutive numbers from <br />
# $F_n = F_{n-1} + F_{n-2} $ <br />
# So, the sequence goes: $0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...$

# %% codecell

# let's create Fibonacci sequence with a function first


def fun_fibo(endnum):
    num = [0]
    if endnum == 0:
        return num
    num.append(1)
    if endnum == 1:
        return num
    for iNo in range(2, endnum+1):
        num.append(num[iNo-1]+num[iNo-2])
    return num


def gen_fibo():
    numN = 0
    yield numN
    numN_1 = numN
    numN = 1
    yield numN
    while True:
        numN_2 = numN_1
        numN_1 = numN
        numN = numN_2 + numN_1
        yield numN


my_fibo = gen_fibo()
print(next(my_fibo))
