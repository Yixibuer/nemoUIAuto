import allure
import pytest
from logs.my_logger import MyLog
import time
from data.cfg import udid, ENV, username183, password183
import uiautomator2 as u2




#调用日志模块
logger = MyLog().getlog()


def pytest_collection_modifyitems(items):
    '''
    测试用例收集完成时，将收集到的items的name和nodeid的中文显示在控制台上
    '''
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")

# #注册别名
# def pytest_configure(config):
#     config.addinivalue_line(
#         "markers", "huanghongliang"
#     )
#     config.addinivalue_line(
#         "markers", "huanghongliang2"
#     )


KeyWords_list = ['测试', 'y', '作品', '1', '-']
KeyWords_ids = ["搜索关键词：%s" % t for t in KeyWords_list]


@pytest.fixture(params=KeyWords_list, ids=KeyWords_ids)
@allure.step(r'输入中文、英文、符号、数字等关键字进行搜索')
def SearchKeyWords(request):
    '''返回测试数据'''
    # 注意conftest.py里的sys.path[1]只识别到D盘(项目所在根盘符)
    return request.param


@pytest.fixture()
def stop_and_run_nemo(request):
    '''
    前置：
    1.停止当前Nemo进程
    2.启动Nemo
    后置：
    1.停止当前Nemo进程
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.1  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    # print(d.info)

    # # #第一种方法，启动App（包名）
    # #为避免正在运行先停止
    # with allure.step('为避免正在运行先停止'):
    #     logger.info('为避免正在运行先停止')
    #     d.app_stop("com.codemao.nemo")

    with allure.step('第一种方法，启动App（包名）'):
        logger.info('第一种方法，启动App（包名）')
        d.app_start("com.codemao.nemo")
        d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
        d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
        pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
        if not pid:
            print("com.codemao.nemo is not running")
        else:
            print("com.codemao.nemo pid is %d" % pid)

    yield

    @allure.step('step in "Tear down" from conftest.py')
    def my_tear_down():
        with allure.step('获取设备udid'):
            logger.info('获取设备udid')
            d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
            d.debug = True
            # d.implicitly_wait(10.0)
            # set delay 0.5s after each UI click and click
            d.click_post_delay = 0.1  # default no delay

            # set default element wait timeout (seconds)
            d.wait_timeout = 30.0  # default 20.0
            # print(d.info)

        # #第一种方法，启动App（包名）
        # 为避免正在运行先停止
        with allure.step('停止运行Nemo'):
            logger.info('停止运行Nemo')
            d.app_stop("com.codemao.nemo")
    request.addfinalizer(my_tear_down)


@pytest.fixture()
def log_out_nemo(request):
    '''
    后置：
    重启App，进入后点击我的，设置按钮，下滑，点击退出登录
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    yield

    @allure.step('step in "Tear down" from conftest.py')
    def my_tear_down():
        with allure.step('获取设备udid'):
            logger.info('获取设备udid')
            d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
            # d.debug = True
            # d.implicitly_wait(10.0)
            # set delay 0.5s after each UI click and click
            d.click_post_delay = 0.5  # default no delay

            # set default element wait timeout (seconds)
            d.wait_timeout = 30.0  # default 20.0
            # print(d.info)

        # #第一种方法，启动App（包名）
        # 为避免正在运行先停止
        with allure.step('为避免正在运行先停止'):
            logger.info('为避免正在运行先停止')
            d.app_stop("com.codemao.nemo")

        with allure.step('第一种方法，启动App（包名）'):
            logger.info('第一种方法，启动App（包名）')
            d.app_start("com.codemao.nemo")
            d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
            d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
            pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
            if not pid:
                print("com.codemao.nemo is not running")
            else:
                print("com.codemao.nemo pid is %d" % pid)

        with allure.step('点击我的'):
            logger.info('点击我的')
            # 退出登录
            d(resourceId="com.codemao.nemo:id/mine_rb").click()

        with allure.step('点击设置按钮'):
            logger.info('点击设置按钮')
            d(resourceId="com.codemao.nemo:id/left_view").click()

        with allure.step('从下滑到上（两次）'):
            logger.info('从下滑到上（两次）')
            # d.swipe(0.582, 0.904, 0.539, 0.631, 0.5)  # swipe for 0.5s(default)
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_enter"]').get()
            el.swipe("up")  # 从下滑到上
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_about"]').get()
            el.swipe("up")  # 从下滑到上

        with allure.step('点击退出登录'):
            logger.info('点击退出登录')
            d(resourceId="com.codemao.nemo:id/tv_logout").click()

    request.addfinalizer(my_tear_down)


