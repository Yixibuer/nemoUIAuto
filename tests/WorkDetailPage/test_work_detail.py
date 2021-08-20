import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog

'''
作品详情页(点赞/收藏/分享)测试用例
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "TC0005")
@allure.feature('作品详情页')
@allure.story('作品收藏')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_one(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品详情页收藏按钮功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('获取最新页第一个作品名字'):
        logger.info('获取最新页第一个作品名字')
        new_first_work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('点击“收藏”按钮'):
        logger.info('点击“收藏”按钮')
        d(resourceId="com.codemao.nemo:id/iv_collect").click()

    with allure.step('点击“返回”，退出作品详情页'):
        logger.info('点击“返回”，退出作品详情页')
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击用户名'):
        logger.info('点击用户名')
        d(resourceId="com.codemao.nemo:id/author_name_tv").click()

    with allure.step('点击“收藏”'):
        logger.info('点击“收藏”')
        d(text="收藏").click()
        time.sleep(0.5)

    with allure.step('获取收藏页面第一个作品名字'):
        logger.info('获取收藏页面第一个作品名字')
        collect_first_work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()

    with allure.step('判断最新页第一个作品名字等于收藏页面第一个作品名字'):
        logger.info('判断最新页第一个作品名字等于收藏页面第一个作品名字')
        assert new_first_work_name == collect_first_work_name

    with allure.step('点击“返回”'):
        logger.info('点击“返回”')
        d(resourceId="com.codemao.nemo:id/left_view").click()

    with allure.step('再次点击“返回”'):
        logger.info('再次点击“返回”')
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('点击“发现”'):
        logger.info('点击“发现”')
        d(resourceId="com.codemao.nemo:id/discover_rb").click()

    with allure.step('点击进入第一个作品详情页(返回该作品详情页)'):
        logger.info('点击进入第一个作品详情页(返回该作品详情页)')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('再次点击“收藏”按钮'):
        logger.info('再次点击“收藏”按钮')
        d(resourceId="com.codemao.nemo:id/iv_collect").click()

    with allure.step('点击“返回”，退出作品详情页'):
        logger.info('点击“返回”，退出作品详情页')
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('点击用户名'):
        logger.info('点击用户名')
        d(resourceId="com.codemao.nemo:id/author_name_tv").click()

    with allure.step('点击“收藏”'):
        logger.info('点击“收藏”')
        d(text="收藏").click()

    with allure.step('重新获取收藏页面第一个作品名字'):
        logger.info('重新获取收藏页面第一个作品名字')
        collect_first_work_name_now = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()

    with allure.step('判断最新页第一个作品名字不等于收藏页面第一个作品名字'):
        logger.info('判断最新页第一个作品名字不等于收藏页面第一个作品名字')
        assert new_first_work_name != collect_first_work_name_now

    allure.attach("最新页第一个作品名字new_first_work_name: {}\n"
                  "收藏页面第一个作品名字collect_first_work_name: {}\n"
                  "重新获取收藏页面第一个作品名字collect_first_work_name_now: {}\n".format(new_first_work_name,
                                                                            collect_first_work_name,
                                                                            collect_first_work_name_now), '用例参数',
                  allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0006")
@allure.feature('作品详情页')
@allure.story('作品点赞')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_two(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品详情页点赞按钮功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('获取最新页结果列表第一个作品的点赞数(01)'):
        logger.info('获取最新页结果列表第一个作品的点赞数(01)')
        new_first_praise_num01 = d(resourceId="com.codemao.nemo:id/tv_praise_num").get_text()
        new_first_praise_num01 = int(new_first_praise_num01)

    with allure.step('获取最新页第一个作品名字'):
        logger.info('获取最新页第一个作品名字')
        new_first_work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('点击“点赞”按钮'):
        logger.info('点击“点赞”按钮')
        d(resourceId="com.codemao.nemo:id/iv_praise").click()

    with allure.step('点击“返回”，退出作品详情页'):
        logger.info('点击“返回”，退出作品详情页')
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('沿着第一个作品封面下滑刷新'):
        logger.info('沿着第一个作品封面下滑刷新')
        el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_cover"]').get()
        el.swipe("down")  # 从上滑到下
        el.swipe("down")  # 从上滑到下

    with allure.step('等待5s'):
        logger.info('等待5s')
        time.sleep(5)

    with allure.step('寻找之前第一个作品，找不到则向上滑动'):
        logger.info('寻找之前第一个作品，找不到则向上滑动')
        new_first_work = d(text=new_first_work_name).exists
        if new_first_work:
            with allure.step('获取该作品最新点赞数(02)'):
                logger.info('获取该作品最新点赞数(02)')
                new_first_praise_num02 = d(text=new_first_work_name).down(resourceId="com.codemao.nemo:id/tv_praise_num"
                                                                          ).get_text()
                new_first_praise_num02 = int(new_first_praise_num02)
        else:
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_cover"]').get()
            el.swipe("up")  # 从下滑到上

    with allure.step('判断：之前获取的点赞数(01)+1等于现在的点赞数(02)'):
        logger.info('判断：之前获取的点赞数(01)+1等于现在的点赞数(02)')
        assert new_first_praise_num01 + 1 == new_first_praise_num02

    with allure.step('点击进入之前第一个作品详情页'):
        logger.info('点击进入之前第一个作品详情页')
        d(text=new_first_work_name).click()
        time.sleep(0.5)

    with allure.step('再次点击“点赞”按钮，取消点赞'):
        logger.info('再次点击“点赞”按钮，取消点赞')
        d(resourceId="com.codemao.nemo:id/iv_praise").click()

    with allure.step('点击“返回”，退出作品详情页'):
        logger.info('点击“返回”，退出作品详情页')
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('沿着第一个作品封面下滑刷新'):
        logger.info('沿着第一个作品封面下滑刷新')
        el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_cover"]').get()
        el.swipe("down")  # 从上滑到下
        el.swipe("down")  # 从上滑到下

    with allure.step('等待5s'):
        logger.info('等待5s')
        time.sleep(5)

    with allure.step('寻找之前第一个作品，找不到则向上滑动'):
        logger.info('寻找之前第一个作品，找不到则向上滑动')
        new_first_work = d(text=new_first_work_name).exists
        if new_first_work:
            with allure.step('获取该作品最新点赞数(02)'):
                logger.info('获取该作品最新点赞数(02)')
                new_first_praise_num03 = d(text=new_first_work_name).down(resourceId="com.codemao.nemo:id/tv_praise_num"
                                                                          ).get_text()
                new_first_praise_num03 = int(new_first_praise_num03)
        else:
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_cover"]').get()
            el.swipe("up")  # 从下滑到上

    with allure.step('判断：之前获取的点赞数(01)+1等于现在的点赞数(02)'):
        logger.info('判断：之前获取的点赞数(01)+1等于现在的点赞数(02)')
        assert new_first_praise_num02 - 1 == new_first_praise_num03

    allure.attach("获取的点赞数(01)new_first_praise_num01: {}\n"
                  "获取的点赞数(02)new_first_praise_num02: {}\n"
                  "获取的点赞数(03)new_first_praise_num03: {}\n".format(new_first_praise_num01,
                                                                  new_first_praise_num02,
                                                                  new_first_praise_num03), '用例参数',
                  allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0007")
@allure.feature('作品详情页')
@allure.story('作品分享')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_three(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品详情页分享按钮功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 1  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('点击“分享”按钮'):
        logger.info('点击“分享”按钮')
        d(resourceId="com.codemao.nemo:id/iv_share").click()

    with allure.step('左滑2次，找到“复制链接”'):
        logger.info('左滑2次，找到“复制链接”')
        for i in range(3):
            d(text='朋友圈').swipe("left", steps=10)  # 1 steps is about 5ms, so 20 steps is about 0.1s
        for i in range(3):
            d(text="QQ").swipe("left", steps=10)

    with allure.step('点击“复制链接”3次，分别获取toast进行校验，然后关闭弹窗'):
        logger.info('点击“复制链接”3次，分别获取toast进行校验，然后关闭弹窗')
        d(text="复制链接").click(3)
        message = d.toast.get_message()
        assert "链接已复制到剪贴板" in message
        time.sleep(1)
        d(text="复制链接").click(3)
        message = d.toast.get_message()
        assert "链接已复制到剪贴板" in message
        time.sleep(1)
        d(text="复制链接").click(3)
        message = d.toast.get_message()
        assert "链接已复制到剪贴板" in message
        time.sleep(1)
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()

    allure.attach("message: {}\n".format(message), '用例参数', allure.attachment_type.TEXT)


@allure.tag(f"environment:{ENV}", "TC0008")
@allure.feature('作品详情页')
@allure.story('作品播放页进入/退出')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_four(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证能否从作品详情页进入/退出Player播放页
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('获取该作品作品名'):
        logger.info('获取该作品作品名')
        work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()

    with allure.step('获取作者名'):
        logger.info('获取作者名')
        author_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()

    with allure.step('点击作品播放按钮'):
        logger.info('点击作品播放按钮')
        d(resourceId="com.codemao.nemo:id/iv_work_play").click()
        time.sleep(1)

    with allure.step('验证新页面有截图、点赞和重置按钮'):
        logger.info('验证新页面有截图、点赞和重置按钮')
        screenshoot_button = d.xpath('//*[@resource-id="com.codemao.nemo:id/iv_screenshoot"]')
        praise_button = d.xpath('//*[@resource-id="com.codemao.nemo:id/iv_praise"]')
        refresh_button = d.xpath('//*[@resource-id="com.codemao.nemo:id/iv_refresh"]')
        assert screenshoot_button.wait()
        assert praise_button.wait()
        assert refresh_button.wait()

    with allure.step('点击退出player播放页'):
        logger.info('点击退出player播放页')
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        time.sleep(0.5)

    with allure.step('获取当页作品名、作者名'):
        logger.info('获取当页作品名、作者名')
        work_name_now = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
        author_name_now = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()

    with allure.step('验证之前获取的作品名、作者名与现在获取的作品名、作者名一致'):
        logger.info('验证之前获取的作品名、作者名与现在获取的作品名、作者名一致')
        assert work_name == work_name_now
        assert author_name == author_name_now


@allure.tag(f"environment:{ENV}", "TC0009")
@allure.feature('作品详情页')
@allure.story('作品详情页信息验证')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_five(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证最新列表作品信息与作品详情页信息一致
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.implicitly_wait(10.0)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('点击“最新”'):
        logger.info('点击“最新”')
        d(text="最新").click()

    with allure.step('获取最新列表第一个作品的作品名、作者名'):
        logger.info('获取最新列表第一个作品的作品名、作者名')
        work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
        author_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()

    with allure.step('点击进入第一个作品详情页'):
        logger.info('点击进入第一个作品详情页')
        d(resourceId="com.codemao.nemo:id/tv_work_name").click()

    with allure.step('获取当页作品名、作者名'):
        logger.info('获取当页作品名、作者名')
        work_name_now = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
        author_name_now = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()

    with allure.step('验证之前获取的作品名、作者名与现在获取的作品名、作者名一致'):
        logger.info('验证之前获取的作品名、作者名与现在获取的作品名、作者名一致')
        assert work_name == work_name_now
        assert author_name == author_name_now


@allure.tag(f"environment:{ENV}", "TC0010")
@allure.feature('作品详情页')
@allure.story('作品再创作')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_six(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品详情页再创作按钮功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
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

    with allure.step('找寻作品，如果不是自己名字，才点击进去(点进去如果找不到再创作按钮（即不开源），退出滑动再寻找)'):
        logger.info('找寻作品，如果不是自己名字，才点击进去(点进去如果找不到再创作按钮（即不开源），退出滑动再寻找)')
        while True:
            logger.info('找寻作品，如果不是自己名字，才点击进去')
            # 自动匹配第一个，即使有多个元素拥有此ID
            user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
            if user_name == my_name:
                d.swipe_ext("up", scale=0.1)
            else:
                d(text=user_name).click()
                work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
                OpenSource = d(resourceId="com.codemao.nemo:id/iv_rework_num").exists
                if not OpenSource:
                    logger.info('退出作品详情页')
                    d(resourceId="com.codemao.nemo:id/iv_back").click()
                    time.sleep(0.5)
                    d.swipe_ext("up", scale=0.1)
                else:
                    break

    with allure.step('点击再创作按钮'):
        logger.info('点击再创作按钮')
        d(resourceId="com.codemao.nemo:id/iv_rework_num").click()
        time.sleep(0.5)

    with allure.step('校验弹出页面的title是否等于“再创作也是学习的好方式”'):
        logger.info('校验弹出页面的title是否等于“再创作也是学习的好方式”')
        title = d(resourceId="com.codemao.nemo:id/tv_title").get_text()
        assert title == "再创作也是学习的好方式"

    with allure.step('点击“学习代码”按钮'):
        logger.info('点击“学习代码”按钮')
        d(resourceId="com.codemao.nemo:id/tv_go_to_work").click()

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
        time.sleep(1)

    with allure.step('校验草稿箱第一个作品名字包含之前获取的作品名'):
        logger.info('校验草稿箱第一个作品名字包含之前获取的作品名')
        work_name_box = d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()
        assert work_name in work_name_box


@allure.tag(f"environment:{ENV}", "TC0011")
@allure.feature('作品详情页')
@allure.story('作品再创作-稍后打开')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_seven(login_and_logout183_module, stop_and_run_nemo):
    '''
    验证作品详情页再创作按钮的"稍后打开"功能是否正常
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # 这个用例的“稍后打开”消失较快，所以用0s间隔去点击
    d.click_post_delay = 0  # default no delay
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

    with allure.step('找寻作品，如果不是自己名字，才点击进去(点进去如果找不到再创作按钮（即不开源），退出滑动再寻找)'):
        logger.info('找寻作品，如果不是自己名字，才点击进去(点进去如果找不到再创作按钮（即不开源），退出滑动再寻找)')
        while True:
            logger.info('找寻作品，如果不是自己名字，才点击进去')
            # 自动匹配第一个，即使有多个元素拥有此ID
            user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
            if user_name == my_name:
                d.swipe_ext("up", scale=0.1)
            else:
                d(text=user_name).click()
                time.sleep(1)
                work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
                OpenSource = d(resourceId="com.codemao.nemo:id/iv_rework_num").exists()
                if not OpenSource:
                    logger.info('退出作品详情页')
                    d(resourceId="com.codemao.nemo:id/iv_back").click()
                    time.sleep(0.5)
                    d.swipe_ext("up", scale=0.1)
                else:
                    break

    with allure.step('获取再创作数'):
        logger.info('获取再创作数')
        time.sleep(0.5)
        rework_number = int(d(resourceId="com.codemao.nemo:id/tv_to_rework",
                              className="android.widget.TextView").get_text())
        logger.info(f'获取再创作数rework_number的值是{rework_number}')

    with allure.step('点击再创作按钮'):
        logger.info('点击再创作按钮')
        d(resourceId="com.codemao.nemo:id/iv_rework_num").click()
        time.sleep(0.5)

    with allure.step('校验弹出页面的title是否等于“再创作也是学习的好方式”'):
        logger.info('校验弹出页面的title是否等于“再创作也是学习的好方式”')
        title = d(resourceId="com.codemao.nemo:id/tv_title").get_text()
        assert title == "再创作也是学习的好方式"

    with allure.step('点击“学习代码”'):
        logger.info('点击“学习代码”')
        d(resourceId="com.codemao.nemo:id/tv_go_to_work").click()

    with allure.step('此时点击“稍后打开”按钮'):
        logger.info('此时点击“稍后打开”按钮')
        if d.xpath("//android.widget.TextView[contains(@text, '打开')]").exists:
            d.xpath("//android.widget.TextView[contains(@text, '打开')]").click_nowait()
        else:
            raise Exception('找不到"稍后打开"按钮')

    with allure.step('校验是否弹出toast："已加入我的作品，稍后可在我的中查看"'):
        logger.info('校验是否弹出toast："已加入我的作品，稍后可在我的中查看"')
        message = d.toast.get_message()
        assert "已加入我的作品，稍后可在我的中查看" in message

    with allure.step('退出作品详情页'):
        logger.info('退出作品详情页')
        d(resourceId="com.codemao.nemo:id/iv_back").click()

    with allure.step('找寻刚才的作品，点击进去'):
        logger.info('找寻刚才的作品，点击进去')
        d(text=work_name).click()

    with allure.step('获取此时的再创作数rework_number_now'):
        logger.info('获取此时的再创作数rework_number_now')
        time.sleep(0.5)
        rework_number_now = int(d(resourceId="com.codemao.nemo:id/tv_to_rework",
                                  className="android.widget.TextView").get_text())
        assert rework_number + 1 == rework_number_now

    with allure.step('退出作品详情页'):
        logger.info('退出作品详情页')
        d(resourceId="com.codemao.nemo:id/iv_back", className="android.widget.ImageView").click()

    with allure.step('点击“我的”'):
        logger.info('点击“我的”')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()

    with allure.step('校验草稿箱第一个作品名字包含之前获取的作品名'):
        logger.info('校验草稿箱第一个作品名字包含之前获取的作品名')
        work_name_box = d(resourceId="com.codemao.nemo:id/works_name_tv")[0].get_text()
        assert work_name in work_name_box


