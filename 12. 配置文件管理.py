# 导入模块
import configparser

# 配置文件路径
path = 'mysqld.cnf'
# 创建configParser模块
config = configparser.ConfigParser()
# 读取文件
config.read(path, encoding='utf-8')
# 获取所有的section
sections = config.sections()
print(sections)

# 获取section为mysqd_safe下所有的key
keys = config.options('mysqld_safe')
print(keys)

# 获取section为mysqld_safe下所有的key-vale
items = config.items("mysqld_safe")
print(items)

# 获取section为mysqld,key为log_error对应的value
val = config.get('mysqld', 'log_error')
print(val)

# 修改
# 新配置文件
newpath = 'mysqld1.cnf'
# 是否存在section:mysqld
if not config.has_section('mysqld'):
    config.add_section('mysqld')
# 设置logerror路径
config.set('mysqld', 'log_error', '/home/workdir/log/mysql_error.log')
# 添加section:Mysqldump
if not config.has_section('mysqldump'):
    config.add_section('mysqldump')
config.set('mysqld', 'max_allowed_packet', '16M')
# 打开要写入新的配置文件路径
with open(newpath, 'w') as f:
    # 写入文件
    config.write(f, space_around_delimiters=True)
