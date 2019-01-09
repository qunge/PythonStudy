"""
 1.一个例子搞定打开，读取与关闭
 准备工作：
    1.创建一个本地文件：E:\workdir\readme.txt（或者自己准备一个其他文本文件）；
    2.文件中添加一行内容：this is test
 """

# 文件路径
path = r'E:\workdir\readme.txt'
# 打开文件
f = open(path)
# 读取文件
txt = f.read()
print(txt)
# 关闭文件
f.close()

"""
2 文件打开方式详解
    2.1 open方法详解：
        主要参数：
            file:文件打开路径
            mode:打开方式，默认只读方式
            encoding:打开文件编码格式
                打开方式：
                    r：只读方式，不能输入
                    w：只写方式打开，文件不存在创建文件，文件存在截断文件
                    a：只写方式打开，如果文件存在，在文件尾部可是写入
                    +：读写方式打开
                    b：二进制方式打开，例如图片：'rb','wb','ab'上面操作类似
2.2 打开方式测试
case1：文件不存在创建文件
"""
# 文件不存在
wfpath = r'E:\workdir\testw.txt'
f = open(wfpath, 'w')
# 写入一行
f.write('python')
f.close()
# 执行代码后创建testw.txt,并在文件中写入字符串‘python’

"""
case2：文件存在只写方式打开
准备工作：
    1.在'E:\workdir'下创建文件：test1.txt；
    2.写入一行文本：'abcd1234'；
"""
# 文件存在
fpath = r'E:\workdir\test1.txt'
f = open(fpath, 'w')
f.close()
# 查看test1.txt文件，已被清空

"""
case3：只写方式打开不能读取，否则会报错
"""
# fpath = r'E:\workdir\test1.txt'
# # 文件只写方式打开
# f = open(fpath, 'w')
# f.read()
# f.close()
# f.read()报错，只写方式打开不能读取

"""
case4：只写方式打开并写入，尾部开始写入
"""
# 先写入abc,关闭重新打开文件，再写入123
fpath = r'E:\workdir\testa.txt'
f = open(fpath, 'w')
f.write('abc')
f.close()
# 追加方式打开，文件尾开始写入
fpath = r'E:\workdir\testa.txt'
f = open(fpath, 'a')
f.write('123')
f.close()
# 文件内容abc123

"""
case5：读写方式打开
'r+'：读写方式打开，从文件头开始读,末尾追加写入
'w+'：读写方式打开，文件被清空
'a+'：追加方式读写打开，从文件尾开始读写
"""
# 文件路径，文件内容为：this is test
path=r'E:\workdir\readme.txt'
# 打开文件
f=open(path,'r+')
line=f.read()
print(line)
# 写入文本
f.write('end')
# 关闭文件，文件尾写入end
txt=f.read()
print(txt)
f.close()
# 结果：读取文件内容，并在文件尾插入end;