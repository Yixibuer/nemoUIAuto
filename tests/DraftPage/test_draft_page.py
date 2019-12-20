import uiautomator2 as u2
import time
from data.cfg import udid
import allure
import pytest
from data.cfg import ENV, username183, password183
from logs.my_logger import MyLog
from time import sleep



'''
测试草稿箱页面
'''

# 调用日志模块
logger = MyLog().getlog()


@allure.tag(f"environment:{ENV}", "P0", "TC2001")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
def test_env_login_one(login_and_logout183):
    '''
      启动App
    点击切换环境按钮
    选择test环境并等待0.5s
    清空编程猫的app信息
    选择编程猫账号登录
    登录后草稿箱数目为0
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2

    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0

    with allure.step('点击物品的，进入草稿箱'):
        logger.info('进入我的页面')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
        draft_id = d(text="草稿箱(0)")
        assert draft_id.wait()
        assert draft_id.get_text() == "草稿箱(0)"
        logger.info('草稿箱数目为0')


@allure.tag(f"environment:{ENV}", "P0", "TC2002")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
def test_env_deaft_two(login_and_logout183):
    '''
    登录后点击自由创作后，作品可以新增成功
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2

    d.click_post_delay = 0.5  # default no delay
    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0

    logger.info('进入我的页面')
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    with allure.step('进入我的页面'):
        logger.info('自由创作第1个作品')
        logger.info('点击“创作”')
    with allure.step('点击创作'):
        d(resourceId="com.codemao.nemo:id/createBtn").click()
        sleep(3)
        logger.info('全新的作品')
    with allure.step('点击自由创作'):
        d(resourceId="com.codemao.nemo:id/item3_name").click()
        sleep(8)
        logger.info('点击菜单')
        d(resourceId="com.codemao.nemo:id/menu").click()
        sleep(3)
        logger.info('点击退出')
        d(resourceId="com.codemao.nemo:id/tv_quit").click()
        sleep(5)
    draft_id = d(text="草稿箱(1)")
    assert draft_id.wait()
    assert draft_id.get_text() == "草稿箱(1)"
    logger.info('自由创作创建一个作品成功')




