import uiautomator2 as u2
import pprint
import time
from data.cfg import udid



'''
起始页：未登录点击进入Nemo第一页
登录后再退出
如此循环。。。
'''


def circulate():
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('123456f')
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0w'w'w'w'w'w'w'w'w'w'w'w'w'w'w'w'w'w'w
    # print(d.info)

    # #第一种方法，启动App（包名）
    # d.app_start("com.codemao.nemo")
    # d.app_wait("com.codemao.nemo", front=True) # 等待应用前台运行
    # d.app_wait("ccom.codemao.nemo", timeout=20.0) # 最长等待时间20s（默认）
    # pid = d.app_wait("com.codemao.nemo") # 等待应用运行, return pid(int)
    # if not pid:
    #     print("com.codemao.nemo is not running")
    # else:
    #     print("ccom.codemao.nemo pid is %d" % pid)

    # 第二种方法，启动App(包名)，使用session
    # launch app if not running, skip launch if already running
    # d.app_stop("com.codemao.nemo")
    # nemo = d.session("com.codemao.nemo")
    # nemo.click_post_delay = 0.5 # default no delay
    # nemo.wait_timeout = 30.0 # default 20.0
    # nemo.implicitly_wait(30)
    d.xpath.global_set("timeout", 10)
    # pprint.pprint(nemo.info)

    #开始登陆
    d(resourceId="com.codemao.nemo:id/tv_change").click()
    d(resourceId="com.codemao.nemo:id/tv_test").click()
    time.sleep(0.5)
    d(resourceId="com.codemao.nemo:id/iv_Login_account").click()
    d(resourceId="com.codemao.nemo:id/edit_user_name").click()
    d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
    d.send_keys("18319138088")  # adb广播输入
    d(resourceId="com.codemao.nemo:id/et_password").click()
    d.send_keys("123456")  # adb广播输入
    d.set_fastinput_ime(False)  # 切换成正常的输入法
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
    assert recommend.get_text() == "推荐"
    assert newest.get_text() == "最新"
    #退出登录
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    d(resourceId="com.codemao.nemo:id/left_view").click()
    # d.swipe(0.582, 0.904, 0.539, 0.631, 0.5)  # swipe for 0.5s(default)
    el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_enter"]').get()
    el.swipe("up")  # 从下滑到上
    el = d.xpath('//*[@resource-id="com.codemao.nemo:id/rl_about"]').get()
    el.swipe("up")  # 从下滑到上
    d(resourceId="com.codemao.nemo:id/tv_logout").click()


if __name__ == '__main__':
    for i in range(20):
        circulate()
        print('已运行{}次'.format(i + 1))

