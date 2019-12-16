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


@allure.tag(f"environment:{ENV}", "P0", "TC1005")
@allure.feature('“地底寻宝”模板作品测试')
# @allure.story('用例1')
@allure.severity('important')
def test_mould_create(login_and_logout183):
    '''
    启动App并登录
    点击“+”
    验证创作方式展示页已成功打开
    点击"从模版创建"，进入模版页面，并等待1s
    验证选择模版1"地底寻宝"作品去创作
    验证加载作品提示，成功进入创作成功
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0

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
        learn = d.xpath('//*[@text="从模版创建"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击"从模版创建"，进入模版页面，并等待1s'):
        logger.info('点击"从模版创建"，进入模版页面，并等待1s')
        # 点击从模版创建，进入模版页面
        d(resourceId="com.codemao.nemo:id/item2_area").click()
        time.sleep(1)

    with allure.step('验证已成功打开模版页'):
        logger.info('验证已成功打开模版页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="选择模版"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('验证选择模版1"地底寻宝"作品去创作'):
        logger.info('验证选择模版1"地底寻宝"作品去创作')
        # 验证选择1-8模版作品去创作
        # bcm = {"地底寻宝", "源码画板", "唱片机", "声控捕鱼", "贪吃猴", "飞翔的蓝雀", "躲避弹球", "丛林爬爬"}
        # el = d.xpath('//*[@text="地底寻宝"]')
        d(resourceId="com.codemao.nemo:id/tv_enter").click()

        # for b in bcm:
        #     if b == bcm[1]:
        #     d(resourceId="com.codemao.nemo:id/tv_enter").click()

    with allure.step('验证加载作品提示，成功进入创作成功'):
        logger.info('验证加载作品提示，成功进入创作')
        # 验证成功进入创作
        load = d.xpath('//*[@text="作品加载中"]')
        assert load.wait()
        assert load.get_text()
        time.sleep(10)


@allure.tag(f"environment:{ENV}", "P0", "TC1006")
@allure.feature('自由创作按钮测试')
# @allure.story('用例1')
@allure.severity('important')
def test_free_create(login_and_logout183):
    '''
    启动App并登录
    点击“+”
    验证创作方式展示页已成功打开
    点击选择 从模版创建
    模版页面已成功打开

    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay

    d.wait_timeout = 30.0  # default 20.0

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
        learn = d.xpath('//*[@text="自由创作"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击"自由创作"，进入创作页面'):
        logger.info('点击"自由创作"，进入创作页面')
        # 点击"自由创作"，进入创作页面
        d(resourceId="com.codemao.nemo:id/item3_area").click()
        time.sleep(1)

    with allure.step('验证加载作品提示，成功进入创作成功'):
        logger.info('验证加载作品提示，成功进入创作')
        # 验证成功进入创作
        load = d.xpath('//*[@text="作品加载中"]')
        assert load.wait()
        assert load.get_text()
        time.sleep(10)
    yield

    # with allure.step('验证成功进入创作成功'):
    #     logger.info('验证成功进入创作')
    #     # 验证成功进入创作
    #     role = d.xpath('//*[@text="添加角色"]')
    #     # role = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_add_role"]')
    #     assert role.wait()
    #     assert role.get_text()
    #     time.sleep(30)

    # with allure.step('点击菜单按钮'):
    #     logger.info('点击菜单按钮')
    #     # 点击菜单按钮
    #     d(resourceId="com.codemao.nemo:id/menu").click()
    #     time.sleep(5)


@allure.tag(f"environment:{ENV}", "P0", "TC1007")
@allure.feature('创作方式选择页面关闭按钮测试')
# @allure.story('用例1')
@allure.severity('important')
def test_cancel_create(login_and_logout183):
    '''
    启动App并登录
    点击“+”
    验证创作方式展示页已成功打开
    点击关闭按钮，取消创作
    验证已回到发现首页，创作方式展示页已成功关闭

    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay

    d.wait_timeout = 30.0  # default 20.0

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
        learn = d.xpath('//*[@text="自由创作"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击"从模版创建"，进入模版页面，并等待1s'):
        logger.info('点击"从模版创建"，进入模版页面，并等待1s')
        # 点击从模版创建，进入模版页面
        d(resourceId="com.codemao.nemo:id/item2_area").click()
        time.sleep(1)

    with allure.step('验证已成功打开模版页'):
        logger.info('验证已成功打开模版页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="选择模版"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('从右向左滑动'):
        logger.info('从右向左滑动')
        # 从右向左滑动
        t = d.xpath('//*[@resource-id="com.codemao.nemo:id/viewPager"]/android.widget.FrameLayout[1]').get()
        t.swipe("left")
        time.sleep(1)

    with allure.step('从左向右滑动'):
        logger.info('从左向右滑动')
        # 从左向右滑动
        t = d.xpath('//*[@resource-id="com.codemao.nemo:id/viewPager"]/android.widget.FrameLayout[2]').get()
        t.swipe("right")
        time.sleep(1)

    with allure.step('点击退出模版页'):
        logger.info('点击退出模版页')
        # 点击退出模版页
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        time.sleep(1)

    with allure.step('验证已成功关闭模版页'):
        logger.info('验证已成功关闭模版页')
        # 验证已正常打开创作方式页
        learn = d.xpath('//*[@text="边学边做"]')
        assert learn.wait()
        assert learn.get_text()

    with allure.step('点击关闭按钮'):
        logger.info('点击关闭按钮')
        # 点击关闭按钮
        d(resourceId="com.codemao.nemo:id/cancel").click()
        time.sleep(1)

    with allure.step('验证已成功关闭创作方式页，回到发现首页'):
        logger.info('验证已成功关闭创作方式页，回到发现首页')
        # 验证已成功创作方式页，回到发现首页
        learn = d.xpath('//*[@text="推荐"]')
        assert learn.wait()
        assert learn.get_text()

    yield


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
    pytest.main(["-s", "-q", "test_create.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
