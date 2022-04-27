if __name__ == '__main__':
    n=0
    while True:
        n=n+1
        if (n%1==0) and (n%3==0) and (n%7==0) and (n%9==0) and (n%2==1) and (n%4==1) and ((n+1)%5==0) and (n%6==3) and (n%8==1):
            print(n)
            break
