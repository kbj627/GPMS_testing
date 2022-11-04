import logging, pytest
from TestCases.test_Base import BaseTest
from Pages.page_Login import PageLogin


class Test_Login(BaseTest):
    url_LoginPage = 'https://test-gpms.tmaxos.com/gpms/login'
    url_HomePage = 'https://test-gpms.tmaxos.com/gpms/home#'
    login_id = 'admin4'
    login_pw = 'Qwer12#$'

    @classmethod
    def setup_class(cls):
        cls.init_Logger(cls, logLevel=logging.INFO)

    @classmethod
    def teardown_class(cls):
        pass

    def test_login_Success(self):
        page = PageLogin()
        page.move_login_page(self.url_LoginPage)
        page.input_textfield_id(self.login_id)
        page.input_textfield_pw(self.login_pw)
        page.click_login_btn()
        
        assert page.check_Page(url=self.url_HomePage, logger=self.logger)

    @pytest.mark.skip(reason='pause')
    def test_login_Fail_InvalidID(self):
        page = PageLogin()
        page.move_login_page(self.url_LoginPage)
        page.input_textfield_id(self.login_id + 'invalidID')
        page.input_textfield_pw(self.login_pw)
        page.click_login_btn()
        
        assert page.check_login_message('계정 정보가 잘못 되었습니다.')

    @pytest.mark.skip(reason='pause')
    def test_login_Fail_InvalidPW(self):
        page = PageLogin()
        page.move_login_page(self.url_LoginPage)
        page.input_textfield_id(self.login_id)
        page.input_textfield_pw(self.login_pw + 'invalidPW')
        page.click_login_btn()

        assert page.check_login_message('계정 정보가 잘못 되었습니다.')