"""
def checkvalid(userId,pwd):
    # 连接数据库，检查userid和pwd，默认返回true
    return True

# insertValue直接插入数据
def insertValue(userId,pwd,**kwargs):
    #插入数据
    pass

# queryValue直接查询数据
def queryValue(userId,pwd,**kwargs):
    #查询数据
    pass

# 定义检查参数函数
# 输入参数为函数，返回值为函数
def checkargs(func):
    def foo(userId,pwd,**kwargs):
        if not checkvalid(userId,pwd):
            return
        func(userId,pwd,**kwargs)
    return foo

# 插入数据，检查参数
insertValue=checkargs(insertValue)
queryValue=checkargs(queryValue)


def checkvalid(userid,pwd):
    # 连接数据库，检查userid，pwd，默认返回True
    return True

# 定义检查参数函数
# 输入参数为函数，返回值为函数
def checkargs(func):
    print('call checkargs')
    def foo(userId,pwd,**kwargs):
        print('call here foo function')
        if not checkvalid(userId,pwd):
            return
        func(userId,pwd,**kwargs)
    return foo

# insertValue直接插入数据
# @checkargs 为装饰器语法糖，功能理解为：
# insertValue=checkargs(insertValue)
@checkargs
def insertValue(userid,pwd,**kwargs):
    # 插入数据
    print('call here inserValue')

# queryValue直接查询数据
# @checkargs 为装饰器语法糖，功能理解为：
# queryValue=checkargs(queryValue)
@checkargs
def queryValue(userid,pwd,**kwargs):
    #查询数据
    print('call here queryValue')

insertValue('test1','123456')



# 装饰器函数
def deco(func):
    # 打印出装饰函数信息
    print('deco func',func)
    # 内嵌函数foo没有任何参数
    def foo():
        # 注意打印顺序
        print('before call testfunc')
        # func作用域：Enclosing
        print('func info',func)
        func()
        print('after call testfunc')
    # 返回值为函数
    return foo

# 装饰器函数testfunc:没有函数
@deco
def testfunc():
    print('call testfuncf()')

testfunc()


# 装饰器函数
def decoLog(level):
    print('call decoLog')
    def deco(func):
        print('call deco')
        def logFunc(msg):
            print('%s:'%level,end="")
            func(msg)
        # 实际返回函数
        return logFunc
    # decoLog返回函数，这个函数是装饰器函数
    return deco

# decoLog('Error')返回deco函数
# deco函数装饰LogError
@decoLog('Error')
def LogError(msg):
    print('%s'%(msg))

@decoLog('Debug')
def LogDebug(msg):
    print('%s'%(msg))

# 调用方式
LogError('this is test')
LogDebug('this is test')

"""

#==============匿名函数==============================================

# 判断数字是否为偶数


def isEven(x): return x % 2 == 0


print(isEven(2))

# 多参数


def myAdd(x, y, z): return x+y+z


print(myAdd(1, 2, 3))

# 带默认参数
# 购买手机使用优惠券后的价格


def phoneprice(price, coupon=0): return price-coupon


print('不适用优惠券：', phoneprice(1499))
print('使用优惠券：', phoneprice(1499, 100))

# 可变长参数非关键字
# 求和
myAdd2 = lambda x, y, *args: x+y+sum(args)
print(myAdd2(1, 2, 3, 3))

# 可变长关键字参数例子
# 计算学生成绩平均分
func = lambda **kwargs: sum(list(kwargs.values()))/len(kwargs)
scores = {'1': 90, "2": 100, "3": 80}
# **scores大散字典，key值必须为字符串
print(func(**scores))
print('****************************************************************************************************************************')

# ===========递归函数========================================================
n = 10
result = 1
while n > 0:
    result *= n
    n -= 1
print(result)


def factorial(n):
    if n == 1:
        return n
    return n*factorial(n-1)


print(factorial(5))


info = [[['鬼谷子', 10], ['孙悟空', 9.9], ['李白', 8],
         ['孙尚香', 9]], [['张飞', 9], ['后羿', 10.8]]]


def dumplist(info):
    # 遍历列表
    for val in info:
        if isinstance(val, list):
            dumplist(val)
        else:
            # 截止条件
            print(val, end=',')


print(dumplist(info))





print("hahaha")