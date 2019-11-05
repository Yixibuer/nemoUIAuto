# -*- coding: utf-8 -*-
from page.page_first import FirstPage


def test_login_by_ac_with_right_author(init_test):
    p_first = FirstPage()
    p_login = p_first.tap_login_by_ac_bt()
    p_login.login('18339956220', 'qwe123')
