                                                                    #Name:         test_share_draft_pulished.PY
# Author:       dell
# Date:         2019/12/28
# Name:         test_share_draft_pulished
# Description: 测试草稿箱页面和已发布页面的分享功能
from collections import namedtuple
import uiautomator2 as u2
from data.cfg import udid
import allure
import pytest
import time
from data.cfg import ENV
from tests.DraftPage.BasePage import BasePage
from time import sleep
from dir_config import testcase_dir
# d = u2.connect(f"192.168.1.102:5555")
d =BasePage()


#元素的定位
ele_info = namedtuple('ele_info', ['des', 'id', 'text', 'xpath', 'coordinate'])
mine_rb = ele_info('点击首页我的', 'com.codemao.nemo:id/mine_rb', '我的', '//android.widget.RadioButton',(0.797, 0.913))
copy_iv=ele_info('草稿箱—点击复制按钮','com.codemao.nemo:id/copy_iv','无','无',(0.908, 0.503))
share_iv=ele_info( '草稿箱—点击分享按钮', 'com.codemao.nemo:id/share_iv', '无', '无', '无')
ll_Share_wechat=ele_info('草稿箱—分享到微信好友', 'com.codemao.nemo:id/ll_Share_wechat', '无', '无', '无')
ll_Share_circle=ele_info('草稿箱—分享到微信朋友圈好友', 'com.codemao.nemo:id/ll_Share_circle', '无', '无', '无')
ll_Share_qq=ele_info('草稿箱—分享到QQ好友', 'com.codemao.nemo:id/ll_Share_qq', '无', '无', '无')
ll_Share_qzone=ele_info('草稿箱—分享到QQ空间', 'com.codemao.nemo:id/ll_Share_qzone', '无', '无', '无')
ll_Share_link= ele_info('草稿箱—分享链接', 'com.codemao.nemo:id/ll_Share_link', '无', '无', '无')
ll_share_save= ele_info('草稿箱—保存图片', 'com.codemao.nemo:id/ll_share_save', '无', '无', '无')
ll_share_miao= ele_info('草稿箱—分享喵口令', 'com.codemao.nemo:id/ll_share_miao', '无', '无', '无')
bt_parse= ele_info('草稿箱—分享喵口令点击去粘贴', 'com.codemao.nemo:id/bt_parse', '去粘贴', '无',(0.613, 0.601))
icon_close_loading=ele_info("草稿箱—分享图片正在生成时点击取消","com.codemao.nemo:id/icon_close_loading", '无', '无', '无')
iv_close=ele_info("草稿箱—分享图片创建成功后点击取消","com.codemao.nemo:id/iv_close", '无', '无',(0.471, 0.8))
miao_iv_close=ele_info("草稿箱—喵口令创建成功后点击取消", "com.codemao.nemo:id/iv_close", '无', '无', (0.489, 0.688))
scroll_view=ele_info("草稿箱—分享时的滑动框", "com.codemao.nemo:id/scroll_view", '无', '无', '无')
permission_allow_button=ele_info("系统询问是否有读取图片权限", "com.codemao.nemo:id/permission_allow_button", '无', '无', '无')
# bt_parse=ele_info("喵口令-去粘贴", "com.codemao.nemo:id/bt_parse", '无', '无', (0.613, 0.601))
iv_close2=ele_info("是否打开喵口令——点击取消","com.codemao.nemo:id/iv_close", '无', '无',(0.471, 0.8))