@allure.tag(f"environment:{ENV}", "TC0012")
@allure.feature('作品详情页')
@allure.story('作品再创作-稍后打开')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://lanhuapp.com/web/#/item/project/product?focusItem=825c5b9a-bfef-4910-9302-1789d761bf42&pid='
                 '959752fe-24c5-48ba-a1ad-38a8caaf5862&docId=040f1304-c481-4d3e-9900-fc832422ae99&docType=axure&pageId'
                 '=1cb4203398864bffb00f2b2de88cd24e&image_id=040f1304-c481-4d3e-9900-fc832422ae99&parentId=77f1514d-d7'
                 'e5-43d5-8bbf-caff6ee02f9b', name='蓝湖')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
def test_work_detail_eight(login_and_logout183_module, stop_and_run_nemo):
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
                time.sleep(1)
                work_name = d(resourceId="com.codemao.nemo:id/tv_work_name").get_text()
                tv_follow = d(resourceId="com.codemao.nemo:id/tv_follow").get_text()
                if tv_follow == "已关注":
                    logger.info('退出作品详情页')
                    d(resourceId="com.codemao.nemo:id/iv_back").click()
                    time.sleep(0.5)
                    d.swipe_ext("up", scale=0.1)
                else:
                    break

    with allure.step('点击下面关注按钮，关注作者'):
        logger.info('点击下面关注按钮，关注作者')
        d(resourceId="com.codemao.nemo:id/tv_follow").click()

    with allure.step('点击作者头像进入作者个人首页'):
        logger.info('点击作者头像进入作者个人首页')
        d(resourceId="com.codemao.nemo:id/iv_user_avatar").click()

    with allure.step('点击粉丝,进入粉丝列表'):
        logger.info('点击粉丝,进入粉丝列表')
        d(resourceId="com.codemao.nemo:id/tv_fan_num").click()

    with allure.step('查看粉丝列表是否有我的名字'):
        logger.info('查看粉丝列表是否有我的名字')
        while True:
            logger.info('找寻粉丝列表')
            # 自动匹配第一个，即使有多个元素拥有此ID
            if not d(resourceId="com.codemao.nemo:id/tv_user_name").exists():
                logger.info('粉丝列表为空')
                break
            user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
            if user_name != my_name:
                d.swipe_ext("up", scale=0.1)
                if d(text="喵~已经到最后啦！").exists():
                    for view in d(resourceId="com.codemao.nemo:id/tv_user_name"):
                        if view.get_text() == my_name:
                            logger.info('已找到我的名字')
                            break
                    raise Exception("我的名字不在粉丝列表中")
            elif user_name == my_name:
                logger.info('已找到我的名字')
                break
            else:
                raise Exception("未知错误")

    with allure.step('后退两步回到作品详情页，点击取消关注'):
        logger.info('后退两步回到作品详情页，点击取消关注')
        d.press("back")
        d.press("back")
        time.sleep(1)
        d(text="已关注").click()

    with allure.step('检验弹出toast是否为：您已经取消了对Ta的关注'):
        logger.info('检验弹出toast是否为：您已经取消了对Ta的关注')
        message = d.toast.get_message()
        assert "您已经取消了对Ta的关注" in message

    with allure.step('点击作者头像进入作者个人首页'):
        logger.info('点击作者头像进入作者个人首页')
        d(resourceId="com.codemao.nemo:id/iv_user_avatar").click()

    with allure.step('点击粉丝,进入粉丝列表'):
        logger.info('点击粉丝,进入粉丝列表')
        d(resourceId="com.codemao.nemo:id/tv_fan_num").click()

    with allure.step('查看粉丝列表应该没有我的名字'):
        logger.info('查看粉丝列表应该没有我的名字')
        while True:
            logger.info('找寻粉丝列表')
            # 自动匹配第一个，即使有多个元素拥有此ID
            user_name = d(resourceId="com.codemao.nemo:id/tv_user_name").get_text()
            if user_name != my_name:
                d.swipe_ext("up", scale=0.1)
                if d(text="喵~已经到最后啦！").exists():
                    for view in d(resourceId="com.codemao.nemo:id/tv_user_name"):
                        if view.get_text() == my_name:
                            logger.info('已找到我的名字')
                            raise Exception("我的名字还在粉丝列表中")
                    break
            elif user_name == my_name:
                logger.info('已找到我的名字')
                raise Exception("我的名字还在粉丝列表中")
            else:
                raise Exception("未知错误")


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
    pytest.main(["-s", "-q", "test_work_detail.py", "--alluredir", path_xml])
    # pytest.main(["-lf", "-q", "-s", "test_work_detail.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