@allure.tag(f"environment:{ENV}", "P0", "TC2003")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
def test_env_deaft_three(login_and_logout183):
    '''
    登录成功后，新增作品可以存储在草稿箱，草稿箱数目变与新增数相同
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2

    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step('进入我的页面'):
        logger.info('进入我的页面')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
    with allure.step('自由创作2个作品'):
        for i in  range(0,2):
            with allure.step('进入我的页面'):
                logger.info('自由创作{}个作品'.format(i))
                logger.info('点击“创作”')
                d(resourceId="com.codemao.nemo:id/createBtn").click()
                sleep(3)
                logger.info('全新的作品')
                d(resourceId="com.codemao.nemo:id/item3_name").click()
                sleep(8)
                logger.info('点击菜单')
                d(resourceId="com.codemao.nemo:id/menu").click()
                sleep(3)
                logger.info('点击退出')
                d(resourceId="com.codemao.nemo:id/tv_quit").click()
                sleep(5)
    draft_id = d(text="草稿箱(2)")
    assert draft_id.wait()
    assert draft_id.get_text() == "草稿箱(2)"


@allure.tag(f"environment:{ENV}", "P0", "TC2004")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
def test_env_draft_four(login_and_logout183):
    '''
    登录成功后，通过‘边学边做’可以新增作品成功
    '''
    d = u2.connect(f"{udid}")  # alias for u2.connect_usb('98899a474a4c535541')621QTCQH222F2

    d.click_post_delay = 0.5  # default no delay

    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    with allure.step("点击我的——进入我的页面"):
        logger.info('进入我的页面')
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
    with allure.step('进入我的页面'):
        logger.info('边学边做创做1个作品')
        logger.info('点击“创作”')
        d(resourceId="com.codemao.nemo:id/createBtn").click()
        sleep(3)
    with allure.step("选择边学边做"):
        logger.info('选择“边学边做”')
        d(resourceId="com.codemao.nemo:id/item1_name").click()
        sleep(8)
        logger.info('点击学习视频')
        d(resourceId="com.codemao.nemo:id/cover").click()
        logger.info('点击：去创造')
        d(text="去创作").click()
        sleep(5)
    with allure.step('退出创作页面'):
        logger.info('点击菜单')
        d(resourceId="com.codemao.nemo:id/menu").click()
        sleep(3)
        d(resourceId="com.codemao.nemo:id/menu").click()
        sleep(3)
        logger.info('点击退出')
        d(resourceId="com.codemao.nemo:id/tv_quit").click()
        sleep(5)
    draft_id = d(text="草稿箱(1)")
    assert draft_id.wait()
    logger.info('草稿箱有1个作品')
    assert draft_id.get_text() == "草稿箱(1)"


@allure.tag(f"environment:{ENV}", "P0", "TC2006")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
def test_env_draft_tc2006(login_and_logout183):
    '''
    登录成功后：
    1.进入 我的
    2.复制草稿箱内作品
    3.点击上云，作品上云
    4.点击删除，可以删除成功
    5.重复复制20次可以复制成功
    6.可以重复删除20次
    7.每次复制后都加编号，第一次复制直接为“副本”，没有编号
    8.复制的时候会检查序号，补充缺失的序号
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    with allure.step("点击复制"):
        d(resourceId="com.codemao.nemo:id/copy_iv").click()
        logger.info('点击复制')

    with allure.step("点击上云"):
        d(resourceId="com.codemao.nemo:id/cloud_up_iv").click()
        logger.info('点击上云')
        sleep(3)
    with allure.step("上云成功上云按钮消失"):
        assert d(resourceId='com.codemao.nemo:id/cloud_up_iv').exists()==0
        logger.info('上云按钮消失')
    with allure.step("点击删除"):
        d(resourceId="com.codemao.nemo:id/remove_iv").click()
        logger.info('点击删除')
        sleep(3)
    with allure.step("删除按钮消失"):
        logger.info("确认不删除")
        d(resourceId='com.codemao.nemo:id/remove_cancel').click()
        sleep(2)
        logger.info('删除按钮还在')
        sleep(2)
        assert d(resourceId='com.codemao.nemo:id/remove_iv').exists() == 1
        logger.info('点击删除')
        d(resourceId="com.codemao.nemo:id/remove_iv").click()
        logger.info("确认删除")
        d(resourceId='com.codemao.nemo:id/remove_confirm').click()
        sleep(2)
        assert d(resourceId='com.codemao.nemo:id/remove_iv').exists()==0
        logger.info('删除按钮消失')

    with allure.step("复制20次，每次检查作品名称后缀"):
        d(resourceId="com.codemao.nemo:id/copy_iv").click()
        sleep(5)
        assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()=='声控小火箭-副本'
        for i in range(1,21):
            d(resourceId="com.codemao.nemo:id/copy_iv").click()
            sleep(5)
            assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()=='声控小火箭-副本{}'.format(i+1)
            logger.info('新复制的作品名称为{}'.format(d(resourceId="com.codemao.nemo:id/works_name_tv").get_text()))
        logger.info('点击复制')
    # 删除副本20
    with allure.step("验证删除副本后，新增副本的编号补充删除的编号"):
        a = d.xpath(
            '//*[@resource-id="com.codemao.nemo:id/rvContainer"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[4]')
        a.click()
        sleep(2)
        d(resourceId='com.codemao.nemo:id/remove_confirm').click()
        logger.info("删除副本20，新的副本为副本20")
        # d(resourceId="com.codemao.nemo:id/copy_iv").click()
        sleep(5)
        logger.info("复制副本19，新的副本为副本20")
        b = d.xpath(
            '//*[@resource-id="com.codemao.nemo:id/rvContainer"]/android.widget.FrameLayout[2]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.ImageView[3]')
        sleep(5)
        b.click()
        sleep(5)
        assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text() == '声控小火箭-副本20'