@pytest.fixture()
def login_nemo_test183(request):
    '''
    前置：
    重启App，选择编程猫账号登录，点击编程猫账号，切换FastInputIME输入法，输入账号密码，点击确定。校验首页发现text和我的text
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    # print(d.info)

    # #第一种方法，启动App（包名）
    #为避免正在运行先停止
    with allure.step('为避免正在运行先停止'):
        logger.info('为避免正在运行先停止')
        d.app_stop("com.codemao.nemo")

    with allure.step('第一种方法，启动App（包名）'):
        logger.info('第一种方法，启动App（包名）')
        d.app_start("com.codemao.nemo")
        d.app_wait("com.codemao.nemo", front=True) # 等待应用前台运行
        d.app_wait("com.codemao.nemo", timeout=5.0) # 最长等待时间20s（默认）
        pid = d.app_wait("com.codemao.nemo") # 等待应用运行, return pid(int)
        if not pid:
            print("com.codemao.nemo is not running")
        else:
            print("com.codemao.nemo pid is %d" % pid)

    # 第二种方法，启动App(包名)，使用session
    # launch app if not running, skip launch if already running
    # d.app_stop("com.codemao.nemo")
    # nemo = d.session("com.codemao.nemo")
    # nemo.click_post_delay = 0.5 # default no delay
    # nemo.wait_timeout = 30.0 # default 20.0
    # nemo.implicitly_wait(30)
    with allure.step('设置xpath全局等待10s'):
        logger.info('设置xpath全局等待10s')
        d.xpath.global_set("timeout", 10)
    # pprint.pprint(nemo.info)

    # with allure.step('点击切换环境按钮'):
    #     logger.info('点击切换环境按钮')
    #     d(resourceId="com.codemao.nemo:id/tv_change").click()
    #
    # with allure.step('选择test环境并等待0.5s'):
    #     logger.info('选择test环境并等待0.5s')
    #     d(resourceId="com.codemao.nemo:id/tv_test").click()
    #     time.sleep(0.5)

    with allure.step('选择编程猫账号登录'):
        logger.info('选择编程猫账号登录')
        d(resourceId="com.codemao.nemo:id/iv_Login_account").click()

    with allure.step('点击账号，并切换成FastInputIME输入法输入username183'):
        logger.info('点击账号，并切换成FastInputIME输入法输入username183')
        d(resourceId="com.codemao.nemo:id/edit_user_name").click()
        # time.sleep(0.5)
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{username183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{username183}")

    with allure.step('点击密码，输入password183'):
        logger.info('点击密码，输入password183')
        d(resourceId="com.codemao.nemo:id/et_password").click()
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{password183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{password183}")

    with allure.step('切换回正常输入法并点击登录按钮'):
        logger.info('切换回正常输入法并点击登录按钮')
        # d.set_fastinput_ime(False)  # 切换成正常的输入法
        d(resourceId="com.codemao.nemo:id/bt_Login").click()

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

    with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
            recommend.get_text(), newest.get_text())):
        logger.info('校验是否成功登录并进入首页')
        assert recommend.get_text() == "推荐"
        assert newest.get_text() == "最新"

    yield


@pytest.fixture()
def login_and_logout183(request):
    '''
    前置：
    重启App，选择编程猫账号登录，点击编程猫账号，切换FastInputIME输入法，输入账号密码，点击确定。校验首页发现text和我的text
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    后置：
    重启App，进入后点击我的，设置按钮，下滑，点击退出登录。
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    # print(d.info)

    # #第一种方法，启动App（包名）
    #为避免正在运行先停止
    with allure.step('为避免正在运行先停止'):
        logger.info('为避免正在运行先停止')
        d.app_stop("com.codemao.nemo")

    with allure.step('第一种方法，启动App（包名）'):
        logger.info('第一种方法，启动App（包名）')
        d.app_start("com.codemao.nemo")
        d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
        d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
        pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
        if not pid:
            print("com.codemao.nemo is not running")
        else:
            print("com.codemao.nemo pid is %d" % pid)

    # 第二种方法，启动App(包名)，使用session
    # launch app if not running, skip launch if already running
    # d.app_stop("com.codemao.nemo")
    # nemo = d.session("com.codemao.nemo")
    # nemo.click_post_delay = 0.5 # default no delay
    # nemo.wait_timeout = 30.0 # default 20.0
    # nemo.implicitly_wait(30)
    with allure.step('设置xpath全局等待10s'):
        logger.info('设置xpath全局等待10s')
        d.xpath.global_set("timeout", 10)
    # pprint.pprint(nemo.info)

    # with allure.step('点击切换环境按钮'):
    #     logger.info('点击切换环境按钮')
    #     d(resourceId="com.codemao.nemo:id/tv_change").click()
    #
    # with allure.step('选择test环境并等待0.5s'):
    #     logger.info('选择test环境并等待0.5s')
    #     d(resourceId="com.codemao.nemo:id/tv_test").click()
    #     time.sleep(0.5)

    with allure.step('选择编程猫账号登录'):
        logger.info('选择编程猫账号登录')
        d(resourceId="com.codemao.nemo:id/iv_Login_account").click()

    with allure.step('点击账号，并切换成FastInputIME输入法输入username183'):
        logger.info('点击账号，并切换成FastInputIME输入法输入username183')
        d(resourceId="com.codemao.nemo:id/edit_user_name").click()
        # time.sleep(0.5)
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{username183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{username183}")

    with allure.step('点击密码，输入password183'):
        logger.info('点击密码，输入password183')
        d(resourceId="com.codemao.nemo:id/et_password").click()
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{password183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{password183}")

    with allure.step('切换回正常输入法并点击登录按钮'):
        logger.info('切换回正常输入法并点击登录按钮')
        # d.set_fastinput_ime(False)  # 切换成正常的输入法
        d(resourceId="com.codemao.nemo:id/bt_Login").click()

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

    with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
            recommend.get_text(), newest.get_text())):
        logger.info('校验是否成功登录并进入首页')
        assert recommend.get_text() == "推荐"
        assert newest.get_text() == "最新"

    yield

    @allure.step('step in "Tear down" from conftest.py')
    def my_tear_down():
        with allure.step('获取设备udid'):
            logger.info('获取设备udid')
            d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
            # d.debug = True
            # d.implicitly_wait(10.0)
            # set delay 0.5s after each UI click and click
            d.click_post_delay = 0.5  # default no delay

            # set default element wait timeout (seconds)
            d.wait_timeout = 30.0  # default 20.0
            # print(d.info)

        # #第一种方法，启动App（包名）
        # 为避免正在运行先停止
        with allure.step('为避免正在运行先停止'):
            logger.info('为避免正在运行先停止')
            d.app_stop("com.codemao.nemo")

        with allure.step('第一种方法，启动App（包名）'):
            logger.info('第一种方法，启动App（包名）')
            d.app_start("com.codemao.nemo")
            d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
            d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
            pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
            if not pid:
                print("com.codemao.nemo is not running")
            else:
                print("com.codemao.nemo pid is %d" % pid)

        with allure.step('点击我的'):
            logger.info('点击我的')
            # 退出登录
            d(resourceId="com.codemao.nemo:id/mine_rb").click()

        with allure.step('点击设置按钮'):
            logger.info('点击设置按钮')
            d(resourceId="com.codemao.nemo:id/left_view").click()

        with allure.step('从下滑到上（两次）'):
            logger.info('从下滑到上（两次）')
            # d.swipe(0.582, 0.904, 0.539, 0.631, 0.5)  # swipe for 0.5s(default)
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_enter"]').get()
            el.swipe("up")  # 从下滑到上
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_about"]').get()
            el.swipe("up")  # 从下滑到上

        with allure.step('点击退出登录'):
            logger.info('点击退出登录')
            d(resourceId="com.codemao.nemo:id/tv_logout").click()

    request.addfinalizer(my_tear_down)


