# coding:utf-8
import logging
import time


class MyLog(object):
    '''
封装后的logging
    '''

    def __init__(self, logger=None):
        '''
            指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        '''

        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        # self.log_time = time.strftime("%Y_%m_%d_")
        # self.log_path = "D:\\PyLib\\CodemaoApiTest\\logs\\"
        # self.log_name = self.log_path + self.log_time + 'test.log'

        # fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 这个是python3的
        # fh.setLevel(logging.INFO)

        # 每次被调用后，清空已经存在handler
        self.logger.handlers.clear()

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        # fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        # self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        #  添加下面一句，在记录日志之后移除句柄，否则会重复记录（此方法兼容性较差）
        # self.logger.removeHandler(ch)
        # self.logger.removeHandler(fh)
        # 关闭打开的文件
        # fh.close()
        ch.close()

    def getlog(self):
        return self.logger

'''
封装后的logging代码中format()中的自定义日志格式，可以根据喜好更换：

 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息

封装python自带的logging类，向Logger类中传用例名称，用法
log = Logger().getlog()  #放在class上面
class ClassName()
log.info("log message")
结果：
[2018-01-17 22:45:05,447] test_mainrun.py test_run_mail line:31 [INFO]截图保存成功,全路径
'''