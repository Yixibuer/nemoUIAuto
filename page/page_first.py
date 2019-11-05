# -*- coding: utf-8 -*-
import allure

from page.base_page import BasePage
from page.page_login_ac import LoginPageAC


class FirstPage(BasePage):

    def __init__(self):
        self._login_by_we = (self.MB.ID, 'iv_Login_Wechat')
        self._login_by_qq = (self.MB.ID, 'iv_Login_QQ')
        self._login_by_ac = (self.MB.ID, 'iv_Login_account')

    @allure.step('选择账号登录方式')
    def tap_login_by_ac_bt(self):
        self.find(self._login_by_ac).click()
        return LoginPageAC()

    @allure.step('选择微信登录方式')
    def tap_login_by_we_bt(self):
        self.find(self._login_by_we).click()

    @allure.step('选择QQ登录方式')
    def tap_login_by_qq_bt(self):
        self.find(self._login_by_qq).click()