@allure.tag(f"environment:{ENV}", "P0", "TC2007")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
def test_env_draft_tc2007(login_and_logout183):
    '''
    登录成功后：
    进入 我的
    复制草稿箱内作品
    点击编辑按钮，修改作品名称
    清空作品名
    取消重命名作品，作品名称不变
    输入新的名称，确认修改名称
    修改名称成功
    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    with allure.step("点击复制"):
        d(resourceId="com.codemao.nemo:id/copy_iv").click()
        logger.info('点击复制')
    with allure.step("修改作品名称"):
        logger.info('点击修改作品名称')
        d(resourceId="com.codemao.nemo:id/iv_edit_name").click()
        sleep(2)
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        logger.info('清空作品名')
        d.set_fastinput_ime(True)
        d.clear_text()
        sleep(2)
        logger.info('修改作品名称成功')
        d.send_keys(f"你好，大黄鸭")  # adb广播输入
    with allure.step('点击X，取消重命名'):
        d(resourceId="com.codemao.nemo:id/iv_close").click()
        sleep(2)
        assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text() == '声控小火箭-副本'
        logger.info("作品名称不变")
    with allure.step('点击确认'):
        logger.info('点击修改作品名称')
        d(resourceId="com.codemao.nemo:id/iv_edit_name").click()
        sleep(2)
        d(resourceId="com.codemao.nemo:id/edit_content").click()
        logger.info('清空作品名')
        d.clear_text()
        sleep(2)
        logger.info('修改作品名称成功')
        d.send_keys(f"你好大黄鸭")
        logger.info('切换回正常输入法')
        d.set_fastinput_ime(False)  # 切换成正常的输入法
        logger.info("点击确定")
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        sleep(5)
        assert d(resourceId="com.codemao.nemo:id/works_name_tv").get_text() == '你好大黄鸭'



@allure.tag(f"environment:{ENV}", "P0", "TC2008")
@allure.feature('草稿箱测试')
# @allure.story('用例1')
@allure.severity('important')
@allure.testcase('https://shimo.im/sheets/VOAWVRwnN0i8FYkZ/ylQht', name='测试用例链接')
@pytest.mark.smoke
@pytest.mark.hzj
#login_and_logout183
def test_env_draft_tc2008(login_and_logout183):
    '''
    登录成功后：
    进入 我的
    复制草稿箱内作品
    点击发布，跳转到发布页面
    点击“发布”，发布成功后进入“最新”页面
    回到我的页面，点击取消发布
    二次确认时，选择“保留发布”，作品没有取消发布
    二次确认时，选择“取消发布”，作品取消发布

    '''
    d = u2.connect(f"{udid}")
    d.click_post_delay = 0.5  # default no delay
    # set default element wait timeout (seconds)
    d.wait_timeout = 30.0  # default 20.0
    d(resourceId="com.codemao.nemo:id/mine_rb").click()
    with allure.step("点击复制"):
        d(resourceId="com.codemao.nemo:id/copy_iv").click()
        logger.info('点击复制')
        sleep(2)
    with allure.step("点击发作品"):
        logger.info('点击发布')
        d(resourceId="com.codemao.nemo:id/pub_iv").click()
        sleep(5)
        logger.info("跳转发布页面")
        logger.info("点击发布")
        d.click(0.887, 0.061)
        sleep(5)

    recommend = d.xpath('//*[@text="推荐"]')
    newest = d.xpath('//*[@text="最新"]')
    with allure.step('校验是否成功登录并进入首页，推荐按钮text校验：{}, 最新按钮text校验：{}'.format(
                recommend.get_text(), newest.get_text())):
        logger.info('校验是否成功登录并进入首页')
        assert recommend.get_text() == "推荐"
        assert newest.get_text() == "最新"
    with allure.step("二次确认是否取消发布"):
        d(resourceId="com.codemao.nemo:id/mine_rb").click()
        sleep(3)
        d(resourceId="com.codemao.nemo:id/pub_iv").click()
        sleep(5)
        logger.info("二次确认时点击保留发布")
        assert d(resourceId="com.codemao.nemo:id/tv_content").get_text()=="取消发布作品后他人将无法看到你的作品。"
        d(resourceId="com.codemao.nemo:id/tv_confirm").click()
        logger.info("作品没有取消发布成功")
        logger.info("没有删除按钮")
        assert d(resourceId='com.codemao.nemo:id/remove_iv').exists()==0
        assert d
        sleep(2)
        logger.info("点击取消发布")
        d(resourceId="com.codemao.nemo:id/pub_iv").click()
        d(resourceId="com.codemao.nemo:id/tv_cancel").click()
        logger.info("作品取消发布成功")
        sleep(5)
        logger.info("有删除按钮")
        # assert d(resourceId='com.codemao.nemo:id/remove_iv').exists()== 1

# a=test_env_draft_tc2008()