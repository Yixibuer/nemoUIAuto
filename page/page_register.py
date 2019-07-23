# -*- coding: utf-8 -*-
from page.base_page import BasePage


class RegPage(BasePage):

    def __init__(self):
        self._phone_number = (self.MB.ID, 'et_phone')
        self._ver_code = (self.MB.ID, 'et_code')
        self._get_ver_code = (self.MB.ID, 'tv_get_code')
        self._register_bt = (self.MB.ID, 'btn_next_step')
        self._provision = (self.MB.ID, 'tv_private_provision')
