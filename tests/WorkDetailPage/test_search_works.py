import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog

'''
 搜索本地库 
 搜索已发布列表
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC0014")
@allure.feature('我的-本地搜索页')
@allure.story('本地搜索')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
# @pytest.mark.parametrize("KeyWords", ['测试', 'y', '作品', '1', '-'])
@pytest.mark.P0
def test_search_works_one(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证本地搜索是否能搜出对应结果
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.debug = True
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击复制草稿箱第一个作品复制按钮'):
        logger.info('点击复制草稿箱第一个作品复制按钮')
        d(resourceId="com.codemao.nemo:id/copy_iv").click()
        time.sleep(0.5)

    with allure.step('点击草稿箱第一个作品改名按钮'):
        logger.info('点击草稿箱第一个作品改名按钮')
        d(resourceId="com.codemao.nemo:id/iv_edit_name").click()

    with allure.step('更改作品名字为：本地搜索测试作品'):
        logger.info('更改作品名字为：本地搜索测试作品')
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        time.sleep(0.3)
        d.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
        d.send_keys("本地搜索测试作品")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()  #点击确认

    with allure.step('点击本地搜索按钮，输入关键词：本地搜索测试作品，并搜索'):
        logger.info('点击本地搜索按钮，输入关键词：本地搜索测试作品，并搜索')
        d(resourceId="com.codemao.nemo:id/right_view").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/animRoot").click()
        d.send_keys("本地搜索测试作品")  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        d.send_action("search")  # 模拟输入法的搜索
        time.sleep(0.5)

    with allure.step('搜索结果共有{}个,验证是否所有结果的标题都包含：本地搜索测试作品'):
        logger.info('搜索结果共有{}个,验证是否所有结果的标题都包含：本地搜索测试作品')
        for view in d(resourceId="com.codemao.nemo:id/works_name_tv"):
            assert "本地搜索测试作品" in view.get_text()
        count_number = len(d(resourceId="com.codemao.nemo:id/works_name_tv"))
        assert count_number > 0

    allure.attach("搜索结果个数: {}\n"
                  "搜索结果: {}\n".format(count_number,
                                      [view.get_text() for view in d(resourceId="com.codemao.nemo:id/works_name_tv")]),
                  '搜索结果个数及搜索结果', allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0015")
@allure.feature('我的-已发布搜索页')
@allure.story('已发布列表搜索')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.parametrize("KeyWords", ['作品', '-'])
@pytest.mark.P0
def test_search_works_two(login_and_logout183_module, stop_and_run_nemo, KeyWords):
    '''
    验证已发布列表是否能搜出对应结果
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.debug = True
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击本地搜索按钮，输入关键词：KeyWords，并搜索'):
        logger.info('点击本地搜索按钮，输入关键词：KeyWords，并搜索')
        d(resourceId="com.codemao.nemo:id/right_view").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/animRoot").click()
        d.send_keys(KeyWords)  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        d.send_action("search")  # 模拟输入法的搜索
        time.sleep(0.5)

    with allure.step('点击已发布标签页'):
        logger.info('点击已发布标签页')
        d(text="已发布").click()

    with allure.step('搜索结果共有{}个,验证是否所有结果的标题都包含：KeyWords'):
        logger.info('搜索结果共有{}个,验证是否所有结果的标题都包含：KeyWords')
        for view in d(resourceId="com.codemao.nemo:id/name_tv"):
            assert KeyWords in view.get_text()
        count_number = len(d(resourceId="com.codemao.nemo:id/name_tv"))
        assert count_number > 0

    allure.attach("搜索结果个数: {}\n"
                  "搜索结果: {}\n".format(count_number,
                                      [view.get_text() for view in d(resourceId="com.codemao.nemo:id/name_tv")]),
                  '搜索结果个数及搜索结果', allure.attachment_type.TEXT)


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
    pytest.main(["-s", "-q", "test_search_works.py", "--alluredir", path_xml])
    # pytest.main(["--lf", "-v", "test_cloud.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
