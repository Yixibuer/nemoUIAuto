#-*- coding:utf-8 _*-
"""
@author: hzj
@time: 2019/09/25
@software: PyCharm
@filename：dir_config.py
@Description:各文件夹的路径aa
"""

import os


'''
各文件夹的路径
'''
cur_dir=os.path.split(os.path.abspath(__file__))[0]

# print(cur_dir,type(cur_dir))


testcase_dir=cur_dir+'\\tests\\'

htmlreport_dir=cur_dir+'\\report\\'

log_dict=cur_dir+'\\logs\\'

testdatas_dir=cur_dir+'\\data\\'

