import logging

# 创建一个logger对象
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录一条日志
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# 处理异常并记录
try:
    # 故意引发一个异常
    1 / 0
except ZeroDivisionError as e:
    logger.exception('An exception occurred: %s', str(e))

