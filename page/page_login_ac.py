# -*- coding: utf-8 -*-
import allure

from page.base_page import BasePage
from page.page_register import RegPage


class LoginPage(BasePage):

    def __init__(self):
        self._account = (self.MB.ID, 'edit_user_name')
        self._password = (self.MB.ID, 'et_password')
        self._login_bt = (self.MB.ID, 'bt_Login')
        self._register = (self.MB.ID, 'tv_register')
        self._forget_pw = (self.MB.ID, 'tv_forget')
        self._go_back = (self.MB.ID, 'iv_close')

    @allure.step('输入用户名 <{account}>')
    def _input_account(self, account: str):
        self.find(self._account).send_keys(account)

    @allure.step('输入用户名 <{pw}>')
    def _input_password(self, pw: str):
        self.find(self._password).send_keys(pw)

    @allure.step('点击登录按钮')
    def _tap_login_bt(self):
        self.find(self._login_bt).click()

    def login(self, account, pw):
        self._input_account(account)
        self._input_password(pw)
        self._tap_login_bt()

    @allure.step('点击「新用户注册」')
    def tap_register(self):
        self.find(self._register).click()
        return RegPage()

    @allure.step('点击「忘记密码」')
    def tap_forget_pw(self):
        self.find(self._forget_pw).click()
        return
