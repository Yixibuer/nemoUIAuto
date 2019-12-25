import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog
from time import sleep
from common.read_excel import read_excel
from dir_config import testdatas_dir

filename = testdatas_dir + "从模板创作.xlsx"

test_datas = list(read_excel(filename, 'data'))

# print(filename)
'''
测试从模板创作
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "P0", "TC2005")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj1
# login_and_logout183_module, stop_and_run_nemo
def test_env_draft_mould(login_and_logout183_module, stop_and_run_nemo):
    '''
    登录成功后，通过‘从模板创作’创建作品可以成功
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step("点击我的——进入我的页面"):
        logger.info('进入我的页面')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
        sleep(4)
    for test_num in test_datas:
        j = test_num['num']
        index = test_num['index']
        tv_name = test_num['name']
        tv_content = test_num['content']
        with allure.step("点击+进入创作页面"):
            logger.info('点击+按钮')
            d(resourceId="com.codemao.nemo:id/createBtn").click()
        with allure.step("选择边学边做"):
            sleep(3)
            logger.info('选择“从模板创建”')
            d(resourceId="com.codemao.nemo:id/item2_name").click()
            sleep(5)
        with allure.step('进入从模板创作：{}'.format(tv_name)):
            logger.info('从模板创做作品‘{}’'.format(tv_name))
            for i in range(0, j - 1):
                d.swipe_ext("left", scale=0.8)
                sleep(3)
            logger.info('左滑{}次'.format(j - 1))
            logger.info('模板的序号为：{}'.format(d(resourceId='com.codemao.nemo:id/index').get_text()))
            logger.info('模板的名称为：{}'.format(d(resourceId='com.codemao.nemo:id/tv_name').get_text()))
            logger.info('模板的说明为：{}'.format(d(resourceId='com.codemao.nemo:id/tv_content').get_text()))
            assert d(resourceId='com.codemao.nemo:id/index').get_text() == index
            assert d(resourceId='com.codemao.nemo:id/tv_name').get_text() == tv_name
            assert d(resourceId='com.codemao.nemo:id/tv_content').get_text() == tv_content
            logger.info('点击“立即创作”')
            d(resourceId="com.codemao.nemo:id/tv_enter").click()
            sleep(15)
            logger.info('点击“菜单”')
            d(resourceId="com.codemao.nemo:id/menu").click()
            sleep(2)
            logger.info('点击“退出”')
            d(resourceId="com.codemao.nemo:id/tv_quit").click()
            sleep(2)
            logger.info('点击“好的”')
            d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        draft_id = d.xpath('//*[@text="{}-副本"]'.format(tv_name))
        assert draft_id.wait()
        assert draft_id.get_text() == "{}-副本".format(tv_name)
        logger.info('{}-副本，创建成功'.format(tv_name))


if __name__ == '__main__':
    import subprocess
    import sys
    import os
    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_draft_mould.py", "--alluredir", path_xml])
    # pytest.main(["-lf", "-q", "-s", "test_work_detail.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
