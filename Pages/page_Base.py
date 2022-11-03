import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class PageBase:
    def __init__(self, logger):
        self.logger = logger
        self.init_Webdriver()

    def __del__(self):
        self.del_WebDriver()

    def init_Webdriver(self, pageLoadingWaitTime=10):
        # pageLoadingWaitTime : 페이지 로딩을 기다리는 시간
        try:
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            self.driver.implicitly_wait(pageLoadingWaitTime)
        except Exception as e:
            print(e)

    def del_WebDriver(self):
        try:
            if not self.driver == None:
                self.driver.quit()
        except Exception as e:
            print(e)
    
    def get_WebDriver(self):
        if not self.driver == None:
            return self.driver

    def check_Page(self, url:str):
        result = url in self.driver.current_url
        currentFunc = sys._getframe(0).f_code.co_name
        calledFunc = sys._getframe(1).f_code.co_name

        self.logger.info('[{}] Function called [{}]'.format(calledFunc, currentFunc))
        self.logger.info('[{}] Result : {}'.format(currentFunc, result))
        self.logger.info('[{}] Current URL : {}'.format(currentFunc, self.driver.current_url))
        self.logger.info('[{}] Assert URL : {}'.format(currentFunc, url))

        return result

    def check_message(self, locator, text, waitTime=10):
        return self.find_element(locator, waitTime).text == text

    def find_element(self, locator, waitTime=10):
        """ 엘리먼트 찾기 """
        try:
            WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator) 
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))
        # 로깅 추가 필요함

    def find_elements(self, locator, waitTime=10):
        """ 엘리먼트 찾기 (배열로 리턴) """
        try:
            WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def move_url(self, url):
        """ URL 이동 """
        self.driver.get(url)

    def click_element(self, locator, waitTime=10):
        """ 클릭 """
        try:
            WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located(locator)).click()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def input_textfield(self, locator, text, waitTime=10):
        """ 인풋 필드 값 입력 """
        self.find_element(locator, waitTime).send_keys(text)