from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get(self, url):
        """ URL 이동 """
        self.driver.get(url)

    def click(self, locator, waitTime=10):
        """ 클릭 """
        try:
            WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located(locator)).click()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

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

    def input_text(self, locator, text, waitTime=10):
        """ 인풋 필드 값 입력 """
        self.find_element(locator, waitTime).send_keys(text)