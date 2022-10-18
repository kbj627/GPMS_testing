from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    def __init__(self):
        self.init_Webdriver()

    def __del__(self):
        self.del_WebDriver()

    def init_Webdriver(self):
        try:
            chrome_options = webdriver.ChromeOptions()
            #chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
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