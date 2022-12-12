import logging
import os.path
import time

""""
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
%(message)s: 打印日志信息 项目使用log 将所有print改为log
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
"""


class GetLog():
    def getlog(self):
        #创建一个logger
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)  #log登记总开关

        #第二步 创建handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        #log_path = os.path.dirname(os.getcwd()) + '/Logs'
        current_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        log_path = current_path+'/log/'
        log_name = log_path+ 'log_info'
        logfile = log_name
        if not logger.handlers:  #避免日志重复打印
            fh = logging.FileHandler(logfile,mode='w',encoding="utf-8-sig")  #日志的写入方式,注意编码格式
            fh.setLevel(logging.DEBUG)  #输出到file的log等级开关

            #控制台获取日志
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            #第三步 定义handler的输出格式
            formatter = logging.Formatter("%(asctime)s - %(filename)s - %(funcName)s[line:%(lineno)d] - %(levelname)s: %(message)s")
            fh.setFormatter(formatter)

            #第四步 ，将logger添加到handler里面

            logger.addHandler(fh)


            #控制台输出日志
            ch.setFormatter(formatter)
            logger.addHandler(ch)
        return logger

if __name__ == '__main__':
    logger = GetLog().getlog()
    #日志
    logger.debug('this is a logger debug message 抵扣')
    logger.info('this is a logger info message 热热离开我')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')
    logger.info("来看看".format(input("请输入")))