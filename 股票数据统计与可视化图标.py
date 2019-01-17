"""
# 1. 学生成绩单生成
# 题目要求：一个班级20人，生成一份学号与随机数组成绩单，并写入文件
import random


def genscore(fname, nums):
    # 只写方式打开
    f = open(fname, 'w')
    # 根据个数产生成绩，并写入文件
    for i in range(1, nums + 1):
        # 生成成绩单
        line = '{} {}\n'.format(i, random.randint(30, 100))
        # 将成绩单写入文件
        f.write(line)


# 产生一份数学成绩单
genscore('./math.txt', 20)
# 产生一份语文成绩单
genscore('./chinese.txt', 20)


# 2. 成绩单合并
# 2.1 合并两个成绩到一个文件
def megreScore(fname, source1, source2):
    # 只写方式打开
    f = open(fname, 'w')
    # 打开两个文件
    fchinese = open(source1)
    fmath = open(source2)
    # 将两个文件读取出来，类型为字符串列表
    chinese_lines = fchinese.readlines()
    math_lines = fmath.readlines()
    # 处理列表
    for i in range(len(chinese_lines)):
        # 对每个成绩进行切分
        cline = chinese_lines[i].split()
        mline = math_lines[i].split()
        # 将成绩按学号合并：[1,90,90]
        cline.append(mline[1])
        # 拼接成新的字符串‘1 90 90\n’
        wline = ' '.join(cline) + '\n'
        # 写入文件
        f.write(wline)
    f.close()


megreScore('result.txt', './chinese.txt', './math.txt')

# 2.2 新的需求来了
"""
"""
1. 课程数量不确认，可能三科，可能四科
2. 如果有人缺考，学号对应的成绩不存在
一个班级20个人但某科目可能只有19条成绩
"""
"""


# 合并两个成绩到一个文件
# output:保存结果文件
# nums：班级人数
# subjects：成绩单文件名，长度不固定
def megreMoreScores(output, nums, *subjects):
    # 保存成绩单
    list_subject = []
    fw = open(output, 'w')
    # 待处理每个成绩单
    for fname in subjects:
        f = open(fname)
        # 保留每条成绩
        info = []
        for line in f:
            # 数据格式：[[学号，成绩]]
            info.append(line.split())
        dinfo = dict(info)
        # 每个科目成绩添加到列表：[{},{}]
        list_subject.append(dict(info))
        f.close()
    # 按学号获取成绩
    for i in range(1, nums + 1):
        # 整理一个学生对应成绩
        line = []
        line.append(str(i))  # 添加学号
        # 添加每个科目分数
        for data in list_subject:
            # 如果缺考默认值为0
            line.append(str(' ' + data.get(str(i), 0)) + ' ')
        # 写入数据
        wline = ''.join(line) + '\n'
        fw.write(wline)
    fw.close()


# 为了看到调试结果，这里添加三个文件，一个数学成绩（将一个学号对应成绩去掉），两个语文成绩
megreMoreScores('tresult2.txt', 20, './math.txt', './chinese.txt', './chinese.txt')



"""

# 3. 股票统计分析
"""
A股2018最后一个交易日的部分数据，下载地址：https://pan.baidu.com/s/1vKDE18Cgw8ZaTMJQepDdZQ
3.1 价格区间统计
"""


# 生成价格与价格区间，价格区间与数量字典
def genPriceRange(price_range):
    # 区间：数量字典
    dresult=dict.fromkeys(price_range,0)
