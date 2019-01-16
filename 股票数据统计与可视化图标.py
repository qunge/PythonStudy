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
