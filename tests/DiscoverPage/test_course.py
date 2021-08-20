import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog


'''
发现页：滑动加展示作品
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "P0", "TC1001")
@allure.feature('课程页播放视频测试')
# @allure.story('用例1')
@allure.severity('important')
def test_course_startVideo(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登陆
    点击创作
    点击课程进入播放页
    点击开始/停止播放视频
    点击退出播放页
    点击退出课程页
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5
    d.wait_timeout = 30.0
    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    assert recommend.wait()
    assert newest.wait()
    assert recommend.get_text()
    assert newest.get_text()

    with allure.step('点击 + 按钮'):
        logger.info('点击 + 按钮')
        # 点击创作按钮，+
        d(resourceId="com.codemao.nemo:id/createBtn").click()

    with allure.step('验证已正常打开创作方式页'):
        logger.info('验证已正常打开创作方式页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="边学边做"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击边学边做，进入课程页，并等待1s'):
        logger.info('点击边学边做，进入课程页，并等待1s')
        # 点击边学边做，进入课程页
        d(resourceId="com.codemao.nemo:id/item1_area").click()
        time.sleep(1)

    coures = d.xpath('//*[@text="你好编程猫"]')
    assert coures.wait()
    assert coures.get_text()
    with allure.step('点击进入播放页，并等待1s'):
        logger.info('点击进入播放页，并等待1s')
        # 点击课程进入播放页
        d(resourceId="com.codemao.nemo:id/root").click()
        time.sleep(1)

    create = d.xpath('//*[@text="去创作"]')
    assert create.wait()
    assert create.get_text()

    # with allure.step('点击播放视频'):
    #     logger.info('点击播放视频')
    #     # 点击播放视频
    #     d(resourceId="com.codemao.nemo:id/start").click()
        # time.sleep(0.5)
    # with allure.step('点击停止视频'):
    #     logger.info('点击停止视频')
    #     # 点击播放视频
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/surface_container"]/android.view.View[1]').click()

    with allure.step('点击返回，退出播放页并等待3s'):
        logger.info('点击返回，退出播放页')
        # 退出播放页
        time.sleep(5)
        # d(resourceId="com.codemao.nemo:id/back").click()
        d.press("back")
        time.sleep(3)
    coures = d.xpath('//*[@text="你好编程猫"]')
    assert coures.wait()
    assert coures.get_text()

    with allure.step('点击返回，退出课程页并等待3s'):
        logger.info('点击返回，退出课程页')
        # 退出课程页
        d(resourceId="com.codemao.nemo:id/left_view").click()


@allure.tag(f"environment:{ENV}", "P0", "TC1002")
@allure.feature('课程页去创作按钮测试')
# @allure.story('用例1')
@allure.severity('important')
def test_course_creat(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登录账号
    验证是否成功进入发现页面
    点击打开创作方式选择页
    验证是否成功打开创作方式选择页
    点击选择“边学边做”，进入课程页
    验证成功进入课程页面
    点击课程，进入播放页面
    点击去创作
    验证成功打开了创作页面并加载作品

    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5
    d.wait_timeout = 30.0
    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    assert recommend.wait()
    assert newest.wait()
    assert recommend.get_text()
    assert newest.get_text()
    with allure.step('点击 + 按钮'):
        logger.info('点击 + 按钮')
        # 点击创作按钮，+
        d(resourceId="com.codemao.nemo:id/createBtn").click()

    with allure.step('验证已正常打开创作方式页'):
        logger.info('验证已正常打开创作方式页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="边学边做"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击边学边做，进入课程页，并等待1s'):
        logger.info('点击边学边做，进入课程页，并等待1s')
        # 点击边学边做，进入课程页
        d(resourceId="com.codemao.nemo:id/item1_area").click()
        time.sleep(1)

    coures = d.xpath('//*[@text="你好编程猫"]')
    assert coures.wait()
    assert coures.get_text()
    with allure.step('点击进入播放页，并等待1s'):
        logger.info('点击进入播放页，并等待1s')
        # 点击课程进入播放页
        d(resourceId="com.codemao.nemo:id/root").click()
        time.sleep(1)

    create = d.xpath('//*[@text="去创作"]')
    assert create.wait()
    assert create.get_text()
    with allure.step('点击去创作'):
        logger.info('点击去创作')
        # 点击去创作按钮
        d(resourceId="com.codemao.nemo:id/createBtn").click()

    # with allure.step('验证加载作品提示，成功进入创作'):
    #     logger.info('验证加载作品提示，成功进入创作')
    #     # 验证成功进入创作
    #     role = d.xpath('//*[@text="作品加载中"]')
    #     assert role.wait()
    #     assert role.get_text()

    with allure.step('来到创作页内，点击左上角菜单按钮'):
        logger.info('来到创作页内，点击左上角菜单按钮')
        # 关键步骤，来到创作页等待一定时间再定位元素
        time.sleep(10)
        d(resourceId="com.codemao.nemo:id/menu", className="android.widget.ImageView").click()

    with allure.step('校验存在退出、发布、帮助按钮'):
        logger.info('校验存在退出、发布、帮助按钮')
        quit_button = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_quit"]')
        upload_button = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_upload"]')
        help_button = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_help"]')
        assert quit_button.get_text() == "退出"
        assert upload_button.get_text() == "发布"
        assert help_button.get_text() == "帮助"

    with allure.step('点击退出'):
        logger.info('点击退出')
        d(resourceId="com.codemao.nemo:id/tv_quit").click()


@allure.tag(f"environment:{ENV}", "P0", "TC1003")
@allure.feature('课程页全屏播放视频测试')
# @allure.story('用例1')
@allure.severity('important')
def test_FullScreen(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登陆
    点击选择创作方式
    点击课程进入播放页
    点击播放视频
    点击全屏按钮，进入全屏模式
    点击退出全屏
    点击退出播放页
    点击退出课程页

    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5
    d.wait_timeout = 30.0
    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    assert recommend.wait()
    assert newest.wait()
    assert recommend.get_text()
    assert newest.get_text()

    with allure.step('点击 + 按钮'):
        logger.info('点击 + 按钮')
        # 点击创作按钮，+
        d(resourceId="com.codemao.nemo:id/createBtn").click()

    with allure.step('验证已正常打开创作方式页'):
        logger.info('验证已正常打开创作方式页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="边学边做"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击边学边做，进入课程页，并等待1s'):
        logger.info('点击边学边做，进入课程页，并等待1s')
        # 点击边学边做，进入课程页
        d(resourceId="com.codemao.nemo:id/item1_area").click()
        time.sleep(1)

    coures = d.xpath('//*[@text="你好编程猫"]')
    assert coures.wait()
    assert coures.get_text()
    with allure.step('点击进入播放页，并等待1s'):
        logger.info('点击进入播放页，并等待1s')
        # 点击课程进入播放页
        d(resourceId="com.codemao.nemo:id/root").click()
        time.sleep(3)

        create = d.xpath('//*[@text="去创作"]')
        assert create.wait()
        assert create.get_text()

    with allure.step('点击全屏按钮并等待1'):
        logger.info('点击全屏按钮并等待1')
        # 点击播放视频
        d(resourceId="com.codemao.nemo:id/fullscreen").click()
        time.sleep(1)
    # with allure.step('点击播放视频'):
    #     logger.info('点击播放视频')
    #     # 点击播放视频
    #     d(resourceId="com.codemao.nemo:id/start").click()
        # time.sleep(0.5)
    # with allure.step('点击停止视频'):
    #     logger.info('点击停止视频')
    #     # 点击播放视频
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/surface_container"]/android.view.View[1]').click()

    with allure.step('点击返回，退出全屏并等待3s'):
        logger.info('点击返回，退出全屏')
        # 退出全屏模式
        d(resourceId="com.codemao.nemo:id/back").click()
        time.sleep(3)

    with allure.step('点击返回，退出播放页并等待3s'):
        logger.info('点击返回，退出播放页')
        # 退出播放页
        d(resourceId="com.codemao.nemo:id/back").click()
        time.sleep(3)
    coures = d.xpath('//*[@text="你好编程猫"]')
    assert coures.wait()
    assert coures.get_text()

    with allure.step('点击返回，退出课程页并等待3s'):
        logger.info('点击返回，退出课程页')
        # 退出课程页
        d(resourceId="com.codemao.nemo:id/left_view").click()


@allure.tag(f"environment:{ENV}", "P0", "TC1004")
@allure.feature('课程页全屏播放时去创作按钮测试')
# @allure.story('用例1')
@allure.severity('important')
def test_FullScreen_creat(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登陆
    点击创作
    点击课程进入播放页
    点击全屏按钮，进入全屏模式
    全屏模式点去创作按钮
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5
    d.wait_timeout = 30.0
    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    assert recommend.wait()
    assert newest.wait()
    assert recommend.get_text()
    assert newest.get_text()

    with allure.step('点击 + 按钮'):
        logger.info('点击 + 按钮')
        # 点击创作按钮，+
        d(resourceId="com.codemao.nemo:id/createBtn").click()

    with allure.step('验证已正常打开创作方式页'):
        logger.info('验证已正常打开创作方式页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="边学边做"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击边学边做，进入课程页，并等待1s'):
        logger.info('点击边学边做，进入课程页，并等待1s')
        # 点击边学边做，进入课程页
        d(resourceId="com.codemao.nemo:id/item1_area").click()
        time.sleep(1)

    coures = d.xpath('//*[@text="你好编程猫"]')
    assert coures.wait()
    assert coures.get_text()
    with allure.step('点击进入播放页，并等待1s'):
        logger.info('点击进入播放页，并等待1s')
        # 点击课程进入播放页
        d(resourceId="com.codemao.nemo:id/root").click()
        time.sleep(1)

    create = d.xpath('//*[@text="去创作"]')
    assert create.wait()
    assert create.get_text()

    with allure.step('点击全屏按钮并等待1'):
        logger.info('点击全屏按钮并等待1')
        # 点击播放视频
        d(resourceId="com.codemao.nemo:id/fullscreen").click()
        time.sleep(1)
    with allure.step('点击播放视频'):
        logger.info('点击播放视频')
        # 点击播放视频
        d(resourceId="com.codemao.nemo:id/start").click()
        # time.sleep(0.5)
    # with allure.step('点击停止视频'):
    #     logger.info('点击停止视频')
    #     # 点击播放视频
    #     d.xpath('//*[@resource-id="com.codemao.nemo:id/surface_container"]/android.view.View[1]').click()
    with allure.step('点击去创作'):
        logger.info('点击去创作')
        # 点击去创作按钮
        d(resourceId="com.codemao.nemo:id/create_l").click()

    with allure.step('验证加载作品提示，成功进入创作'):
        logger.info('验证加载作品提示，成功进入创作')
        # 验证进入创作成功
        role = d.xpath('//*[@text="作品加载中"]')
        assert role.wait()
        assert role.get_text()


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
    pytest.main(["-s", "-q", "test_course.py::test_FullScreen", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
