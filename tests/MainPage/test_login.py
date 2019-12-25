import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog


'''
起始页：未登录点击进入Nemo第一页
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", 'TC0000')
@allure.feature('登录页')
@allure.story('编程猫账号登录')
@allure.severity('critical')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_env_login_one(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证是否可以正常登录Nemo
    启动App
    点击切换环境按钮
    选择test环境并等待0.5s
    选择编程猫账号登录
    点击账号，并切换成FastInputIME输入法输入username183
    点击密码，输入password183
    切换回正常输入法并点击登录按钮
    校验是否成功登录并进入首页，推荐按钮text校验, 最新按钮text校验。
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    # print(d.info)

    # # #第一种方法，启动App（包名）
    # #为避免正在运行先停止
    # with allure.step('为避免正在运行先停止'):
    #     logger.info('为避免正在运行先停止')
    #     d.app_stop("com.codemao.nemo")
    #
    # with allure.step('第一种方法，启动App（包名）'):
    #     logger.info('第一种方法，启动App（包名）')
    #     d.app_start("com.codemao.nemo")
    #     d.app_wait("com.codemao.nemo", front=True) # 等待应用前台运行
    #     d.app_wait("ccom.codemao.nemo", timeout=10.0) # 最长等待时间20s（默认）
    #     pid = d.app_wait("com.codemao.nemo") # 等待应用运行, return pid(int)
    #     if not pid:
    #         print("com.codemao.nemo is not running")
    #     else:
    #         print("ccom.codemao.nemo pid is %d" % pid)
    #
    # # 第二种方法，启动App(包名)，使用session
    # # launch app if not running, skip launch if already running
    # # d.app_stop("com.codemao.nemo")
    # # nemo = d.session("com.codemao.nemo")
    # # nemo.click_post_delay = 0.5 # default no delay
    # # nemo.wait_timeout = 30.0 # default 20.0
    # # nemo.implicitly_wait(30)
    # with allure.step('设置xpath全局等待10s'):
    #     logger.info('设置xpath全局等待10s')
    #     d.xpath.global_set("timeout", 10)
    # # pprint.pprint(nemo.info)
    #
    # with allure.step('点击切换环境按钮'):
    #     logger.info('点击切换环境按钮')
    #     d(resourceId="com.codemao.nemo:id/tv_change").click()
    #
    # with allure.step('选择test环境并等待0.5s'):
    #     logger.info('选择test环境并等待0.5s')
    #     d(resourceId="com.codemao.nemo:id/tv_test").click()
    #     time.sleep(0.5)
    #
    # with allure.step('选择编程猫账号登录'):
    #     logger.info('选择编程猫账号登录')
    #     d(resourceId="com.codemao.nemo:id/iv_Login_account").click()
    #
    # with allure.step('点击账号，并切换成FastInputIME输入法输入username183'):
    #     logger.info('点击账号，并切换成FastInputIME输入法输入username183')
    #     d(resourceId="com.codemao.nemo:id/edit_user_name").click()
    #     d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
    #     d.send_keys(f"{username183}")  # adb广播输入
    #
    # with allure.step('点击密码，输入password183'):
    #     logger.info('点击密码，输入password183')
    #     d(resourceId="com.codemao.nemo:id/et_password").click()
    #     d.send_keys(f"{password183}")  # adb广播输入
    #
    # with allure.step('切换回正常输入法并点击登录按钮'):
    #     logger.info('切换回正常输入法并点击登录按钮')
    #     d.set_fastinput_ime(False)  # 切换成正常的输入法
    #     d(resourceId="com.codemao.nemo:id/bt_Login").click()

    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    #.wait()没找到返回None，.get()没找到直接抛出XPathElementNotFoundError 异常。默认等待时间10s
    # print(recommend.wait())
    # print(newest.wait())
    # print(moni.wait())
    # recommend.get()
    # newest.get()
    # moni.get()
    assert recommend.wait()
    assert newest.wait()
    assert recommend.get_text()
    assert newest.get_text()

    # with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
    #         recommend.get_text(), newest.get_text())):
    #     logger.info('校验是否成功登录并进入首页')
    #     assert recommend.get_text() == "推荐"
    #     assert newest.get_text() == "最新"


if __name__ == '__main__':
    import subprocess
    import sys
    import os

    # pytest.main(["-v", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "-s", "test_ban_and_recover_login.py"])
    # pytest.main(["-v", "--setup-show", "test_ban_and_recover_login.py"])
    # 运行全部test用例
    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_login.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