#已发布页面按钮
published_button=ele_info("已发布—点击进入已发布页面", "无", "已发布(*)", "//*[contains(@text, '已发布')]", (0.489, 0.688))
p_tv_work_name=ele_info("已发布—点击作品标题，进入作品", "com.codemao.nemo:id/tv_work_name", "无","无", (0.463, 0.709))
p_iv_share=ele_info( '已发布—点击分享按钮', 'com.codemao.nemo:id/iv_share', '无', '无', '无')
p_share_wechat=ele_info('已发布—分享到微信好友', '无', '微信好友', '无', '无')
p_share_circle=ele_info('已发布—分享到微信朋友圈', '无', '朋友圈', '无', '无')
p_share_qq=ele_info('已发布—分享到QQ好友', '无', 'QQ', '无', '无')
p_share_qzone=ele_info('已发布—分享到QQ空间', '无', 'QQ空间', '无', '无')
p_share_link= ele_info('已发布—分享链接', '无', '复制链接', '无', '无')
p_tv_cancel=ele_info("已发布—分享链接_取消分享", "com.codemao.nemo:id/tv_cancel", '无', '无', (0.489, 0.688))


#图片的存储位置
img_name=testcase_dir+'DraftPage\\pic\\'+time.strftime('%Y%m%d_%H%M%S')


def app_currrent():
    sleep(5)
    weixin = 'com.tencent.mm'
    QQ = "com.tencent.mobileqq"
    a = d.app_current()
    if weixin==(a["package"]):
        weinxin_current=1
    else:
        weinxin_current = 0
    if QQ == (a["package"]):
        QQ_current = 1
    else:
        QQ_current = 0
    app_list = d.app_list()
    if QQ in app_list:
        qq_install = 1
    else:
        qq_install = 0
    if weixin in app_list:
        wx_install = 1
    else:
        wx_install = 0
    return weinxin_current,QQ_current,qq_install,wx_install

weinxin_current=app_currrent()[0]
QQ_current=app_currrent()[1]
qq_install=app_currrent()[2]
wx_install=app_currrent()[3]



@allure.tag(f"environment:{ENV}", "P0", "TC2015")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品——微信好友')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
# @pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_draft_share_tc2015(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享到微信好友
    复制一个作品
    然后分享到微信好友
    如果分享失败就截图
    '''
    a='草稿箱点击分享到微信好友'
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    #print(d(resourceId=ll_Share_wechat.id).exists(timeout=3)) #TODO 检查元素是否存在，需要继续调试
    # print(d.element_exist('id',ll_Share_wechat))
    with allure.step('点击分享到微信好友'):
        d.logger.info("校验是否跳转到微信")
        try:
            #d.element_click("id", ll_Share_wechat)
            #d.element_click2("id","com.tencent.mm:id/ln")
            weinxin_current==1
            d.logger.info("已经跳转到到微信页面")
        except:
            d.logger.info("没有跳转到微信选择发送页面，请查看失败截图")
            # d.save_img(img_name+'分享到微信失败截图.png')
    d.logger.info(f'{a}成功')

@allure.tag(f"environment:{ENV}", "P0", "TC2016")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品——微信朋友圈')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
# @pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_draft_share_tc2016(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享到微信朋友圈
    复制一个作品
    然后分享到微信朋友圈
    如果没有跳转朋友圈则判断分享失败且截图
    '''
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    with allure.step('点击分享到微信好友'):
        d.logger.info("校验是否跳转到微信")
        try:
            # d.element_click("id", ll_Share_circle)
            # d.element_click2("text","所在位置")
            weinxin_current == 1
            d.logger.info("已经跳转到微信页面")
        except:
            d.logger.info("没有跳转到到微信朋友圈发表页面，请查看失败截图")

