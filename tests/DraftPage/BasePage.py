
import time
# from tests.DraftPage.mylog import MyLog
from logs.my_logger import MyLog
from dir_config import testcase_dir
import uiautomator2 as u2
# from uiautomator2.session import Session
# from uiautomator2.widget import Widget
from dir_config import  log_dict

image_dir=testcase_dir+'DraftPage\\pic\\'
# device_name=f"{udid}"

class BasePage:

    def __init__(self):
        self.d=u2.connect(f"{udid}")
        # self.logger = MyLog(log_name='hzj',file_name=log_dict+time.strftime('%Y-%m-%d')+'.md')
        self.logger = MyLog().getlog()
        self.d.click_post_delay = 0.5  # default no delay
        self.d.wait_timeout = 30.0  # default 20.0

    # 等待元素可见,再点击
    def element_click(self, by, locator, wait_time=15):
        '''
        :param by: 指定定位方式
        :param locator: 传入元素的元组
        :param wait_time: 等待的时间
        :return: 无
        '''
        d = self.d
        try:
            self.logger.info(f"现在的操作为是：{locator.des}")
            if by == "id":
                d(resourceId=locator.id).click(timeout=wait_time)
                self.logger.info(f"点击成功：使用定位方法___{by}-{locator.id}，等待元素出现并点击")
            elif by == "text":
                d(text=locator.text).click(timeout=wait_time)
                self.logger.info(f"点击成功：使用定位方法___{by}-{locator.text}，等待元素出现并点击")
            elif by == "xpath":
                d.xpath(locator.xpath).click(timeout=wait_time)
                self.logger.info(f"点击成功：使用定位方法___{by}-{locator.xpath}，等待元素出现并点击")
            elif by=="c" or by=="coordinate":#使用定位坐标定位
                d.click(x=locator.coordinate[0],y=locator.coordinate[1])
                self.logger.info(f"点击成功：使用定位方法___{by}-{locator.coordinate}，等待元素出现并点击")
        except Exception as e:
            self.logger.info(f"出现错误请检查，错误原因是{e}")
            self.logger.info(f"使用定位___{by}-{locator.des},等待{wait_time}S后，还是没有找到元素")
            self.logger.info(f"错误截图的存储在___{image_dir}")
            self.save_img(img_name=image_dir + time.strftime('%Y%m%d_%H%M%S') + locator.des + '-定位错误.PNG')
            # raise e

    def save_img(self, img_name=image_dir + time.strftime('%Y%m%d_%H%M%S') + '.PNG'):
        self.logger.info("截图位置：%s" % (img_name))
        self.d.screenshot(img_name)

    def toast_message(self,wait_timeout=10,
                            cache_timeout=10,
                            default=None):
        '''
        获取toast
        :param wait_timeout:
        :param cache_timeout:
        :param default:
        :return: 返回toast值，string类型
        '''
        message = self.d.toast.get_message(wait_timeout=wait_timeout,
                            cache_timeout=cache_timeout,
                            default=default)
        return message

    def app_stop(self, pkg_name):
        """ Stop one application: am force-stop"""
        self.logger.info("关闭app：{}".format(pkg_name))
        self.d.app_stop(pkg_name)

    def app_start(self,
                  package_name,
                  activity=None,
                  extras={},
                  wait=False,
                  stop=False,
                  unlock=False,
                  launch_timeout=None,
                  use_monkey=False):
        self.logger.info("打开app：{}".format(package_name))
        self.d.app_start(package_name=package_name,
                  activity=activity,
                  extras=extras,
                  wait=wait,
                  stop=stop,
                  unlock=unlock,
                  launch_timeout=launch_timeout,
                  use_monkey=use_monkey)

    def ele_exist(self, **kwargs):
        '''
        :param kwargs:
        :return: 返回0、1
        示范：
        d.ele_exist(resourceId=scroll_view.id)
        '''
        if self.d(**kwargs).exists()==1:
            self.logger.info('元素存在：'+str(kwargs))
        else:
            self.logger.info('元素不存在：'+str(kwargs))
        return  self.d(**kwargs).exists()

    def app_list(self):
        '''
        返回设备上所有的appname
        :return:
        '''
        import subprocess
        aa = udid
        order = 'adb -s {} shell pm list packages'.format(aa)  # adb shell pm list packages
        print(order)
        '''
            :return: 已连接设备名
            '''
        # getstatusoutpu为元组，index为0时为状态，成功时为0，失败为1，后面为输出字符串，strip去除首尾空格
        pudid = subprocess.getstatusoutput(order)[1].strip()
        str2 = pudid.split('\n')
        str2.remove(str2[0])
        app_list = [i.split(':')[1] for i in str2]
        return app_list

    def app_current(self):
        '''
        返回设备上所有的appname
        :return:
        '''
        # self.logger.info('当前运行的app信息为：{}'.format(self.d.app_current()))
        return  self.d.app_current()

    # 显示等待时长
    def ele_sleep(self, wait_time,reason=None):
        self.logger.info(f"{reason}__等待{wait_time}S")
        time.sleep(wait_time)

    def swipe_ext(self,fx="left",scale=1):
        '''
        :return:
        示范：
        d = BasePage()
        d.swipe_ext("left",scale=0.8)
        '''
        if fx=="left":
            self.logger.info('从右向左滑动，滑动距离为屏幕宽度的{}'.format(scale))
            self.d.swipe_ext("left",scale=0.6)
        elif fx=="right":
            self.logger.info('从右向左滑动，滑动距离为屏幕宽度的{}'.format(scale))
            self.d.swipe_ext("right", scale=0.6)
        elif fx=="up":
            self.logger.info('从下向上滑动，滑动距离为屏幕宽度的{}'.format(scale))
            self.d.swipe_ext("up", scale=0.6)
        elif fx=="down":
            self.logger.info('从上向下滑动，滑动距离为屏幕宽度的{}'.format(scale))
            self.d.swipe_ext("down", scale=0.6)

    # def ele_swipe(self,fx, fy, tx, ty, duration=0.1, steps=None):
    #     self.d.swipe(fx=fx, fy=fy, tx=tx, ty=ty, duration=duration, steps=steps)


    #基于元素滑动
    def swipe(self,by,locator,direction='left', steps=10):
        """
        :param by:
        :param locator:
        :param direction:
        :param steps:
        :return:
        示范：
        d = BasePage()
        d.swipe('id',ll_Share_link)
        """
        d = self.d
        try:
            if by == "id":
                d(resourceId=locator.id).swipe(direction=direction,steps=steps)
            elif by == "text":
                d(text=locator.text).swipe(direction=direction,steps=steps)
            elif by == "xpath":
                d.xpath(locator.xpath).swipe(direction=direction,steps=steps)
            self.logger.info(f"{locator.des}_{direction}滑动成功")
        except Exception as e:
            self.logger.info(f"{direction}滑动失败")
            self.logger.info(f"错误截图的存储在___{image_dir}")
            self.save_img(img_name=image_dir + time.strftime('%Y%m%d_%H%M%S') + locator.des + '-定位错误.PNG')
            self.logger.info(f"错误原因：  {e}")
            raise e


    def send_text(self,text=None):
        '''
        :param text: 默认处理为str类型
        :return:
        示范:
        d.send_text('aaaa')
        '''
        self.d.set_fastinput_ime(True)  # 切换成FastInputIME输入法
        self.d.clear_text()  # 清除输入框所有内容(Require android-uiautomator.apk version >= 1.0.7)
        self.d.send_keys(text)  # adb广播输入
        self.d.set_fastinput_ime(False)  # 切换成正常的输入法
        # self.d.send_action("search")  # 模拟输入法的搜索

    def logger(self):
        return MyLog().getlog()

