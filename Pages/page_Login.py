from Pages.page_Base import PageBase
from selenium.webdriver.common.by import By


class PageLogin(PageBase):
    textfield_id = (By.NAME, 'userId')
    textfield_pw = (By.NAME, 'userPassword')
    #button_login = (By.NAME, 'submit')
    button_login = (By.XPATH, '//input[@value="로그인"]')
    message_login_failed = (By.XPATH, '/html/body/div/div/form/p')

    def move_login_page(self, url):
        self.move_url(url)

    def input_textfield_id(self, id):
        self.input_textfield(self.textfield_id, id)

    def input_textfield_pw(self, pw):
        self.input_textfield(self.textfield_pw, pw)

    def click_login_btn(self):
        self.click_element(self.button_login)

    def check_login_message(self, text):
        return self.check_message(self.message_login_failed, text)