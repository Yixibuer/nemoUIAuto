import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog

'''
云端测试用例
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC0001")
@allure.feature('云端作品页')
@allure.story('云端搜索')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
# @pytest.mark.parametrize("KeyWords", ['测试', 'y', '作品', '1', '-'])
@pytest.mark.P0
def test_cloud_one(login_and_logout183_module, stop_and_run_nemo, SearchKeyWords):
    '''
    验证云端搜索是否能搜出对应结果
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.debug = True
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击“云端”按钮'):
        logger.info('点击“云端”按钮')
        d(resourceId="com.codemao.nemo:id/cloud_down_iv").click()

    with allure.step('点击搜索按钮，输入关键词：SearchKeyWords，并搜索'):
        logger.info('点击搜索按钮，输入关键词：SearchKeyWords，并搜索')
        d(resourceId="com.codemao.nemo:id/right_view").click()
        d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        d(resourceId="com.codemao.nemo:id/animRoot").click()
        d.send_keys(SearchKeyWords)  # adb广播输入
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        d.send_action("search")  # 模拟输入法的搜索

        CountNumber = len(d(resourceId="com.codemao.nemo:id/name_tv"))

    with allure.step('搜索结果共有{}个,验证是否所有结果的标题都包含SearchKeyWords'.format(CountNumber)):
        logger.info('搜索结果共有{}个,验证是否所有结果的标题都包含SearchKeyWords'.format(CountNumber))
        for view in d(resourceId="com.codemao.nemo:id/name_tv"):
            assert SearchKeyWords in view.get_text()

    allure.attach("搜索结果个数: {}\n"
                  "搜索结果: {}\n".format(CountNumber,
                                      [view.get_text() for view in d(resourceId="com.codemao.nemo:id/name_tv")]),
                  '用例参数', allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0002")
@allure.feature('云端作品页')
@allure.story('云端删除')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_cloud_two(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证云端作品取消删除按钮功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击“云端”按钮'):
        logger.info('点击“云端”按钮')
        d(resourceId="com.codemao.nemo:id/cloud_down_iv").click()

    with allure.step('获取当前页所有作品状态，存到一个列表中'):
        logger.info('获取当前页所有作品状态，存到一个列表中')
        work_names = [view.get_text() for view in d(resourceId="com.codemao.nemo:id/time_tv")]

    with allure.step('逐一从中选出看有无“更新”(已发布作品不能删除，更新的才能删除)两字，有则获取作品名字，点击删除按钮，'
                     '第一个删除按钮必定匹配该作品；无则上滑屏幕宽度的10%寻找'):
        logger.info('逐一从中选出看有无“更新”(已发布作品不能删除，更新的才能删除)两字，有则获取作品名字，点击删除按钮，'
                    '第一个删除按钮必定匹配该作品；无则上滑屏幕宽度的10%寻找')
        while True:
            # 自动匹配第一个，即使有多个元素拥有此ID
            work_times = d(resourceId="com.codemao.nemo:id/time_tv").get_text()
            if "更新" not in work_times:
                d.swipe_ext("up", scale=0.1)
            else:
                first_work = d(text=work_times).up(resourceId="com.codemao.nemo:id/name_tv").get_text()
                d(resourceId="com.codemao.nemo:id/remove_iv").click()
                break

    with allure.step('点击取消'):
        logger.info('点击取消')
        d(resourceId="com.codemao.nemo:id/remove_cancel").click()

    with allure.step('检查第一个作品是否仍在当前页'):
        logger.info('检查第一个作品是否仍在当前页')
        work_names = [view.get_text() for view in d(resourceId="com.codemao.nemo:id/name_tv")]
        j = 0
        for now_first_name in work_names:
            if now_first_name == first_work:
                j += 1
                break
        if j == 0:
            raise Exception("点击了取消按钮，但作品被删除了")

    allure.attach("first_work: {}\n"
                  "now_first_name: {}\n".format(first_work, now_first_name), '用例参数', allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0003")
@allure.feature('云端作品页')
@allure.story('云端删除')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_cloud_three(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证云端作品删除按钮功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击“云端”按钮'):
        logger.info('点击“云端”按钮')
        d(resourceId="com.codemao.nemo:id/cloud_down_iv").click()

    with allure.step('获取当前页所有作品状态，存到一个列表中'):
        logger.info('获取当前页所有作品状态，存到一个列表中')
        work_names = [view.get_text() for view in d(resourceId="com.codemao.nemo:id/time_tv")]

    with allure.step('逐一从中选出看有无“更新”(已发布作品不能删除，更新的才能删除)两字，有则获取作品名字，点击删除按钮，'
                     '第一个删除按钮必定匹配该作品；无则上滑屏幕宽度的10%寻找'):
        logger.info('逐一从中选出看有无“更新”(已发布作品不能删除，更新的才能删除)两字，有则获取作品名字，点击删除按钮，'
                    '第一个删除按钮必定匹配该作品；无则上滑屏幕宽度的10%寻找')
        while True:
            # 自动匹配第一个，即使有多个元素拥有此ID
            work_times = d(resourceId="com.codemao.nemo:id/time_tv").get_text()
            if "更新" not in work_times:
                d.swipe_ext("up", scale=0.1)
            else:
                first_work = d(text=work_times).up(resourceId="com.codemao.nemo:id/name_tv").get_text()
                d(resourceId="com.codemao.nemo:id/remove_iv").click()
                break

    with allure.step('点击确定，删除该作品'):
        logger.info('点击确定，删除该作品')
        d(resourceId="com.codemao.nemo:id/remove_confirm").click()

    with allure.step('检查第一个作品是否仍在当前页'):
        logger.info('检查第一个作品是否仍在当前页')
        time.sleep(5)
        work_names = [view.get_text() for view in d(resourceId="com.codemao.nemo:id/name_tv")]
        j = 0
        for now_first_name in work_names:
            if now_first_name == first_work:
                j += 1
                break
        if j != 0:
            raise Exception("点击了删除按钮，但作品没有被删除了")

    allure.attach("first_work: {}\n"
                  "now_first_name: {}\n".format(first_work, work_names), '用例参数', allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0004")
@allure.feature('云端作品页')
@allure.story('云端下载')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_cloud_four(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证云端作品下载功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('获取当前草稿箱第一个作品名字'):
        logger.info('获取当前草稿箱第一个作品名字')
        first_box_work = d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()

    with allure.step('点击“云端”按钮'):
        logger.info('点击“云端”按钮')
        d(resourceId="com.codemao.nemo:id/cloud_down_iv").click()

    with allure.step('获取云端列表第一个作品名字'):
        logger.info('获取云端列表第一个作品名字')
        first_work_name = d(resourceId="com.codemao.nemo:id/name_tv").get_text()

    with allure.step('点击第一个作品下载按钮，下载该作品'):
        logger.info('点击第一个作品下载按钮，下载该作品')
        d(resourceId="com.codemao.nemo:id/download_iv").click()

    with allure.step('点击返回按钮，返回草稿箱页面'):
        logger.info('点击返回按钮，返回草稿箱页面')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    with allure.step('获取草稿箱当前第一个作品名字'):
        logger.info('获取草稿箱当前第一个作品名字')
        first_box_work_now = d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()

    with allure.step('判断云端第一个作品名字包含于草稿箱第一个作品'):
        logger.info('判断云端第一个作品名字包含于草稿箱第一个作品')
        assert first_work_name in first_box_work_now

    with allure.step('判断草稿箱第一个作品名字不等于原来的第一个作品'):
        logger.info('判断草稿箱第一个作品名字不等于原来的第一个作品')
        assert first_box_work_now != first_box_work

    allure.attach("草稿箱初始第一个作品名字first_box_work: {}\n"
                  "云端第一个作品名字first_work_name: {}\n"
                  "获取草稿箱当前第一个作品名字first_box_work_now: {}\n".format(first_box_work, first_work_name,
                                                                  first_box_work_now), '用例参数',
                  allure.attachment_type.TEXT)


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
    pytest.main(["-s", "-q", "test_cloud.py", "--alluredir", path_xml])
    # pytest.main(["--lf", "-v", "test_cloud.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
