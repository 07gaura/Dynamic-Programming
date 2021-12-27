def main():
    n = 5
    li = [None]*(n+1)
    print(fib(n, li))
    
def fib(n,li):
    if n == 1 or n == 0:
        return n
    if li[n-1]!=None:
        return li[n] 
    fib1 = fib(n-1,li)
    fib2 = fib(n-2, li)
    sums = fib1 + fib2
    li[n] = sums
    return sums
if __name__ == "__main__":
    main()
