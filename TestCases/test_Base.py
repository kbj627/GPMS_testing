import logging, os, platform, sys
from logging.handlers import TimedRotatingFileHandler


class BaseTest:
    #TestCase를 Page단위로 구분하여 기록하기 위해 Logger를 TestCase Base 클래스에 위치
    def init_Logger(self, logLevel = logging.DEBUG): #Logger를 초기화한다.
        cur_os = platform.system()
        called = sys._getframe(1).f_code.co_name
        if cur_os == 'Windows':
            self.log_dir = os.getcwd() + '\\logs'
            self.logfile_dir = self.log_dir + '\\pytest_{}.log'.format(called)
        elif cur_os == 'Linux':
            self.log_dir = os.getcwd() + '/logs'
            self.logfile_dir = self.log_dir + '/pytest_{}.log'.format(called)

        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)

        self.logger = logging.getLogger()
        formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')
        self.logger.setLevel(logLevel)

        self.fileHandler = TimedRotatingFileHandler(filename=self.logfile_dir, when='midnight', interval=1, encoding='utf-8')
        self.fileHandler.setFormatter(formatter)
        self.fileHandler.suffix = '%Y%m%d'
        self.logger.addHandler(self.fileHandler)