from collections import namedtuple
from data.cfg import udid
if __name__ == '__main__':
    ele_info = namedtuple('ele_info', ['des', 'id', 'text', 'xpath', 'coordinate'])
    mine_rb = ele_info('点击首页我的', 'com.codemao.nemo:id/mine_rb', '我的', '//android.widget.RadioButton', (0.797, 0.913))
    ll_Share_link = ele_info('草稿箱—分享链接', 'com.codemao.nemo:id/ll_Share_link', '无', '无', '无')
    aa = ele_info('测试', 'com.codemao.nemo:id/menu', 'com.codemao.nemo:id/works_cover_iv', '无', '无')
    bb=ele_info('测试', 'com.codemao.nemo:id/works_cover_iv', '无', '无', '无')
    d = BasePage()
    scroll_view = ele_info("草稿箱—分享时的滑动框", "com.codemao.nemo:id/scroll_view", '无', '无', '无')
    # d.swipe("id",scroll_view,'left')
    # d.ele_sleep(5,'测试')
    # d.swipe('id',ll_Share_link)
    # d.element_click('id',ll_Share_link)
    # d(resourceId="com.codemao.nemo:id/scroll_view").swipe("left", steps=10)
    # print(d.ele_exist(resourceId=scroll_view.id))
    d.send_text('2<3]OzU(!h')
    # d.logger.info('aa')