@pytest.fixture(scope="session")
def login_and_logout183_session(request):
    '''
    前置：
    重启App，选择编程猫账号登录，点击编程猫账号，切换FastInputIME输入法，输入账号密码，点击确定。校验首页发现text和我的text
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    后置：
    重启App，进入后点击我的，设置按钮，下滑，点击退出登录。
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    # print(d.info)

    # #第一种方法，启动App（包名）
    #为避免正在运行先停止
    with allure.step('为避免正在运行先停止'):
        logger.info('为避免正在运行先停止')
        d.app_stop("com.codemao.nemo")

    with allure.step('第一种方法，启动App（包名）'):
        logger.info('第一种方法，启动App（包名）')
        d.app_start("com.codemao.nemo")
        d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
        d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
        pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
        if not pid:
            print("com.codemao.nemo is not running")
        else:
            print("com.codemao.nemo pid is %d" % pid)

    # 第二种方法，启动App(包名)，使用session
    # launch app if not running, skip launch if already running
    # d.app_stop("com.codemao.nemo")
    # nemo = d.session("com.codemao.nemo")
    # nemo.click_post_delay = 0.5 # default no delay
    # nemo.wait_timeout = 30.0 # default 20.0
    # nemo.implicitly_wait(30)
    with allure.step('设置xpath全局等待10s'):
        logger.info('设置xpath全局等待10s')
        d.xpath.global_set("timeout", 10)
    # pprint.pprint(nemo.info)

    # with allure.step('点击切换环境按钮'):
    #     logger.info('点击切换环境按钮')
    #     d(resourceId="com.codemao.nemo:id/tv_change").click()
    #
    # with allure.step('选择test环境并等待0.5s'):
    #     logger.info('选择test环境并等待0.5s')
    #     d(resourceId="com.codemao.nemo:id/tv_test").click()
    #     time.sleep(0.5)

    with allure.step('选择编程猫账号登录'):
        logger.info('选择编程猫账号登录')
        d(resourceId="com.codemao.nemo:id/iv_Login_account").click()

    with allure.step('点击账号，并切换成FastInputIME输入法输入username183'):
        logger.info('点击账号，并切换成FastInputIME输入法输入username183')
        d(resourceId="com.codemao.nemo:id/edit_user_name").click()
        # time.sleep(0.5)
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{username183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{username183}")

    with allure.step('点击密码，输入password183'):
        logger.info('点击密码，输入password183')
        d(resourceId="com.codemao.nemo:id/et_password").click()
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{password183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{password183}")

    with allure.step('切换回正常输入法并点击登录按钮'):
        logger.info('切换回正常输入法并点击登录按钮')
        # d.set_fastinput_ime(False)  # 切换成正常的输入法
        d(resourceId="com.codemao.nemo:id/bt_Login").click()

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

    with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
            recommend.get_text(), newest.get_text())):
        logger.info('校验是否成功登录并进入首页')
        assert recommend.get_text() == "推荐"
        assert newest.get_text() == "最新"

    yield

    @allure.step('step in "Tear down" from conftest.py')
    def my_tear_down():
        with allure.step('获取设备udid'):
            logger.info('获取设备udid')
            d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
            # d.debug = True
            # d.implicitly_wait(10.0)
            # set delay 0.5s after each UI click and click
            d.click_post_delay = 0.5  # default no delay

            # set default element wait timeout (seconds)
            d.wait_timeout = 30.0  # default 20.0
            # print(d.info)

        # #第一种方法，启动App（包名）
        # 为避免正在运行先停止
        with allure.step('为避免正在运行先停止'):
            logger.info('为避免正在运行先停止')
            d.app_stop("com.codemao.nemo")

        with allure.step('第一种方法，启动App（包名）'):
            logger.info('第一种方法，启动App（包名）')
            d.app_start("com.codemao.nemo")
            d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
            d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
            pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
            if not pid:
                print("com.codemao.nemo is not running")
            else:
                print("com.codemao.nemo pid is %d" % pid)

        with allure.step('点击我的'):
            logger.info('点击我的')
            # 退出登录
            d(resourceId="com.codemao.nemo:id/mine_rb").click()

        with allure.step('点击设置按钮'):
            logger.info('点击设置按钮')
            d(resourceId="com.codemao.nemo:id/left_view").click()

        with allure.step('从下滑到上（两次）'):
            logger.info('从下滑到上（两次）')
            # d.swipe(0.582, 0.904, 0.539, 0.631, 0.5)  # swipe for 0.5s(default)
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_enter"]').get()
            el.swipe("up")  # 从下滑到上
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_about"]').get()
            el.swipe("up")  # 从下滑到上

        with allure.step('点击退出登录'):
            logger.info('点击退出登录')
            d(resourceId="com.codemao.nemo:id/tv_logout").click()

    request.addfinalizer(my_tear_down)


@pytest.fixture(scope="module")
def login_and_logout183_module(request):
    '''
    前置：
    重启App，选择编程猫账号登录，点击编程猫账号，切换FastInputIME输入法，输入账号密码，点击确定。校验首页发现text和我的text
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    后置：
    重启App，进入后点击我的，设置按钮，下滑，点击退出登录。
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    # print(d.info)

    # #第一种方法，启动App（包名）
    #为避免正在运行先停止
    with allure.step('为避免正在运行先停止'):
        logger.info('为避免正在运行先停止')
        d.app_stop("com.codemao.nemo")

    with allure.step('第一种方法，启动App（包名）'):
        logger.info('第一种方法，启动App（包名）')
        d.app_start("com.codemao.nemo")
        d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
        d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
        pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
        if not pid:
            print("com.codemao.nemo is not running")
        else:
            print("com.codemao.nemo pid is %d" % pid)

    # 第二种方法，启动App(包名)，使用session
    # launch app if not running, skip launch if already running
    # d.app_stop("com.codemao.nemo")
    # nemo = d.session("com.codemao.nemo")
    # nemo.click_post_delay = 0.5 # default no delay
    # nemo.wait_timeout = 30.0 # default 20.0
    # nemo.implicitly_wait(30)
    with allure.step('设置xpath全局等待10s'):
        logger.info('设置xpath全局等待10s')
        d.xpath.global_set("timeout", 10)
    # pprint.pprint(nemo.info)

    # with allure.step('点击切换环境按钮'):
    #     logger.info('点击切换环境按钮')
    #     d(resourceId="com.codemao.nemo:id/tv_change").click()
    #
    # with allure.step('选择test环境并等待0.5s'):
    #     logger.info('选择test环境并等待0.5s')
    #     d(resourceId="com.codemao.nemo:id/tv_test").click()
    #     time.sleep(0.5)

    with allure.step('选择编程猫账号登录'):
        logger.info('选择编程猫账号登录')
        d(resourceId="com.codemao.nemo:id/iv_Login_account").click()

    with allure.step('点击账号，并切换成FastInputIME输入法输入username183'):
        logger.info('点击账号，并切换成FastInputIME输入法输入username183')
        d(resourceId="com.codemao.nemo:id/edit_user_name").click()
        # time.sleep(0.5)
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{username183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{username183}")

    with allure.step('点击密码，输入password183'):
        logger.info('点击密码，输入password183')
        d(resourceId="com.codemao.nemo:id/et_password").click()
        # d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        # d.send_keys(f"{password183}")  # adb广播输入
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{password183}")

    with allure.step('切换回正常输入法并点击登录按钮'):
        logger.info('切换回正常输入法并点击登录按钮')
        # d.set_fastinput_ime(False)  # 切换成正常的输入法
        d(resourceId="com.codemao.nemo:id/bt_Login").click()

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

    with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
            recommend.get_text(), newest.get_text())):
        logger.info('校验是否成功登录并进入首页')
        assert recommend.get_text() == "推荐"
        assert newest.get_text() == "最新"

    yield

    @allure.step('step in "Tear down" from conftest.py')
    def my_tear_down():
        with allure.step('获取设备udid'):
            logger.info('获取设备udid')
            d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
            # d.debug = True
            # d.implicitly_wait(10.0)
            # set delay 0.5s after each UI click and click
            d.click_post_delay = 0.5  # default no delay

            # set default element wait timeout (seconds)
            d.wait_timeout = 30.0  # default 20.0
            # print(d.info)

        # #第一种方法，启动App（包名）
        # 为避免正在运行先停止
        with allure.step('为避免正在运行先停止'):
            logger.info('为避免正在运行先停止')
            d.app_stop("com.codemao.nemo")

        with allure.step('第一种方法，启动App（包名）'):
            logger.info('第一种方法，启动App（包名）')
            d.app_start("com.codemao.nemo")
            d.app_wait("com.codemao.nemo", front=True)  # 等待应用前台运行
            d.app_wait("com.codemao.nemo", timeout=5.0)  # 最长等待时间20s（默认）
            pid = d.app_wait("com.codemao.nemo")  # 等待应用运行, return pid(int)
            if not pid:
                print("com.codemao.nemo is not running")
            else:
                print("com.codemao.nemo pid is %d" % pid)

        with allure.step('点击我的'):
            logger.info('点击我的')
            # 退出登录
            d(resourceId="com.codemao.nemo:id/mine_rb").click()

        with allure.step('点击设置按钮'):
            logger.info('点击设置按钮')
            d(resourceId="com.codemao.nemo:id/left_view").click()

        with allure.step('从下滑到上（两次）'):
            logger.info('从下滑到上（两次）')
            # d.swipe(0.582, 0.904, 0.539, 0.631, 0.5)  # swipe for 0.5s(default)
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_enter"]').get()
            el.swipe("up")  # 从下滑到上
            el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_about"]').get()
            el.swipe("up")  # 从下滑到上

        with allure.step('点击退出登录'):
            logger.info('点击退出登录')
            d(resourceId="com.codemao.nemo:id/tv_logout").click()

    request.addfinalizer(my_tear_down)


