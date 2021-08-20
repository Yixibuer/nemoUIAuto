import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog

'''
作品举报测试用例
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC0013")
@allure.feature('作品举报页')
@allure.story('作品举报-色情低俗内容')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_report_one(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品详情页里关注按钮功能是否有效
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # 这个用例的“稍后打开”消失较快，所以用0s间隔去点击
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('获取自己昵称'):
        logger.info('获取自己昵称')
        my_name = d(resourceId="com.codemao.nemo:id/author_name_tv").get_text()

    with allure.step('点击“发现”'):
        logger.info('点击“发现”')
        d(resourceId="com.codemao.nemo:id/discover_rb").click()

    with allure.step('找寻作品，如果不是自己名字，才点击进去(点进去按钮是已关注，退出滑动再寻找)'):
        logger.info('找寻作品，如果不是自己名字，才点击进去(点进去按钮是已关注，退出滑动再寻找)')
        while True:
            logger.info('找寻作品，如果不是自己名字，才点击进去')
            # 自动匹配第一个，即使有多个元素拥有此ID
            user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
            if user_name == my_name:
                d.swipe_ext("up", scale=0.1)
            else:
                d(text=user_name).click()
                break

    with allure.step('点击三点按钮'):
        logger.info('点击三点按钮')
        d(resourceId="com.codemao.nemo:id/iv_more").click()

    with allure.step('点击举报按钮'):
        logger.info('点击举报按钮')
        d(text="举报").click()
        time.sleep(0.5)

    with allure.step('点击选中“色情低俗内容”'):
        logger.info('点击选中“色情低俗内容”')
        d(resourceId="com.codemao.nemo:id/cb_reason_yellow").click()

    with allure.step('点击选中文本输入框'):
        logger.info('点击选中文本输入框')
        d(resourceId="com.codemao.nemo:id/edit_tip_reason").click()

    with allure.step('输入原因：举报色情测试'):
        logger.info('输入原因：举报色情测试')
        d.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d.send_keys("举报色情测试")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        d.send_action("search")  # 模拟输入法的搜索

    with allure.step('点击确定按钮'):
        logger.info('点击确定按钮')
        d(resourceId="com.codemao.nemo:id/tv_commit").click()

    with allure.step('检验弹出toast是否包含：感谢您对Nemo社区的支持!'):
        logger.info('检验弹出toast是否为：感谢您对Nemo社区的支持!')
        message = d.toast.get_message()
        assert "感谢您对Nemo社区的支持!" in message


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
    pytest.main(["-s", "-q", "test_work_report.py::test_work_report_one", "--alluredir", path_xml])
    # pytest.main(["-lf", "-q", "-s", "test_work_detail.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
