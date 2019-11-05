# -*- coding: utf-8 -*-
import allure

from page.page_register import RegPage


class FindPWPage(RegPage):

    def __init__(self):
        super(FindPWPage, self).__init__()

    @allure.step('点击「找回密码」按钮')
    def tap_find_pw_bt(self):
        self.find(self._register_bt).click()
