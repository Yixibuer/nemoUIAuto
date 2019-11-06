import uiautomator2 as u2
import pprint
import time
from data.cfg import udid


'''
进入创作页内，运行脚本
'''


def circulate():
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('123456f')
    # d.debug = True
    # d.implicitly_wait(10.0)
    # set delay 0.5s after each UI click and click
    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
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

    d.xpath('//*[@resource-id="com.codemao.nemo:id/rv_roles"]/android.view.ViewGroup[3]').click()
    d(resourceId="com.codemao.nemo:id/iv_top").click()
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[1]').click()
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[2]').click()
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[3]').get()
    el.swipe("up")  # 从下滑到上
    time.sleep(0.2)
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[3]').click()
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[4]').get()
    el.swipe("up")  # 从下滑到上
    time.sleep(0.2)
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[4]').click()
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[5]').click()
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[6]').click()
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[7]').get()
    el.swipe("up")  # 从下滑到上
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[7]').click()
    time.sleep(0.2)
    el.swipe("up")  # 从下滑到上
    time.sleep(0.2)
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[8]').get()
    el.swipe("up")  # 从下滑到上
    time.sleep(0.2)
    d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[8]').click()
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[9]').get()
    el.swipe("up")  # 从下滑到上
    time.sleep(0.2)
    el.swipe("up")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[9]').click()
    time.sleep(0.2)
    #再次点击收回
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[9]').click()
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[9]').get()
    el.swipe("down")  # 从上滑到    time.sleep(0.2)
    time.sleep(0.2)
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[8]').get()
    el.swipe("down")  # 从下滑到    time.sleep(0.2)    time.sleep(0.2)
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[7]').get()
    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)
    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[6]').get()
    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)
    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    el = d.xpath('//*[@content-desc="Codemao Blockly"]/android.view.View[1]/android.view.View[5]').get()
    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    el.swipe("down")  # 从下滑到    time.sleep(0.2)
    time.sleep(0.2)

    d(resourceId="com.codemao.nemo:id/iv_bottom").click()
    time.sleep(0.2)
    d(resourceId="com.codemao.nemo:id/tv_title", text="烟雾").click()

if __name__ == '__main__':
    for i in range(20):
        circulate()
        print('已运行{}次'.format(i + 1))



