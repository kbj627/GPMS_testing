import logging, os, platform, sys
from logging.handlers import TimedRotatingFileHandler

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:
    driver = None
    logger = None
    url_gpms_Domain = None

    def init_Webdriver(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        except Exception as e:
            print(e)

    def del_WebDriver(self):
        if not self.driver == None:
            self.driver.quit()
    
    def init_Logger(self, logLevel = logging.DEBUG):
        cur_os = platform.system()
        if cur_os == 'Windows':
            self.log_dir = os.getcwd() + '\\logs'
            self.logfile_dir = self.log_dir + '\\pytest.log'
        elif cur_os == 'Linux':
            self.log_dir = os.getcwd() + '/logs'
            self.logfile_dir = self.log_dir + '/pytest.log'

        if not os.path.exists(self.log_dir):
            os.mkdir(self.log_dir)

        self.logger = logging.getLogger()
        formatter = logging.Formatter(u'%(asctime)s [%(levelname)8s] %(message)s')
        self.logger.setLevel(logLevel)

        self.fileHandler = TimedRotatingFileHandler(filename=self.logfile_dir, when='midnight', interval=1, encoding='utf-8')
        self.fileHandler.setFormatter(formatter)
        self.fileHandler.suffix = '%Y%m%d'
        self.logger.addHandler(self.fileHandler)

    def set_gpms_Domain(self, url_gpms_Domain = 'https://test-gpms.gooroom.kr/'):
        self.url_gpms_Domain = url_gpms_Domain

    def get_WebDriver(self):
        if not self.driver == None:
            return self.driver

    def url_compare(self, path:str):
        if not path[0] == '/':
            path += '/'
        url = self.url_gpms_Domain + path
        result = self.driver.current_url == url
        currentFunc = sys._getframe(0).f_code.co_name
        calledFunc = sys._getframe(1).f_code.co_name

        self.logger.info('[{}] Function called [{}]'.format(calledFunc, currentFunc))
        self.logger.info('[{}] Result : {}'.format(currentFunc, result))

        return result