if __name__ == '__main__':
    RND1 = 30
    RND2 = 45
    for i in range(1, 101):
        if RND1 % i == 0 and RND2 % i == 0:
            x=i
    print(x)
    r = RND2 * RND1
    y = r / x
    print(y)
