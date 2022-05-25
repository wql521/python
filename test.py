if __name__ == '__main__':
    myDict={'汉堡':15,'鸡翅':10,'薯条':6}
    print(type(myDict))
    print(myDict['鸡翅'])
    myDict['鸡翅']=15.5
    print(myDict)
    myDict['奶茶']=12
    print(myDict)
    print('鸡块' in myDict)
    print('鸡翅' in myDict)
    myDict.pop('薯条')
    print(myDict)
    myDict.get('鸡翅')
    myDict.get('鸡腿','抱歉，无此商品！')
    myDict.clear()
    print(myDict)