@allure.tag(f"environment:{ENV}", "P0", "TC2017")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_draft_share_tc2017(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享到QQ好友
    复制一个作品
    然后分享到QQ好友
    如果没有跳转QQ好友则判断分享失败且截图
    '''
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    with allure.step('点击分享到QQ好友'):
        d.logger.info("校验是否跳转到QQ好友")
        try:
            # d.element_click("id", ll_Share_qq)
            # d.element_click2("text","发送给")
            QQ_current==1
            d.logger.info("已经成功跳转到到QQ页面")
        except:
            d.logger.info("没有跳转到到QQ好友页面，请查看失败截图")


@allure.tag(f"environment:{ENV}", "P0", "TC2018")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
# @pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
@pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_draft_share_tc2018(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享到QQ空间
    复制一个作品
    然后分享到QQ空间
    如果没有跳转QQ空间则判断分享失败且截图
    '''
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    with allure.step('点击分享到QQ空间'):
        d.logger.info("校验是否跳转到QQ空间")
        try:
            # d.element_click("id", ll_Share_qzone)
            # d.element_click2("text","写说说")
            QQ_current==1
            d.logger.info("已经成功跳转到到QQ页面")
        except:
            d.logger.info("没有跳转到到QQ到QQ空间，请查看失败截图")

@allure.tag(f"environment:{ENV}", "P0", "TC2019")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('https://www.tapd.cn/47849719/bugtrace/bugreports/my_view', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_draft_share_tc2019(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享链接
    复制一个作品
    然后分享链接
    如果获取toast：复制成功，则判断分享失败且截图
    '''
    a="分享链接"
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    with allure.step(f'点击分享：{a}'):
        d.element_click("id", ll_Share_link)
        d.logger.info(f"校验是否{a}")
        try:
            message = d.toast_message()
            d.logger.info(f"{a}获取toast成功，toast为：{message}")
            assert "复制成功" in message
        except:
            d.logger.info(f"{a}获取toast失败，请查看失败截图")
            d.save_img(img_name+'获取toast失败.png')

@allure.tag(f"environment:{ENV}", "P0", "TC2020")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=1,reruns_delay=2)
def test_draft_share_tc2020(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享图片
    复制一个作品
    然后分享图片
    如果获取toast：图片保存成功，则判断分享失败且截图
    '''
    a="分享图片"
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    sleep(5)
    d.swipe("id",scroll_view,'left')
    with allure.step(f'点击分享：{a}'):
        d.element_click("id", ll_share_save)
        d.logger.info(f"校验是否{a}")
        sleep(5)
        # d.ele_exist(resourceId=permission_allow_button.id)
        if d.ele_exist(resourceId=permission_allow_button.id):
            try:
                d.logger.info("获取相册权限")
                time.sleep(3)
                d.element_click('id',permission_allow_button)
            except:
                d.logger.info("获取相册权限失败，请检查")
        else:
            d.logger.info("不需要获取相册权限")
        try:
            message = d.toast_message()
            d.logger.info(f"{a}获取toast成功，toast为：{message}")
            assert "图片保存成功" in message
        except:
            d.logger.info(f"{a}获取toast失败，请查看失败截图")
            d.save_img(img_name+'获取toast失败.png')

@allure.tag(f"environment:{ENV}", "P0", "TC2021")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.run(order=1)
def test_draft_share_tc2021(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享喵口令
    复制一个作品
    然后分享图片
    如果获取toast：图片保存成功，则判断分享失败且截图
    关闭喵口令
    '''
    a="分享喵口令"
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    d.swipe("id",scroll_view,'left')
    with allure.step(f'点击分享：{a}'):
        d.element_click("id", ll_share_miao,wait_time=30)
        try:
            d.element_click("id",bt_parse)#TODO 喵口令定位不到“去粘贴”
        except:
            d.logger.info('元素定位失败，采用坐标定位')
            d.element_click('c',bt_parse)
        try:
            message = d.toast_message()
            d.logger.info(f"{a}获取toast成功，toast为：{message}")
            assert "喵口令已粘贴成功" in message
        except:
            d.logger.info(f"{a}获取toast失败，请查看失败截图")
            d.save_img(img_name+'获取toast失败.png')
        d.app_stop("com.codemao.nemo")
        d.app_start("com.codemao.nemo")
        d.ele_sleep(15,'等待app重启')
        d.element_click("id", iv_close2)


@allure.tag(f"environment:{ENV}", "P0", "TC2022")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_draft_share_tc2022(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享
    生成取消分享，回到草稿箱页面
    '''
    a="生成分享页面时点击取消分享"
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    with allure.step(f'点击分享：{a}'):
        d.element_click("id", icon_close_loading,wait_time=30)
        d.logger.info(f"校验是否{a}")
        try:
            d.logger.info(f"{a}成功时,直接回到草稿箱页面")
        except:
            d.logger.info(f"{a}失败,请查看截图")
            d.save_img(img_name+a+'.png')
    d.logger.info(f"{a}运行成功")


@allure.tag(f"environment:{ENV}", "P0", "TC2023")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_draft_share_tc2023(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享
    生成图片成功后取消分享，回到草稿箱页面
    '''
    a="生成分享图片生成后，点击取消分享"
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    with allure.step(f'点击分享：{a}'):
        d.element_click("id", iv_close,wait_time=30)
        d.logger.info(f"校验是否：{a}")
        try:
            d.logger.info(f"{a}成功时,直接回到草稿箱页面")
        except:
            d.logger.info(f"{a}失败,请查看截图")
            d.save_img(img_name+a+'.png')
    d.logger.info(f"{a}运行成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2024")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('草稿箱分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_draft_share_tc2024(login_and_logout183):
    '''
    验证作品详情页分享按钮功能是否正常---草稿箱分享
    喵口令生成成功后取消分享，回到草稿箱页面
    '''
    a="生成分享图片生成后，点击取消分享"
    d.logger.info(mine_rb.des)
    d.element_click('id', mine_rb)
    d.element_click("id",copy_iv)
    d.element_click("id",share_iv)
    d.swipe("id",scroll_view,'left')
    with allure.step(f'点击分享：{a}'):
        d.element_click("id", ll_share_miao, wait_time=30)
        d.logger.info(f"校验是否：{a}")
        d.element_click("id", miao_iv_close)
        try:
            d.logger.info(f"{a}成功时,直接回到草稿箱页面")
        except:
            d.logger.info(f"{a}失败,请查看截图")
            d.save_img(img_name+a+'.png')
    d.logger.info(f"{a}运行成功")


def pubilsh_share():
    '''
    定义登陆成功后进入已发布作品分享
    :return:
    '''
    d.element_click('id', mine_rb)
    d.element_click("xpath", published_button)
    d.element_click("id", p_tv_work_name)
    d.element_click("id",p_iv_share)


@allure.tag(f"environment:{ENV}", "P0", "TC2025")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('已发布分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
# @pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_pulished_share_tc2025(login_and_logout183):
    '''
    进入已发布作品详情页
    点击分享
    分享微信好友
    '''
    a="已发布作品，分享微信好友"
    pubilsh_share()
    with allure.step(f'点击分享：{a}'):
        d.logger.info("校验是否跳转到微信")
        try:
            # d.element_click("text", p_share_wechat)
            # d.element_click2("id","com.tencent.mm:id/ln")
            weinxin_current==1
            # d.logger.info("已经跳转到到微信选择发送页面")
            d.logger.info("已经跳转到到微信页面")
        except:
            d.logger.info("没有跳转到微信选择发送页面，请查看失败截图")
            d.save_img(img_name+'分享到微信失败截图.png')
    d.logger.info(f"{a}运行成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2026")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('已发布分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
@pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
# @pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_pulished_share_tc2026(login_and_logout183):
    '''
    进入已发布作品详情页
    点击分享
    分享微信朋友圈
    '''
    a="已发布作品，分享微信朋友圈"
    pubilsh_share()
    with allure.step(f'点击分享：{a}'):
        d.logger.info("校验是否跳转到微信朋友圈")
        try:
            # d.element_click("text", p_share_wechat)
            # d.element_click2("id","com.tencent.mm:id/ln")
            weinxin_current == 1
            # d.logger.info("已经跳转到到微信选择发送页面")
            d.logger.info("已经跳转到到微信页面")
        except:
            d.logger.info("没有跳转到到微信朋友圈发表页面，请查看失败截图")
    d.logger.info(f"{a}运行成功")


@allure.tag(f"environment:{ENV}", "P0", "TC2027")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('已发布分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
# @pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
@pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_pulished_share_tc2027(login_and_logout183):
    '''
    进入已发布作品详情页
    点击分享
    分享到QQ好友
    '''
    a="已发布作品，分享分享到QQ好友"
    pubilsh_share()
    with allure.step(a):
        d.logger.info("校验是否跳转到分享到QQ好友")
        try:
            # d.element_click("text", p_share_qq)
            # d.element_click2("text", "发送给")
            # d.logger.info("已经成功跳转到到QQ好友页面")
            QQ_current == 1
            d.logger.info("已经跳转到到QQ页面")
        except:
            d.logger.info("没有跳转到到QQ好友页面，请查看失败截图")
    d.logger.info(f"{a}运行成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2028")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('已发布分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
# @pytest.mark.skipif(wx_install==0,reason='设备没有安装微信')
@pytest.mark.skipif(qq_install==0,reason='设备没有安装QQ')
def test_pulished_share_tc2028(login_and_logout183):
    '''
    进入已发布作品详情页
    点击分享
    分享到QQ空间
    '''
    a="已发布作品，分享分享到QQ空间"
    pubilsh_share()
    with allure.step(f'点击分享：{a}'):
        d.logger.info("校验是否跳转到分享到QQ空间")
        try:
            # d.element_click("text", p_share_qzone)
            # d.element_click2("text", "写说说")
            # d.logger.info("已经成功跳转到到QQ空间")
            QQ_current == 1
            d.logger.info("已经跳转到到QQ页面")
        except:
            d.logger.info("没有跳转到到QQ到QQ空间，请查看失败截图")
    d.logger.info(f"{a}运行成功")

@allure.tag(f"environment:{ENV}", "P0", "TC2029")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('已发布分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_pulished_share_tc2029(login_and_logout183):
    '''
    进入已发布作品详情页
    点击分享
    分享复制链接
    '''
    a="已发布作品，分享链接"
    pubilsh_share()
    with allure.step(f'点击分享：{a}'):
        d.logger.info(f"校验是否{a}")
        try:
            d.element_click("text",p_share_link)
            message = d.toast_message()
            d.logger.info(f"{a}获取toast成功，toast为：{message}")
            assert "复制" in message
        except:
            d.logger.info(f"{a}获取toast失败，请查看失败截图")
            d.save_img(img_name + '获取toast失败.png')
    d.logger.info(f"{a}运行成功")


@allure.tag(f"environment:{ENV}", "P0", "TC2030")
@allure.feature('草稿箱页面、已发布页面')
@allure.story('已发布分享作品')
@allure.severity('normal')  # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@allure.issue('暂无', name='TAPD-缺陷')
@pytest.mark.P0
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_pulished_share_tc2030(login_and_logout183):
    '''
    进入已发布作品详情页
    点击分享
    点击-取消分享按钮。留在当前页面
    '''
    a="已发布作品，关闭分享"
    pubilsh_share()
    with allure.step(f'点击分享：{a}'):
        d.logger.info(f"校验是否{a}")
        d.element_click("id", p_tv_cancel)
        try:
            d.ele_exist(resourceId=p_iv_share.id).exists()==1
        except:
            d.save_img(img_name + '关闭失败.png')
    d.logger.info(f"{a}运行成功")

if __name__ == '__main__':
    # pytest.main(["-k", "2006"])
    import subprocess
    import sys
    import os

    path_xml = os.path.join(sys.path[1], r"report\xml")
    path_html = os.path.join(sys.path[1], r"report\html")
    path_report = os.path.join(sys.path[1], r"report")
    # 先删除report文件夹
    subprocess.run('rmdir /s/q ' + path_report, shell=True, check=True)
    # # pytest.main(["-s", "-q", "--alluredir", path_xml])
    pytest.main(["-s", "-q", "test_share_draft_and_pulished.py", "--alluredir", path_xml])
    subprocess.run(r'allure generate ' + path_xml + ' -o ' + path_html + ' --clean', shell=True, check=True)
    subprocess.run(r'allure serve ' + path_xml, shell=True, check=True)
