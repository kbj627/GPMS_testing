import logging
from TestCases.test_Base import BaseTest
from Pages.page_Login import Login


class Test_Login(BaseTest):
    path_gpms_Home = '/gpms/home#/'

    @classmethod
    def setup_class(cls):
        cls.set_gpms_Domain(cls, url_gpms_Domain='https://test-gpms.gooroom.kr')
        cls.init_Logger(cls, logLevel=logging.INFO)
        cls.init_Webdriver(cls)

    @classmethod
    def teardown_class(cls):
        cls.del_WebDriver(cls)

    def test_login(self):
        login = Login()
        login.get_login_page()
        login.send_keys_id('admin4')
        login.send_keys_pw('Qwer12#$')
        login.click_login_btn()
        
        assert self.url_compare(path=self.path_gpms_Home)

