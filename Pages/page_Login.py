from Pages.page_Base import BasePage
from selenium.webdriver.common.by import By


class Login(BasePage):
    textfield_id = (By.NAME, 'userId')
    textfield_pw = (By.NAME, 'userPassword')
    button_login = (By.NAME, 'submit')

    login_url = 'https://test-gpms.gooroom.kr/gpms/login'

    def __init__(self, driver):
        super(Login, self).__init__(driver)

    def get_login_page(self):
        self.get(self.login_url)

    def send_keys_id(self, id):
        self.input_text(self.textfield_id, id)

    def send_keys_pw(self, pw):
        self.input_text(self.textfield_pw, pw)

    def click_login_btn(self):
        self.click(self.button_login)