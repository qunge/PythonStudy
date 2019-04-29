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
最终实现代码如下：
"""


# 生成价格与价格区间，价格区间与数量字典
def genPriceRange(price_range):
    # 区间：数量字典
    dresult = dict.fromkeys(price_range, 0)
    # 价格：区间字典
    price2range = {}
    # 添加价格到区间元素
    for item in price_range:
        # 获取区间起始值与结束值
        start, end = item.split('~')
        # 添加价格到区间
        for p in range(int(start), int(end)):
            price2range[p] = item
    return dresult, price2range


# fname:文件路径
# vrange:价格区间
# col_index:列索引
def countStocks(fname, vrange, col_index):
    # 生成两个字典
    dRange2nums, dPrice2Range = genPriceRange(vrange)
    # 打开文件，编码格式为utf-8
    f = open(fname, encoding='utf-8')
    # 遍历文件
    for line in f:
        # 按','切分
        info = line.split(',')
        # 根据列取价格
        price = info[col_index]
        # 如果股票价格为‘-’，停牌股票不统计
        if price != '-':
            price = float(price)
            prange = dPrice2Range[int(price)]
            # 区间对应值加一
            dRange2nums[prange] += 1
    # 返回统计结果
    return dRange2nums


# 根据统计情况绘制图标
def gensvg(data, title, output):
    import pygal
    # 柱状图
    line_chart = pygal.Bar()
    # 添加Title
    line_chart.title = title
    for key, val in data.items():
        line_chart.add(key, val)
    line_chart.render_to_file(output)


# 定义价格区间，可以随意改变，最小差值为一，注意只能为整数
price_range = ['0~1', '1~2', '2~3', '3~4', '4~6', '6~8', '8~10', '10~15', '15~20', '20~30', '30~50', '50~600']
# 第三列为价格区间
result = countStocks('2018_stocks.txt', price_range, 2)
gensvg(result,'stock price 2018-12-28','stock_price.svg')
print(result)

# 涨幅统计
# 定义涨幅区间，可以随意改变，最小差值为1
# 注意只能为整数，新股涨停幅度可能到40%多
t_range = ['-10~-8', '-8~-6', '-6~-3', '-3~0', '0~3', '3~6', '6~9', '9~50']
# 文件第四列为价格区间
result = countStocks('2018_stocks.txt', t_range, 4)

print(result)

# pygal模块，官方柱状图示例
import pygal

# 柱状图
line_chart = pygal.Bar()
# 添加Title
line_chart.title = "Browser usage in February 2013(in %)"
# 添加数据
line_chart.add('IE', 19.5)
line_chart.add('Firefox', 36.6)
line_chart.add('Chrome', 36.3)
line_chart.add('Safari', 4.5)
line_chart.add('Opera', 2.3)
# line_chart.render()
# 保存成svg文件
line_chart.render_to_file('browser.svg')