@pytest.fixture(scope='module')
def login_and_logout190(request):
    '''
    前置：
    重启App，选择编程猫账号登录，点击编程猫账号，切换FastInputIME输入法，输入账号密码，点击确定。校验首页发现text和我的text
    request.addfinalizer(func)和yield相比不同的是：无论是固件的“setup”部分是否出现异常或断言失败，它都会执行。
    此外它还支持传入多个函数。
    :param request:
    :return:
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2
    d.click_post_delay = 0.5  # default no delay
    d.wait_timeout = 30.0  # default 20.0
    # #第一种方法，启动App（包名）
    #为避免正在运行先停止
    logger.info("*"*20+'hzj'+'用例开始啦'+"*"*20)
    d.app_clear("com.codemao.nemo")
    d.app_start("com.codemao.nemo")
    d.app_wait("com.codemao.nemo", front=True) # 等待应用前台运行
    d.app_wait("com.codemao.nemo", timeout=5.0) # 最长等待时间20s（默认）
    pid = d.app_wait("com.codemao.nemo") # 等待应用运行, return pid(int)
    if not pid:
        print("com.codemao.nemo is not running")
    else:
        print("com.codemao.nemo pid is %d" % pid)

    with allure.step('选择编程猫账号登录'):
        d.set_fastinput_ime(True)
        logger.info('选择编程猫账号登录')
        time.sleep(1)
        d(resourceId="com.codemao.nemo:id/iv_Login_account").click()
        d(resourceId="com.codemao.nemo:id/edit_user_name").click()
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{username183}")
        time.sleep(0.5)
        logger.info('点击密码，输入password183')
        d(resourceId="com.codemao.nemo:id/et_password").click()
        d(focused=True).clear_text()
        d(focused=True).set_text(f"{password183}")
        time.sleep(0.5)
        d(resourceId="com.codemao.nemo:id/bt_Login").click()
        time.sleep(0.5)
        d.set_fastinput_ime(False)  # 切换成正常的输入法

    yield
    logger.info("*"*20+'hzj'+'用例结束啦'+"*"*20)
    d.app_clear('com.codemao.nemo')

