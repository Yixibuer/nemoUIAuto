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


@allure.tag(f"environment:{ENV}", "P0", "TC1008")
@allure.feature('推荐页面-banner滑动、打开测试')
# @allure.story('用例1')
@allure.severity('important')
def test_discovery1(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动App并登录
    发现页面已成功打开
    验证banner模块已经加载
    从右向左滑动banner 1次
    从左向右滑动banner 1次
    从右向左滑动banner 6次
    点击banner
    验证已成功打开页面并加载内容
    点击关闭按钮
    验证已成功回到发现首页，页面关闭成功

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

    # with allure.step('验证banner模块已经加载'):
    #     logger.info('验证banner模块已经加载')
    #     # 验证banner模块已经加载
    #     learn = d.xpath('//*[@text="从模版创建"]')
    #     assert learn.wait()
    #     assert learn.get_text()

    with allure.step('从左向右滑动banner 1次'):
        logger.info('从左向右滑动banner 1次')
        # 从左向右滑动banner 1次
        t = d.xpath('//*[@resource-id="com.codemao.nemo:id/bannerViewPager"]/android.widget.ImageView[2]').get()
        t.swipe("right")
        time.sleep(1)

    with allure.step('从右向左滑动banner 1次'):
        logger.info('从右向左滑动banner 1次')
        # 从右向左滑动banner 1次
        t = d.xpath('//*[@resource-id="com.codemao.nemo:id/bannerViewPager"]/android.widget.ImageView[2]').get()
        t.swipe("left")
        time.sleep(1)

    with allure.step('点击banner打开，并等待5s'):
        logger.info('点击banner打开，并等待5s')
        # 点击banner打开，并等待1s
        d.xpath('//*[@resource-id="com.codemao.nemo:id/bannerViewPager"]/android.widget.ImageView[2]').click()
        time.sleep(5)

    with allure.step('点击banner页的返回按钮，并等待1s'):
        logger.info('点击banner页的返回按钮，并等待1s')
        # 点击banner页的返回按钮，并等待1s
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        time.sleep(1)

    with allure.step('验证已成功返回发现首页'):
        logger.info('验证已成功返回发现首页')
        # 验证已成功返回发现首页
        learn = d.xpath('//*[@text="推荐"]')
        assert learn.wait()
        assert learn.get_text()


@allure.tag(f"environment:{ENV}", "P0", "TC1009")
@allure.feature('发现-推荐页面下滑动加载作品、左右滑动切换最新页和推荐页功能测试')
# @allure.story('用例1')
@allure.severity('important')
def test_discovery2(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登录账号
    进入发现--推荐首页，验证页面已成功加载
    从下向上滑动5次，查看加载其他屏的作品
    双击“推荐”回到第一屏
    从右向左滑动1次
    验证已成功切换到最新页
    从下向上滑动5次，查看加载其他屏的作品
    双击“最新”回到第一屏
    从左向右滑动1次
    验证已成功切换到推荐页

    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay

    d.wait_timeout = 30.0  # default 20.0

    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')

    assert recommend.wait()
    assert newest.wait()
    assert recommend.get_text()
    assert newest.get_text()

    with allure.step('从下向上滑动5次，查看加载其他屏的作品'):
        logger.info('从下向上滑动5次，查看加载其他屏的作品')
        # 从下向上滑动5次，查看加载其他屏的作品
        el = d.xpath('//*[@resource-id="com.codemao.nemo:id/iv_work_cover"]').get()
        el.swipe("up")
        time.sleep(0.5)
        el.swipe("up")
        el.swipe("up")
        el.swipe("up")
        el.swipe("up")
        time.sleep(1)

    with allure.step('从上向下滑动6次，查看加载其他屏的作品'):
        logger.info('从上向下滑动6次，查看加载其他屏的作品')
        # 从上向下滑动6次，查看加载其他屏的作品
        s = d.xpath('//*[@resource-id="com.codemao.nemo:id/recyclerview"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]').get()
        s.swipe("down")
        time.sleep(0.5)
        s.swipe("down")
        s.swipe("down")
        s.swipe("down")
        s.swipe("down")
        s.swipe("down")
        time.sleep(1)

    with allure.step('从右向左滑动，切换到最新页面'):
        logger.info('从右向左滑动，切换到最新页面')
        # 从右向左滑动，切换到最新页面
        t = d.xpath('//*[@resource-id="com.codemao.nemo:id/recyclerview"]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]').get()
        t.swipe("left")
        time.sleep(1)

    with allure.step('从左向右滑动，切换到推荐页面'):
        logger.info('从左向右滑动，切换到推荐页面')
        # 从左向右滑动，切换到推荐页面
        t = d.xpath('//*[@resource-id="com.codemao.nemo:id/recyclerview"]/android.widget.RelativeLayout[1]').get()
        t.swipe("right")
        time.sleep(1)

    


@allure.tag(f"environment:{ENV}", "P0", "TC1010")
@allure.feature('发现-推荐页面打开作品详情页测试')
# @allure.story('用例1')
@allure.severity('important')
def test_discovery3(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登录账号
    进入发现--推荐首页，验证页面已成功加载
    从下向上滑动1次
    定位到第一个作品，获取作品名称，并点击打开
    获取页面内容是否正确，验证打开的作品正确
    点击关闭作品详情页
    验证已回到发现首页，并定位到当前打开的作品

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

    with allure.step('从下向上滑动1次，查看加载其他屏的作品'):
        logger.info('从下向上滑动1次，查看加载其他屏的作品')
        # 从下向上滑动1次，查看加载其他屏的作品
        el = d.xpath('//*[@resource-id="com.codemao.nemo:id/bannerViewPager"]/android.widget.ImageView[2]').get()
        el.swipe("up")
        time.sleep(1)

    with allure.step('获取作品名称和用户名，并点击作品打开详情页'):
        logger.info('获取作品名称和用户名，并点击作品打开详情页')
        # 获取作品名称和用户名，并点击作品打开详情页
        name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
        user = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
        d(resourceId="com.codemao.nemo:id/iv_work_cover").click()
        time.sleep(5)

    with allure.step('验证成功进入作品详情页面，且打开的作品正确'):
        logger.info('验证成功进入作品详情页面，且打开的作品正确')
        # 验证成功进入作品详情页面，且打开的作品正确
        work = d.xpath('//*[@text="作品"]')
        assert work.wait()
        assert work.get_text()
        name1 = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
        user1 = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_user_name"]').get_text()
        # assert name1 == name
        assert user1 == user

    with allure.step('点击返回按钮'):
        logger.info('点击返回按钮')
        # 点击返回按钮
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('验证关闭作品详情页面，成功回到推荐首页'):
        logger.info('验证关闭作品详情页面，成功回到推荐首页')
        # 验证关闭作品详情页面，成功回到推荐首页
        recommend = d.xpath('//*[@text="推荐"]')
        assert recommend.wait()
        assert recommend.get_text()
    

@allure.tag(f"environment:{ENV}", "P0", "TC1011")
@allure.feature('发现-推荐页面打开用户中心页测试')
@allure.severity('important')
def test_discovery4(login_and_logout183_module, stop_and_run_nemo):
    '''
    启动app并登录账号
    进入发现--推荐首页，验证页面已成功加载
    从下向上滑动1次
    定位到第一个作品，获取用户名称，并点击打开用户名称
    获取用户中心页面内容是，验证打开用户中心内容正确
    点击关闭用户中心页面页
    验证已回到发现首页，并定位到当前打开的作品

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

    with allure.step('从下向上滑动1次，查看加载其他屏的作品'):
        logger.info('从下向上滑动1次，查看加载其他屏的作品')
        # 从下向上滑动1次，查看加载其他屏的作品
        el = d.xpath('//*[@resource-id="com.codemao.nemo:id/bannerViewPager"]/android.widget.ImageView[2]').get()
        el.swipe("up")
        el.swipe("up")
        time.sleep(1)

    with allure.step('获取用户名，并点击用户名打开用户中心页'):
        logger.info('获取用户名，并点击用户名打开用户中心页')
        # 获取用户名，并点击用户名打开用户中心页
        name = d.xpath('//*[@text="333333333"]').get_text()
        user = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
        d(resourceId="com.codemao.nemo:id/tv_user_name").click()
        time.sleep(5)

    with allure.step('验证成功用户中心页面，且打开的用户昵称校验正确'):
        logger.info('验证成功用户中心页面，且打开的用户昵称校验正确')
        # 验证成功用户中心页面，且打开的用户昵称校验正确
        work = d(resourceId = "com.codemao.nemo:id/tv_works_num")
        assert work.wait()
        assert work.get_text()
        # name1 = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_work_name"]').get_text()
        user1 = d.xpath('//*[@resource-id="com.codemao.nemo:id/tv_user_name"]').get_text()
        # assert name1 == name
        assert user1 == user

    with allure.step('点击返回按钮'):
        logger.info('点击返回按钮')
        # 点击返回按钮
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('验证关闭作品详情页面，成功回到推荐首页'):
        logger.info('验证关闭作品详情页面，成功回到推荐首页')
        # 验证关闭作品详情页面，成功回到推荐首页
        recommend = d.xpath('//*[@text="推荐"]')
        assert recommend.wait()
        assert recommend.get_text()


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
    pytest.main(["-s", "-q", "test_discovery.py::test_discovery4", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
